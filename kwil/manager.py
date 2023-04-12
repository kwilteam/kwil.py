import logging
from typing import Any, Optional

from kwil.types import RPCResponse
from kwil.provider import BaseProvider, AutoProvider
from kwil.exceptions import BadResponseFormat


class RequestManager:
    logger = logging.getLogger("kwil.RequestManager")

    _provider = None

    def __init__(
        self,
        kwil: "Kwil",
        provider: Optional[BaseProvider] = None,
        # middlewares: Optional[List[Tuple[str, Middleware]]] = None,
    ):
        self.kwil = kwil

        if provider is None:
            self.provider = AutoProvider()
        else:
            self.provider = provider

        # if middlewares is None:
        #     self.middlewares = self.default_middlewares()

    @property
    def provider(self) -> BaseProvider:
        return self._provider

    @provider.setter
    def provider(self, provider: BaseProvider) -> None:
        self._provider = provider

    # @staticmethod
    # def default_middlewares() -> List[Tuple[Middleware]]:
    #     return ()

    def _make_request(self, method, params: Any) -> RPCResponse:
        # request_func = self.provider.request_func(self.middlewares)
        request_func = self.provider.request_func()
        self.logger.debug("request %s", method)
        return request_func(method, params)

    @staticmethod
    def formatted_response(response: RPCResponse) -> Any:
        if "error" in response:
            raise ValueError(response["error"])
        elif response.get("result") is not None:
            return response["result"]
        else:
            raise BadResponseFormat("Bad response: {0}".format(response))

    def request_blocking(self, method, params: Any) -> Any:
        resp = self._make_request(method, params)
        return self.formatted_response(resp)
