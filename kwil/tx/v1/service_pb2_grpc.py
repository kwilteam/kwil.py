# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from kwil.tx.v1 import account_pb2 as kwil_dot_tx_dot_v1_dot_account__pb2
from kwil.tx.v1 import broadcast_pb2 as kwil_dot_tx_dot_v1_dot_broadcast__pb2
from kwil.tx.v1 import config_pb2 as kwil_dot_tx_dot_v1_dot_config__pb2
from kwil.tx.v1 import dataset_pb2 as kwil_dot_tx_dot_v1_dot_dataset__pb2
from kwil.tx.v1 import list_pb2 as kwil_dot_tx_dot_v1_dot_list__pb2
from kwil.tx.v1 import ping_pb2 as kwil_dot_tx_dot_v1_dot_ping__pb2
from kwil.tx.v1 import price_pb2 as kwil_dot_tx_dot_v1_dot_price__pb2
from kwil.tx.v1 import query_pb2 as kwil_dot_tx_dot_v1_dot_query__pb2


class TxServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Broadcast = channel.unary_unary(
                '/tx.TxService/Broadcast',
                request_serializer=kwil_dot_tx_dot_v1_dot_broadcast__pb2.BroadcastRequest.SerializeToString,
                response_deserializer=kwil_dot_tx_dot_v1_dot_broadcast__pb2.BroadcastResponse.FromString,
                )
        self.EstimatePrice = channel.unary_unary(
                '/tx.TxService/EstimatePrice',
                request_serializer=kwil_dot_tx_dot_v1_dot_price__pb2.EstimatePriceRequest.SerializeToString,
                response_deserializer=kwil_dot_tx_dot_v1_dot_price__pb2.EstimatePriceResponse.FromString,
                )
        self.Query = channel.unary_unary(
                '/tx.TxService/Query',
                request_serializer=kwil_dot_tx_dot_v1_dot_query__pb2.QueryRequest.SerializeToString,
                response_deserializer=kwil_dot_tx_dot_v1_dot_query__pb2.QueryResponse.FromString,
                )
        self.GetAccount = channel.unary_unary(
                '/tx.TxService/GetAccount',
                request_serializer=kwil_dot_tx_dot_v1_dot_account__pb2.GetAccountRequest.SerializeToString,
                response_deserializer=kwil_dot_tx_dot_v1_dot_account__pb2.GetAccountResponse.FromString,
                )
        self.Ping = channel.unary_unary(
                '/tx.TxService/Ping',
                request_serializer=kwil_dot_tx_dot_v1_dot_ping__pb2.PingRequest.SerializeToString,
                response_deserializer=kwil_dot_tx_dot_v1_dot_ping__pb2.PingResponse.FromString,
                )
        self.GetConfig = channel.unary_unary(
                '/tx.TxService/GetConfig',
                request_serializer=kwil_dot_tx_dot_v1_dot_config__pb2.GetConfigRequest.SerializeToString,
                response_deserializer=kwil_dot_tx_dot_v1_dot_config__pb2.GetConfigResponse.FromString,
                )
        self.ListDatabases = channel.unary_unary(
                '/tx.TxService/ListDatabases',
                request_serializer=kwil_dot_tx_dot_v1_dot_list__pb2.ListDatabasesRequest.SerializeToString,
                response_deserializer=kwil_dot_tx_dot_v1_dot_list__pb2.ListDatabasesResponse.FromString,
                )
        self.GetSchema = channel.unary_unary(
                '/tx.TxService/GetSchema',
                request_serializer=kwil_dot_tx_dot_v1_dot_dataset__pb2.GetSchemaRequest.SerializeToString,
                response_deserializer=kwil_dot_tx_dot_v1_dot_dataset__pb2.GetSchemaResponse.FromString,
                )


class TxServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Broadcast(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimatePrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDatabases(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSchema(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TxServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Broadcast': grpc.unary_unary_rpc_method_handler(
                    servicer.Broadcast,
                    request_deserializer=kwil_dot_tx_dot_v1_dot_broadcast__pb2.BroadcastRequest.FromString,
                    response_serializer=kwil_dot_tx_dot_v1_dot_broadcast__pb2.BroadcastResponse.SerializeToString,
            ),
            'EstimatePrice': grpc.unary_unary_rpc_method_handler(
                    servicer.EstimatePrice,
                    request_deserializer=kwil_dot_tx_dot_v1_dot_price__pb2.EstimatePriceRequest.FromString,
                    response_serializer=kwil_dot_tx_dot_v1_dot_price__pb2.EstimatePriceResponse.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=kwil_dot_tx_dot_v1_dot_query__pb2.QueryRequest.FromString,
                    response_serializer=kwil_dot_tx_dot_v1_dot_query__pb2.QueryResponse.SerializeToString,
            ),
            'GetAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccount,
                    request_deserializer=kwil_dot_tx_dot_v1_dot_account__pb2.GetAccountRequest.FromString,
                    response_serializer=kwil_dot_tx_dot_v1_dot_account__pb2.GetAccountResponse.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=kwil_dot_tx_dot_v1_dot_ping__pb2.PingRequest.FromString,
                    response_serializer=kwil_dot_tx_dot_v1_dot_ping__pb2.PingResponse.SerializeToString,
            ),
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=kwil_dot_tx_dot_v1_dot_config__pb2.GetConfigRequest.FromString,
                    response_serializer=kwil_dot_tx_dot_v1_dot_config__pb2.GetConfigResponse.SerializeToString,
            ),
            'ListDatabases': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDatabases,
                    request_deserializer=kwil_dot_tx_dot_v1_dot_list__pb2.ListDatabasesRequest.FromString,
                    response_serializer=kwil_dot_tx_dot_v1_dot_list__pb2.ListDatabasesResponse.SerializeToString,
            ),
            'GetSchema': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSchema,
                    request_deserializer=kwil_dot_tx_dot_v1_dot_dataset__pb2.GetSchemaRequest.FromString,
                    response_serializer=kwil_dot_tx_dot_v1_dot_dataset__pb2.GetSchemaResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tx.TxService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TxService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Broadcast(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tx.TxService/Broadcast',
            kwil_dot_tx_dot_v1_dot_broadcast__pb2.BroadcastRequest.SerializeToString,
            kwil_dot_tx_dot_v1_dot_broadcast__pb2.BroadcastResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimatePrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tx.TxService/EstimatePrice',
            kwil_dot_tx_dot_v1_dot_price__pb2.EstimatePriceRequest.SerializeToString,
            kwil_dot_tx_dot_v1_dot_price__pb2.EstimatePriceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tx.TxService/Query',
            kwil_dot_tx_dot_v1_dot_query__pb2.QueryRequest.SerializeToString,
            kwil_dot_tx_dot_v1_dot_query__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tx.TxService/GetAccount',
            kwil_dot_tx_dot_v1_dot_account__pb2.GetAccountRequest.SerializeToString,
            kwil_dot_tx_dot_v1_dot_account__pb2.GetAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tx.TxService/Ping',
            kwil_dot_tx_dot_v1_dot_ping__pb2.PingRequest.SerializeToString,
            kwil_dot_tx_dot_v1_dot_ping__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tx.TxService/GetConfig',
            kwil_dot_tx_dot_v1_dot_config__pb2.GetConfigRequest.SerializeToString,
            kwil_dot_tx_dot_v1_dot_config__pb2.GetConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDatabases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tx.TxService/ListDatabases',
            kwil_dot_tx_dot_v1_dot_list__pb2.ListDatabasesRequest.SerializeToString,
            kwil_dot_tx_dot_v1_dot_list__pb2.ListDatabasesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSchema(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tx.TxService/GetSchema',
            kwil_dot_tx_dot_v1_dot_dataset__pb2.GetSchemaRequest.SerializeToString,
            kwil_dot_tx_dot_v1_dot_dataset__pb2.GetSchemaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
