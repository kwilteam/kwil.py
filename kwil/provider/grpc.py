import logging
from typing import Any, Dict, Callable

import grpc

from kwil.types import RPCEndpoint, RPCResponse
from kwil.provider.base import ProtoBaseProvider
from kwil._utils.request import grpc_request


class GRPCProvider(ProtoBaseProvider):
    logger = logging.getLogger("kwil.provider.GRPCProvider")

    endpoint_uri = None
    _request_kwargs = None

    def __init__(self, endpoint_uri, request_kwargs):
        self.endpoint_uri = endpoint_uri

    def __str__(self) -> str:
        return "GRPC connection {0}".format(self.endpoint_uri)

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        # make request here
        self.logger.debug("Making GRPC request. URI: %s, Method: %s",
                          self.endpoint_uri, method)

        try:
            raw_response = grpc_request(self.endpoint_uri, method, params)
        except grpc.RpcError as e:
            self.logger.debug("Call GRPC error. URI: %s, Method: %s, Error: %s",
                              self.endpoint_uri, method, e)
            return RPCResponse(error=e)
        else:
            response = self.decode_rpc_request(raw_response)
            self.logger.debug("Got GRPC response. URI: %s, Method: %s, Response: %s",
                              self.endpoint_uri, method, response)
            return RPCResponse(result=response)
