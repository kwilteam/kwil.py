import json
import hashlib
import os
from typing import Optional, Dict, Any, List, cast

from eth_account.signers.local import LocalAccount

from kwil.exceptions import WalletNotSet
from kwil.kwild import Kwild
from kwil.provider import BaseProvider, GRPCProvider
from kwil.manager import RequestManager as DefaultRequestManager
from kwil.types import (
    TxPayloadType,
    TxParam,
    Nonce,
    TxReceipt,
    DatasetIdentifier,
    DBIdentifier,
    ExecuteActionPayload,
    CallActionPayload,
    CallParam,
    ActionArg,
)
from kwil._utils.transaction import sign_tx
from kwil._utils.dataset import generate_dbi
from kwil._utils.signing import load_wallet
from kwil._utils.action import sign_call_action


class BaseKwil:
    GRPCProvider = GRPCProvider
    RequestManager = DefaultRequestManager

    kwild: Kwild
    web3: None

    @property
    def api(self) -> str:
        from kwil import __version__

        return __version__

    @classmethod
    def generate_dbi(cls, owner: str, db_name: str) -> DBIdentifier:
        return generate_dbi(owner, db_name)

    @classmethod
    def load_wallet(cls, private_key: str) -> LocalAccount:
        return load_wallet(private_key)


class Kwil(BaseKwil):
    """
    Kwil expose .
    """

    def __init__(
            self,
            provider: Optional[BaseProvider] = None,
            wallet: Optional[LocalAccount] = None,
    ):
        self.manager = self.RequestManager(self, provider)
        self.kwild = Kwild(self)

        if wallet:
            self._wallet = wallet

    @property
    def kwil_provider(self) -> BaseProvider:
        return cast(BaseProvider, self.manager.provider)

    @kwil_provider.setter
    def kwil_provider(self, provider: BaseProvider) -> None:
        self.manager.provider = provider

    @property
    def wallet(self) -> LocalAccount:
        return self._wallet

    @wallet.setter
    def wallet(self, wallet: LocalAccount) -> None:
        self._wallet = wallet

    def is_connected(self) -> bool:
        return self.kwil_provider.is_connected()

    def _create_tx(self, payload_type: TxPayloadType, payload: bytes) -> TxParam:
        account_info = self.kwild.get_account(self.wallet.address)

        tx_params = TxParam(
            payload_type=payload_type,
            payload=payload,
            sender=self.wallet.address,
            fee="0",
            # SHOULD be done in result formatter
            nonce=Nonce(int(account_info["nonce"]) + 1),
        )

        price = self.kwild.estimate_price(tx_params)
        tx_params["fee"] = price
        tx_params = sign_tx(tx_params, self.wallet)
        return tx_params

    def deploy_database(self, payload: bytes) -> TxReceipt:
        # populate owner
        schema = json.loads(payload)
        schema["owner"] = self.wallet.address
        payload = json.dumps(schema).encode("utf-8")

        payload_type = TxPayloadType.DEPLOY_DATABASE
        tx_params = self._create_tx(payload_type, payload)
        return self.kwild.broadcast(tx_params)

    def get_schema(self, db_id: DBIdentifier) -> Dict[str, Any]:
        return self.kwild.get_schema(db_id)

    def list_databases(self, address: Optional[str] = None) -> List[Dict[str, Any]]:
        if address is None:
            address = self.wallet.address
        return self.kwild.list_databases(address)

    def drop_database(self, name: str) -> TxReceipt:
        payload_type = TxPayloadType.DROP_DATABASE
        db_identifier = DatasetIdentifier(owner=self.wallet.address, name=name)
        payload = json.dumps(db_identifier)
        tx_params = self._create_tx(payload_type, payload.encode())
        return self.kwild.broadcast(tx_params)

    def execute_action(
            self,
            db_id: DBIdentifier,
            action_name: str,
            params: List[Dict[str, Any]],
    ) -> TxReceipt:
        """
        Execute an action on a database to change state, will send request as transaction.
        """
        exec_body = ExecuteActionPayload(
            action=action_name, dbid=db_id, params=params
        )
        payload_type = TxPayloadType.EXECUTE_ACTION
        payload = json.dumps(exec_body).encode()
        tx_params = self._create_tx(payload_type, payload)
        return self.kwild.broadcast(tx_params)

    def query(self, db_id: DBIdentifier, query: str) -> TxReceipt:
        return self.kwild.query(db_id, query)

    def call_action(
            self,
            db_id: DBIdentifier,
            action_name: str,
            args: Dict[str, ActionArg],
    ) -> TxReceipt:
        """
        Call an read-only action on a database, the request will need to be signed in some cases,
        for example, a `mustsign` `view` action.
        """

        payload = CallActionPayload(
                action=action_name,
                dbid=db_id,
                args=args)

        call_param = sign_call_action(payload, self.wallet)
        return self.kwild.call(call_param)
