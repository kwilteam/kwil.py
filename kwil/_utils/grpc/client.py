import grpc

from kwil.types import TxParams, DBIdentifier, HexAddress
from kwil.tx.v1 import (
    ping_pb2,
    query_pb2,
    broadcast_pb2,
    account_pb2,
    config_pb2,
    price_pb2,
    dataset_pb2,
    tx_pb2,
    list_pb2,
    service_pb2_grpc
)

# timeout in seconds
READY_TIMEOUT = 3
REQUEST_TIMEOUT = 2


class Client:
    def __init__(
        self,
        endpoint: str,
        ready_timeout: int = READY_TIMEOUT,
        request_timeout: int = REQUEST_TIMEOUT,
    ):
        self.ready_timeout = ready_timeout
        self.request_timeout = request_timeout
        self.channel = grpc.insecure_channel(endpoint)
        grpc.channel_ready_future(self.channel).result(timeout=self.ready_timeout)
        self.tx_stub = service_pb2_grpc.TxServiceStub(self.channel)

    def close(self):
        self.channel.close()

    def ping(self) -> ping_pb2.PingResponse:
        req = ping_pb2.PingRequest(message="ping")
        return self.tx_stub.Ping(req, timeout=self.request_timeout)

    def query(self, db_id: DBIdentifier, query: str) -> query_pb2.QueryResponse:
        req = query_pb2.QueryRequest(dbid=db_id, query=query)
        return self.tx_stub.Query(req, timeout=self.request_timeout)

    def broadcast(self, tx: TxParams) -> broadcast_pb2.BroadcastResponse:
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
        return self.tx_stub.Broadcast(req, timeout=self.request_timeout)

    def estimate_price(self, tx: TxParams) -> price_pb2.EstimatePriceResponse:
        gtx = tx_pb2.Tx(
            nonce=tx.get("nonce"),
            fee=tx.get("fee"),
            payload_type=tx.get("payloadType"),
            payload=tx.get("payload"),
        )

        req = price_pb2.EstimatePriceRequest(tx=gtx)
        return self.tx_stub.EstimatePrice(req, timeout=self.request_timeout)

    def get_config(self) -> config_pb2.GetConfigResponse:
        req = config_pb2.GetConfigRequest()
        return self.tx_stub.GetConfig(req, timeout=self.request_timeout)

    def get_account(self, address: HexAddress) -> account_pb2.GetAccountResponse:
        req = account_pb2.GetAccountRequest(address=address)
        return self.tx_stub.GetAccount(req, timeout=self.request_timeout)

    def get_schema(self, db_id: DBIdentifier) -> dataset_pb2.GetSchemaResponse:
        req = dataset_pb2.GetSchemaRequest(dbid=db_id)
        return self.tx_stub.GetSchema(req, timeout=self.request_timeout)

    def list_database(self, owner: HexAddress) -> list_pb2.ListDatabasesResponse:
        req = list_pb2.ListDatabasesRequest(owner=owner)
        return self.tx_stub.ListDatabases(req, timeout=self.request_timeout)
