import logging
from typing import Callable, Tuple, Any, Dict

from google.protobuf.json_format import MessageToDict
from google.protobuf import message as _message
import google.protobuf.descriptor_pool as _descriptor_pool

from kwil.types import RPCEndpoint, RPCResponse
from kwil._utils.rpcs import GRPC


class BaseProvider:
    """Handling middlewares"""

    def request_func(self) -> Callable[..., RPCResponse]:
        # apply all middlewares to the request
        return self.make_request

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Provider must implement this method")

    def is_connected(self) -> bool:
        raise NotImplementedError("Provider must implement this method")


class ProtoBaseProvider(BaseProvider):
    """Handling serialization"""

    def __str__(self) -> None:
        pass

    # @staticmethod
    # def apply_validators(method, params) -> None:
    #     # apply validators here
    #     if method not in request_validators:
    #         raise KeyError("Method {0} not found in request validators".format(method))
    #     request_validators[method](params)

    def encode_rpc_request(self, method, params) -> bytes:
        # encode here
        pass

    def decode_rpc_request(self, raw_response: _message) -> Dict[Any, Any]:
        return MessageToDict(raw_response,
                             # descriptor_pool=_descriptor_pool.Default(),
                             including_default_value_fields=True,
                             )

    def is_connected(self) -> bool:
        try:
            response = self.make_request(GRPC.kwil_ping, "")
        except Exception as ex:
            logging.exception("caught error", ex)
            return False

        assert 'error' not in response
        return True
