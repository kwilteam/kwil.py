import logging

import grpc

from kwil.types import (
    TxParams,
    DBIdentifier,
    HexAddress
)
from kwil.tx.v1 import (
    service_pb2_grpc,
    ping_pb2,
    query_pb2,
    broadcast_pb2,
    account_pb2,
    config_pb2,
    price_pb2,
    dataset_pb2,
    tx_pb2,
    list_pb2,
)
from kwil._utils.validation import validate_address, validate_tx_params

_LOGGER = logging.getLogger(__name__)


class Client:
    def __init__(self, endpoint: str):
        self.channel = grpc.insecure_channel(endpoint)
        self.tx = service_pb2_grpc.TxServiceStub(self.channel)

    def close(self):
        self.channel.close()

    def ping(self) -> ping_pb2.PingResponse:
        req = ping_pb2.PingRequest(message="ping")
        resp = self.tx.Ping(req)
        return resp

    def query(self, db_id: DBIdentifier, query: str) -> query_pb2.QueryResponse:
        assert isinstance(query, str), "query must be provided as a string"
        assert isinstance(db_id, str), "db_id must be provided as a string"

        req = query_pb2.QueryRequest(dbid=db_id, query=query)
        resp = self.tx.Query(req)
        return resp

    def broadcast(self, tx: TxParams) -> broadcast_pb2.BroadcastResponse:
        validate_tx_params(tx)

        gtx = tx_pb2.Tx(
            hash=tx.get("hash"),
            nonce=tx.get("nonce"),
            fee=tx.get("fee"),
            payload_type=tx.get("payloadType"),
            payload=tx.get("payload"),
            signature=tx.get("signature"),
            sender=tx.get("sender"),
        )

        req = broadcast_pb2.BroadcastRequest(tx=gtx)
        resp = self.tx.Broadcast(req)
        return resp

    def estimate_price(self, tx: TxParams) -> price_pb2.EstimatePriceResponse:
        validate_tx_params(tx)

        gtx = tx_pb2.Tx(
            nonce=tx.get("nonce"),
            fee=tx.get("fee"),
            payload_type=tx.get("payloadType"),
            payload=tx.get("payload"),
        )

        req = price_pb2.EstimatePriceRequest(tx=gtx)
        resp = self.tx.EstimatePrice(req)
        return resp

    def get_config(self) -> config_pb2.GetConfigResponse:
        req = config_pb2.GetConfigRequest()
        resp = self.tx.GetConfig(req)
        return resp

    def get_account(self, address: HexAddress) -> account_pb2.GetAccountResponse:
        validate_address(address)

        req = account_pb2.GetAccountRequest(address=address)
        resp = self.tx.GetAccount(req)
        return resp

    def get_schema(self, db_id: DBIdentifier) -> dataset_pb2.GetSchemaResponse:
        assert isinstance(db_id, str), "db_id must be provided as a string"

        req = dataset_pb2.GetSchemaRequest(dbid=db_id)
        resp = self.tx.GetSchema(req)
        return resp

    def list_database(self, owner: HexAddress) -> list_pb2.ListDatabasesResponse:
        validate_address(owner)

        req = list_pb2.ListDatabasesRequest(owner=owner)
        resp = self.tx.ListDatabases(req)
        return resp
