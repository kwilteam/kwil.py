from kwil.types import RPCEndpoint


class RPC:
    kwil_broadcast = RPCEndpoint("kwil_broadcast")
    kwil_call = RPCEndpoint("kwil_call")
    kwil_estimatePrice = RPCEndpoint("kwil_estimatePrice")
    kwil_getAccount = RPCEndpoint("kwil_getAccount")
    kwil_getBlock = RPCEndpoint("kwil_getBlock")
    kwil_getConfig = RPCEndpoint("kwil_getConfig")
    kwil_getSchema = RPCEndpoint("kwil_getSchema")
    kwil_listDatabases = RPCEndpoint("kwil_listDatabases")
    kwil_ping = RPCEndpoint("kwil_ping")
    kwil_query = RPCEndpoint("kwil_query")
