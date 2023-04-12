from typing import (
    Callable,
    Sequence,
    Any,
)

import toolz

from kwil.types import RPCResponse, Middleware, RPCEndpoint
from kwil._utils.validation import request_validators


def combine_middlewares(
    middlewares: Sequence[Middleware],
    provider_request_fn: Callable[[RPCEndpoint, Any], Any],
) -> Callable[..., RPCResponse]:
    """
    Returns a callable function which will call the provider_request_fn
    wrapped with all the middlewares.
    Middlewares are applied in reverse order, so the first middleware in
    the list will be the outermost.
    """
    return toolz.reduce(
        lambda request_fn, middleware: middleware(request_fn),
        reversed(middlewares),
        provider_request_fn,
    )


validation_middlewares = request_validators
