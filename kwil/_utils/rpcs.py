from kwil.types import RPCEndpoint


class GRPC:
    kwil_getSchema = RPCEndpoint("kwil_getSchema")
    kwil_getConfig = RPCEndpoint("kwil_getConfig")
    kwil_getAccount = RPCEndpoint("kwil_getAccount")
    kwil_listDatabase = RPCEndpoint("kwil_listDatabase")
    kwil_ping = RPCEndpoint("kwil_ping")
    kwil_getBlock = RPCEndpoint("kwil_getBlock")
    kwil_broadcast = RPCEndpoint("kwil_broadcast")
    kwil_estimatePrice = RPCEndpoint("kwil_estimatePrice")
    kwil_query = RPCEndpoint("kwil_query")
