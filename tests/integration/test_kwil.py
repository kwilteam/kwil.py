import json
import os
import logging
from unittest import TestCase

from eth_account import Account
from dotenv.main import load_dotenv

from kwil.main import Kwil, generate_dbi
from kwil.provider import GRPCProvider
from kwil.types import DBSchema, TxPayloadType, TxParams, Nonce


class TestSdk(TestCase):
    def setUp(self):
        logging.basicConfig(level=os.getenv("LOG_LEVEL", "DEBUG"))
        load_dotenv()
        host = os.getenv("NODE_HOST")
        port = os.getenv("NODE_PORT")
        private_key = os.getenv("PRIVATE_KEY")
        provider = GRPCProvider(f"{host}:{port}", None)
        account = Account.from_key(private_key)
        self.k = Kwil(provider, account)

    def tearDown(self) -> None:
        pass

    def test_ping(self):
        msg = self.k.kwild.ping()
        self.assertEqual(msg, "pong", "expect 'pong'")

    def test_getConfig(self):
        cfg = self.k.kwild.get_config()
        assert "chain_code" in cfg, "expect 'chain_code' in config"
        assert "provider_address" in cfg, "expect 'provider_address' in config"
        assert "pool_address" in cfg, "expect 'pool_address' in config"

    def test_estimatePrice(self):
        json_file_name = "test_data/table_with_action_insert.golden"
        with open(json_file_name, "r") as f:
            db_schema_str = f.read()
            tx_params = TxParams(
                payloadType=TxPayloadType.DEPLOY_DATABASE,
                payload=db_schema_str.encode(),
                nonce=Nonce(1),
            )
            price = self.k.kwild.estimate_price(tx_params)
            assert price is not None, "expect price is not None"

    def test_getAccount(self):
        account_info = self.k.kwild.get_account(self.k.wallet.address)
        assert "nonce" in account_info, "expect 'nonce' in account_info"
        assert "balance" in account_info, "expect 'balance' in account_info"
        assert "address" in account_info, "expect 'address' in account_info"

    def test_deploy_database(self):
        json_file_name = "test_data/table_with_action_insert.golden"
        with open(json_file_name, "r") as f:
            db_schema_str = f.read()
            tx_hash = self.k.deploy_database(db_schema_str.encode())

    def test_get_schema(self):
        db_name = "testdb"
        db_identifier = generate_dbi(self.k.wallet.address, db_name)
        db_schema: DBSchema = self.k.kwild.get_schema(db_identifier)
        assert db_schema is not None, "expect db_schema is not None"

    def test_drop_database(self):
        tx_receipt = self.k.drop_database("test_demo")
        assert tx_receipt is not None, "expect tx_receipt is not None"

    def test_insert_action(self):
        db_name = "testdb"
        db_identifier = generate_dbi(self.k.wallet.address, db_name)
        args = [
            {"$id": 1,
             "$username": "aha",
             "$age": 18,},
        ]
        tx_receipt = self.k.execute_action(db_identifier, "create_user", args)
        assert tx_receipt is not None, "expect tx_receipt is not None"

    def test_query_action(self):
        db_name = "testdb"
        db_identifier = generate_dbi(self.k.wallet.address, db_name)
        tx_receipt = self.k.execute_action(db_identifier, "list_users", [])
        assert tx_receipt is not None, "expect tx_receipt is not None"
        resp = tx_receipt["body"]
        assert len(resp) > 0, "expect len(resp) > 0"
        resp = resp[0][0]
        assert resp["wallet"] == self.k.wallet.address, "expect resp['wallet'] == self.k.wallet.address"

    def test_list_database(self):
        db_list = self.k.list_database()
        assert len(db_list) > 0, "expect len(db_list) > 0"
