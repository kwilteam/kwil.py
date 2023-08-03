import pytest

from kwil.types import TxPayloadType, TxParam, Nonce

non_interactive = True


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
            tx_params = TxParam(
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

    def _test_dropDatabase(self, db_name, client):
        tx_receipt = client.drop_database(db_name)
        assert tx_receipt is not None, "expect tx_receipt is not None"
        assert "txHash" in tx_receipt, "expect 'txHash' in tx_receipt"
        assert "fee" in tx_receipt, "expect 'fee' in tx_receipt"
        assert "result" in tx_receipt, "expect 'result' in tx_receipt"

    def _test_getSchema(self, db_name, client):
        db_identifier = client.generate_dbi(client.wallet.address, db_name)
        db_schema = client.get_schema(db_identifier)
        assert db_schema is not None, "expect db_schema is not None"
        assert (
            db_schema["owner"].lower() == client.wallet.address.lower()
        ), "expect db_schema['owner'] == client.wallet.address"
        assert db_schema["name"] == db_name, "expect db_schema['name'] == db_name"

    def _test_execute_action(self, db_name, client):
        args = [
            {"$id": 1, "$username": "aha", "$age": 18},
        ]
        db_id = client.generate_dbi(client.wallet.address, db_name)
        tx_receipt = client.execute_action(db_id, "create_user", args)
        assert tx_receipt is not None, "expect tx_receipt is not None"

    def _test_call_action(self, db_name, client):
        db_id = client.generate_dbi(client.wallet.address, db_name)
        resp = client.call_action(db_id, "user_post_count", {"$id": 1})
        resp = resp["result"][0]
        assert resp["count"] == 0, f"expect result.count == 1, got {resp['count']}"

    def _test_call_action_mustsign(self, db_name, client):
        db_id = client.generate_dbi(client.wallet.address, db_name)
        resp = client.call_action(db_id, "view_user_info", {})
        resp = resp["result"][0]
        assert resp["username"] == "aha", "expect resp['name'] == 'aha'"
        assert resp["age"] == 18, "expect resp['age'] == 18"

    def _test_call_action_mustsign_without_sign(self, db_name, client):
        wallet = client.wallet
        client.wallet = None
        with pytest.raises(Exception):
            db_id = client.generate_dbi(client.wallet.address, db_name)
            resp = client.call_action(db_id, "view_user_info", {}, False)

        client.wallet = wallet

    def _test_listDatabase(self, db_name, client, count: int):
        db_list = client.list_databases()
        assert len(db_list) >= count, f"expect len(db_list) >= {count}"
        if count > 0:
            assert db_name in db_list, f"expect {db_name} in db_list"

    def _test_query(self, db_name, client, count: int):
        query = "select * from users"
        db_id = client.generate_dbi(client.wallet.address, db_name)
        tx_receipt = client.query(db_id, query)
        resp = tx_receipt["result"]
        assert tx_receipt is not None, "expect tx_receipt is not None"
        assert len(resp) == count, f"expect len(resp) == {count}"

    def test_kwil_behavior(self, client, schema_file, db_name):
        self._test_deployDatabase(client, schema_file)
        self._test_getSchema(db_name, client)
        self._test_listDatabase(db_name, client, 1)
        self._test_execute_action(db_name, client)
        self._test_call_action(db_name, client)
        self._test_call_action_mustsign(db_name, client)
        self._test_call_action_mustsign_without_sign(db_name, client)
        self._test_query(db_name, client, 1)
        self._test_dropDatabase(db_name, client)
        self._test_listDatabase(db_name, client, 0)

    @pytest.mark.skipif(non_interactive, reason="only interactive mode")
    def test_deployDatabase(self, client, schema_file):
        self._test_deployDatabase(client, schema_file)

    @pytest.mark.skipif(non_interactive, reason="only interactive mode")
    def test_dropDatabase(self, db_name, client):
        self._test_dropDatabase(db_name, client)

    @pytest.mark.skipif(non_interactive, reason="only interactive mode")
    def test_getSchema(self, db_name, client):
        self._test_getSchema(db_name, client)

    @pytest.mark.skipif(non_interactive, reason="only interactive mode")
    def test_execute_action(self, db_name, client):
        self._test_execute_action(db_name, client)

    @pytest.mark.skipif(non_interactive, reason="only interactive mode")
    def test_call_action(self, db_name, client):
        self._test_call_action(db_name, client)

    @pytest.mark.skipif(non_interactive, reason="only interactive mode")
    def test_call_action_mustsign(self, db_name, client):
        self._test_call_action_mustsign(db_name, client)

    @pytest.mark.skipif(non_interactive, reason="only interactive mode")
    def test_call_action_mustsign_without_sign(self, db_name, client):
        self._test_call_action_mustsign_without_sign(db_name, client)

    @pytest.mark.skipif(non_interactive, reason="only interactive mode")
    def test_listDatabase(self, db_name, client):
        self._test_listDatabase(db_name, client, 1)

    @pytest.mark.skipif(non_interactive, reason="only interactive mode")
    def test_query(self, db_name, client):
        self._test_query(db_name, client, 1)
