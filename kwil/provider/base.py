import logging
from typing import Callable, Any, Dict, Tuple

from google.protobuf.json_format import MessageToDict
from google.protobuf import message as _message

from kwil.types import RPCEndpoint, RPCResponse, Middleware
from kwil._utils.rpcs import GRPC


class BaseProvider:
    """Handling middlewares"""

    _middlewares: Tuple[Middleware, ...] = ()
    # cache by middlewares, (all_middlewares, request_func)
    _request_func_cache: Tuple[Tuple[Middleware, ...], Callable[..., RPCResponse]] = (
        None,
        None,
    )

    @property
    def middlewares(self) -> Tuple[Middleware, ...]:
        return self._middlewares

    @middlewares.setter
    def middlewares(self, middlewares: Tuple[Middleware, ...]) -> None:
        self._middlewares = middlewares

    def request_func(
        self,
        # middlewares: List[Middleware]
    ) -> Callable[..., RPCResponse]:
        # all_middlewares: Tuple[Middleware] = tuple(middlewares) +
        #   tuple(self.middlewares)
        # cache_key = self._request_func_cache[0]
        # if cache_key is None or cache_key != all_middlewares:
        #     self._request_func_cache = (
        #         all_middlewares,
        #         combine_middlewares(all_middlewares, self.make_request))
        # return self._request_func_cache[1]
        return self.make_request

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Provider must implement this method")

    def is_connected(self) -> bool:
        raise NotImplementedError("Provider must implement this method")


class ProtoBaseProvider(BaseProvider):
    """Handling serialization"""

    def __str__(self) -> None:
        pass

    def encode_rpc_request(self, method, params) -> bytes:
        # encode here
        pass

    def decode_rpc_request(self, raw_response: _message) -> Dict[Any, Any]:
        return MessageToDict(
            raw_response,
            # descriptor_pool=_descriptor_pool.Default(),
            including_default_value_fields=True,
        )

    def is_connected(self) -> bool:
        try:
            response = self.make_request(GRPC.kwil_ping, "")
        except Exception as ex:
            logging.exception("caught error", ex)
            return False

        assert "error" not in response
        return True
