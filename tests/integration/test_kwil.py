import pytest

from kwil.main import generate_dbi
from kwil.types import TxPayloadType, TxParams, Nonce

interactive = True


@pytest.mark.integration
class TestKwilBehavior:
    def test_ping(self, client):
        msg = client.kwild.ping()
        assert msg == "pong", "expect 'pong'"

    def test_getConfig(self, client):
        cfg = client.kwild.get_config()
        assert "chain_code" in cfg, "expect 'chain_code' in config"
        assert "provider_address" in cfg, "expect 'provider_address' in config"
        assert "pool_address" in cfg, "expect 'pool_address' in config"

    def test_estimatePrice(self, client, schema_file):
        with open(schema_file, "r") as f:
            db_schema_str = f.read()
            tx_params = TxParams(
                payloadType=TxPayloadType.DEPLOY_DATABASE,
                payload=db_schema_str.encode("utf-8"),
                nonce=Nonce(1),
            )
            price = client.kwild.estimate_price(tx_params)
            assert price is not None, "expect price is not None"

    def test_getAccount(self, client):
        account_info = client.kwild.get_account(client.wallet.address)
        assert "nonce" in account_info, "expect 'nonce' in account_info"
        assert "balance" in account_info, "expect 'balance' in account_info"
        assert "address" in account_info, "expect 'address' in account_info"

    def _test_deployDatabase(self, client, schema_file):
        with open(schema_file, "r") as f:
            db_schema_str = f.read()
            tx_receipt = client.deploy_database(db_schema_str.encode("utf-8"))
            assert tx_receipt is not None, "expect tx_receipt is not None"
            assert "txHash" in tx_receipt, "expect 'txHash' in tx_receipt"
            assert "fee" in tx_receipt, "expect 'fee' in tx_receipt"
            assert "result" in tx_receipt, "expect 'result' in tx_receipt"

    def _test_dropDatabase(self, client):
        tx_receipt = client.drop_database("testdb")
        assert tx_receipt is not None, "expect tx_receipt is not None"
        assert "txHash" in tx_receipt, "expect 'txHash' in tx_receipt"
        assert "fee" in tx_receipt, "expect 'fee' in tx_receipt"
        assert "result" in tx_receipt, "expect 'result' in tx_receipt"

    def _test_getSchema(self, client):
        db_name = "testdb"
        db_identifier = generate_dbi(client.wallet.address, db_name)
        db_schema = client.kwild.get_schema(db_identifier)
        assert db_schema is not None, "expect db_schema is not None"
        assert db_schema["owner"] == client.wallet.address, "expect db_schema['owner'] == client.wallet.address"
        assert db_schema["name"] == db_name, "expect db_schema['name'] == db_name"

    def _test_execute_insert_action(self, client):
        db_name = "testdb"
        db_identifier = generate_dbi(client.wallet.address, db_name)
        args = [
            {"$id": 1,
             "$username": "aha",
             "$age": 18},
        ]
        tx_receipt = client.execute_action(db_identifier, "create_user", args)
        assert tx_receipt is not None, "expect tx_receipt is not None"

    def _test_execute_query_action(self, client):
        db_name = "testdb"
        db_identifier = generate_dbi(client.wallet.address, db_name)
        tx_receipt = client.execute_action(db_identifier, "list_users", [])
        assert tx_receipt is not None, "expect tx_receipt is not None"
        resp = tx_receipt["result"]
        assert len(resp) > 0, "expect len(resp) > 0"
        resp = resp[0][0]
        assert resp["wallet"] == client.wallet.address, f"expect resp['wallet'] == {client.wallet.address}"
        assert resp["username"] == "aha", "expect resp['name'] == 'aha'"
        assert resp["age"] == 18, "expect resp['age'] == 18"

    def _test_listDatabase(self, client, count: int):
        db_list = client.list_database()
        assert len(db_list) == count, f"expect len(db_list) == {count}"

    def _test_query(self, client, count: int):
        query = "select * from users"
        db_name = "testdb"
        db_identifier = generate_dbi(client.wallet.address, db_name)
        tx_receipt = client.kwild.query(db_identifier, query)
        resp = tx_receipt["result"]
        assert tx_receipt is not None, "expect tx_receipt is not None"
        assert len(resp) == count, f"expect len(resp) == {count}"
    def test_kwil_behavior(self, client, schema_file):
        self._test_deployDatabase(client, schema_file)
        self._test_getSchema(client)
        self._test_listDatabase(client, 1)
        self._test_execute_insert_action(client)
        self._test_execute_query_action(client)
        self._test_query(client, 1)
        self._test_dropDatabase(client)
        self._test_listDatabase(client, 0)

    @pytest.mark.skipif(interactive, reason="interactive mode")
    def test_deployDatabase(self, client, schema_file):
        self._test_deployDatabase(client, schema_file)

    @pytest.mark.skipif(interactive, reason="interactive mode")
    def test_dropDatabase(self, client):
        self._test_dropDatabase(client)

    @pytest.mark.skipif(interactive, reason="interactive mode")
    def test_getSchema(self, client):
        self._test_getSchema(client)

    @pytest.mark.skipif(interactive, reason="interactive mode")
    def test_execute_insert_action(self, client):
        self._test_execute_insert_action(client)

    @pytest.mark.skipif(interactive, reason="interactive mode")
    def test_execute_query_action(self, client):
        self._test_execute_query_action(client)

    @pytest.mark.skipif(interactive, reason="interactive mode")
    def test_listDatabase(self, client):
        self._test_listDatabase(client, 1)

    @pytest.mark.skipif(interactive, reason="interactive mode")
    def test_query(self, client):
        self._test_query(client, 1)