import logging
from typing import TypeVar, Callable, Any, Optional, Generic, Type

from toolz import pipe

from kwil.types import RPCEndpoint, TReturn
from kwil._utils.method_formatters import (
    get_request_formatters,
    get_response_formatters,
)


TFunc = TypeVar("TFunc", bound=Callable[..., Any])

logger = logging.getLogger(__name__)


def _apply_request_validator(
    method: RPCEndpoint, params: Any, validators: Callable[..., TReturn]
) -> None:
    if validators:
        logger.debug("apply request validator to '%s'", method)
        pipe(params, validators)


class Method(Generic[TFunc]):
    def __init__(
        self,
        rpc_method: RPCEndpoint,
        request_formatters: Optional[Callable[..., TReturn]] = None,
        response_formatters: Optional[Callable[..., TReturn]] = None,
    ):
        self.rpc_method = rpc_method
        self.request_formatters = request_formatters or get_request_formatters
        self.response_formatters = response_formatters or get_response_formatters

    # as Descriptor
    def __get__(
        self, obj: Optional["Module"] = None, obj_type: Optional[Type["Module"]] = None
    ) -> TFunc:
        if obj is None:
            raise TypeError("Methods must be called on an instance of a Module class")
        return obj.caller_fn(obj.kwil, self)

    def method_selector_fn(self) -> Callable[..., Any]:
        raise NotImplementedError("Must be implemented by subclasses")

    def process_params(self, module: "Module", *args: Any) -> Any:
        # to simplify, kwargs are not supported

        method = self.rpc_method

        response_formatters = self.response_formatters(method, module)

        _apply_request_validator(self.rpc_method, args, self.request_formatters(method))

        return (method, args), response_formatters
