import json
import os
from typing import Optional, Dict, Any, List, cast

from toolz import pipe
from eth_account.signers.local import LocalAccount
from web3 import Web3

from kwil.kwild import Kwild
from kwil.provider import BaseProvider
from kwil.manager import RequestManager as DefaultRequestManager
from kwil.types import (
    TxPayloadType,
    TxParams,
    Nonce,
    TxReceipt,
    DatasetIdentifier,
    DBIdentifier,
    ActionExecution
)
from kwil._utils.transaction import Transaction, sign_tx
from kwil._utils.action import encode_action_args
from kwil._utils.dataset import generate_dbi


class Kwil:

    RequestManager = DefaultRequestManager

    kwild: Kwild
    web3: Web3

    def __init__(
            self,
            provider: Optional[BaseProvider] = None,
            wallet: Optional[LocalAccount] = None,
            ):
        self.manager = self.RequestManager(self, provider)

        self.kwild = Kwild(self)
        self._wallet = wallet

    @property
    def kwil_provider(self) -> BaseProvider:
        return self.manager.provider

    @kwil_provider.setter
    def kwil_provider(self, provider: BaseProvider) -> None:
        self.manager.provider = provider

    @property
    def wallet(self) -> LocalAccount:
        return self._wallet

    @wallet.setter
    def wallet(self, wallet: LocalAccount) -> None:
        self._wallet = wallet

    @property
    def api(self) -> str:
        from kwil import __version__
        return __version__

    def _create_tx(self, payload_type: TxPayloadType, payload: bytes) -> TxParams:
        account_info = self.kwild.get_account(self.wallet.address)

        tx_params = TxParams(
            payloadType=payload_type,
            payload=payload,
            sender=self.wallet.address,
            fee="0",
            # SHOULD be done in result formatter
            nonce=Nonce(int(account_info["nonce"]) + 1),
            # nonce=Nonce(1),
        )

        price = self.kwild.estimate_price(tx_params)
        tx_params["fee"] = price
        tx_params = sign_tx(tx_params, self.wallet)
        return tx_params

    def deploy_database(self, payload: bytes) -> TxReceipt:
        payload_type = TxPayloadType.DEPLOY_DATABASE
        tx_params = self._create_tx(payload_type, payload)

        # print("hash", [b for b in tx_params["hash"]])
        # print("payloadType", tx_params["payloadType"])
        # print("payload", [b for b in tx_params["payload"]])
        # print("fee", tx_params["fee"])
        # print("nonce", tx_params["nonce"])
        # # print("signature", tx_params["signature"])
        # print("singature_bytes", [b for b in tx_params["signature"]["signature_bytes"]])
        # print("singature_type", tx_params["signature"]["signature_type"])
        # print("sender", tx_params["sender"])

        return self.kwild.broadcast(tx_params)

    def get_database(self, db_id: str) -> Dict[str, Any]:
        db_identifier = generate_dbi(db_id)
        return self.kwild.get_schema(db_identifier)

    def list_database(self) -> List[Dict[str, Any]]:
        return self.kwild.list_database(self.wallet.address)

    def drop_database(self, name: str) -> TxReceipt:
        payload_type = TxPayloadType.DROP_DATABASE
        db_identifier = DatasetIdentifier(owner=self.wallet.address, name=name)
        payload = json.dumps(db_identifier)
        tx_params = self._create_tx(payload_type, payload.encode())
        return self.kwild.broadcast(tx_params)

    def execute_action(self, db_id: str, action: str, inputs: List[Dict[str, Any]]) -> TxReceipt:
        encoded_inputs = encode_action_args(inputs)
        exec_body = ActionExecution(action=action,
                                    dbID=DBIdentifier(db_id),
                                    params=encoded_inputs)
        payload_type = TxPayloadType.EXECUTE_ACTION
        payload = json.dumps(exec_body).encode()
        tx_params = self._create_tx(payload_type, payload)
        return self.kwild.broadcast(tx_params)
