import json
import os
from typing import Optional, Dict, Any, List, cast

from toolz import pipe
from eth_account.signers.local import LocalAccount

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
from kwil._utils.action import encode_action_inputs
from kwil._utils.dataset import generate_dbi
from kwil._utils.signing import load_wallet


class BaseKwil:

    @property
    def api(self) -> str:
        from kwil import __version__
        return __version__

    @classmethod
    def generate_dbi(cls, owner: str, db_name: str) -> DBIdentifier:
        return generate_dbi(owner, db_name)


class Kwil(BaseKwil):

    RequestManager = DefaultRequestManager

    kwild: Kwild
    web3: None

    def __init__(
            self,
            provider: Optional[BaseProvider] = None,
            wallet: Optional[LocalAccount] = None,
            ):
        self.manager = self.RequestManager(self, provider)

        self.kwild = Kwild(self)

        if wallet is None:
            self._wallet = load_wallet(os.getenv("KWIL_ETH_PRIVATE_KEY"))
        else:
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
        encoded_inputs = encode_action_inputs(inputs)
        exec_body = ActionExecution(action=action,
                                    dbID=DBIdentifier(db_id),
                                    params=encoded_inputs)
        payload_type = TxPayloadType.EXECUTE_ACTION
        payload = json.dumps(exec_body).encode()
        tx_params = self._create_tx(payload_type, payload)
        return self.kwild.broadcast(tx_params)
