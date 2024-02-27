import logging
from typing import Any, Optional

from kwil.types import RPCResponse
from kwil.provider import BaseProvider, AutoProvider
from kwil.exceptions import BadResponseFormat


class RequestManager:
    """
    The RequestManager class handles making requests to a provider and
    processing the responses.

    Attributes:
        logger (logging.Logger): The logger instance.

    Args:
        kwil (Kwil): The Kwil instance.
        provider (Optional[BaseProvider]): The provider to use for making requests.
            If not provided, an AutoProvider will be used.

    Properties:
        provider (BaseProvider): The provider used for making requests.

    Methods:
        formatted_response: Formats the response received from the provider.
        request_blocking: Makes a blocking request to the provider.
    """

    logger = logging.getLogger("kwil.RequestManager")

    def __init__(
        self,
        kwil: "Kwil",  # noqa: F821
        provider: Optional[BaseProvider] = None,
        # middlewares: Optional[List[Tuple[str, Middleware]]] = None,
    ):
        """
        Initializes the RequestManager instance.

        Args:
            kwil (Kwil): The Kwil instance.
            provider (Optional[BaseProvider]): The provider to use for making
                requests. If not provided, an AutoProvider will be used.
        """
        self.kwil = kwil

        if provider is None:
            self.provider = AutoProvider()
        else:
            self.provider = provider

        # if middlewares is None:
        #     self.middlewares = self.default_middlewares()

    @property
    def provider(self) -> BaseProvider:
        """
        Get the provider used for making requests.

        Returns:
            BaseProvider: The provider used for making requests.
        """
        return self._provider

    @provider.setter
    def provider(self, provider: BaseProvider) -> None:
        """
        Set the provider used for making requests.

        Args:
            provider (BaseProvider): The provider to use for making requests.
        """
        self._provider = provider

    # @staticmethod
    # def default_middlewares() -> List[Tuple[Middleware]]:
    #     return ()

    def _make_request(self, method, params: Any) -> RPCResponse:
        """
        Make a request to the provider.

        Args:
            method: The method to call.
            params (Any): The parameters for the method.

        Returns:
            RPCResponse: The response received from the provider.
        """
        # request_func = self.provider.request_func(self.middlewares)
        request_func = self.provider.request_func()
        self.logger.debug("request %s", method)
        return request_func(method, params)

    @staticmethod
    def formatted_response(response: RPCResponse) -> Any:
        """
        Format the response received from the provider.

        Args:
            response (RPCResponse): The response received from the provider.

        Returns:
            Any: The formatted response.

        Raises:
            ValueError: If the response contains an error.
            BadResponseFormat: If the response format is invalid.
        """
        if "error" in response:
            raise ValueError(response["error"])
        elif response.get("result") is not None:
            return response["result"]
        else:
            raise BadResponseFormat("Bad response: {0}".format(response))

    def request_blocking(self, method, params: Any) -> Any:
        """
        Make a blocking request to the provider.

        Args:
            method: The method to call.
            params (Any): The parameters for the method.

        Returns:
            Any: The formatted response received from the provider.
        """
        resp = self._make_request(method, params)
        return self.formatted_response(resp)
