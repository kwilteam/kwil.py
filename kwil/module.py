import logging
from typing import Callable, Any

from toolz import curry, pipe

from kwil.method import Method
from kwil.types import RPCEndpoint, TReturn

logger = logging.getLogger(__name__)


@curry
def _apply_result_formatters(
    method: RPCEndpoint, result_formatters: Callable[..., TReturn], result: Any
) -> Any:
    if result_formatters:
        logger.debug("apply result formatter to '%s'", method)
        formatted_result = pipe(result, result_formatters)
        return formatted_result
    else:
        return result


class Module:
    @curry
    def caller_fn(
        self, kwil: "Kwil", method: Method[Callable[..., Any]]
    ) -> Callable[..., Any]:
        def caller(*args: Any) -> Any:
            (method_str, args), response_formatters = method.process_params(self, *args)
            result = kwil.manager.request_blocking(method_str, args)
            return _apply_result_formatters(
                method.rpc_method, response_formatters, result
            )

        return caller
