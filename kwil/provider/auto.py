from typing import Optional, Sequence, Type, Union, Callable, Any

import grpc

from .base import BaseProvider
from .grpc import GRPCProvider
from kwil.types import RPCEndpoint, RPCResponse
from kwil.exceptions import CannotHandleRequest


class AutoProvider(BaseProvider):
    default_providers = (GRPCProvider,)

    _active_provider = None

    def __init__(
        self,
        # either a callable that returns a provider or a provider class
        potential_providers: Optional[
            Sequence[Union[Type[BaseProvider], Callable[..., BaseProvider]]]
        ] = None,
    ) -> None:
        if potential_providers:
            self._potential_providers = potential_providers
        else:
            self._potential_providers = self.default_providers

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        try:
            return self._proxy_request(method, params)
        except grpc.RpcError:
            return self._proxy_request(method, params, use_cache=False)

    def is_connected(self) -> bool:
        provider = self._get_active_provider(use_cache=True)
        return provider is not None and provider.is_connected()

    def _proxy_request(
        self, method: RPCEndpoint, params: Any, use_cache: bool = True
    ) -> RPCResponse:
        provider = self._get_active_provider(use_cache)
        if provider is None:
            raise CannotHandleRequest(
                "Could not discover provider while making request: "
                "method:{0}\n"
                "params:{1}\n".format(method, params)
            )

        return provider.make_request(method, params)

    def _get_active_provider(self, use_cache: bool) -> Optional[BaseProvider]:
        if use_cache and self._active_provider is not None:
            return self._active_provider

        for Provider in self._potential_providers:
            provider = Provider()
            if provider is not None and provider.is_connected():
                self._active_provider = provider
                return provider

        return None
