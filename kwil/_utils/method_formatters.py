import base64
import json
from typing import Dict, Any, Callable, List

from toolz import curry, compose, identity

from kwil.types import RPCEndpoint
from kwil._utils.rpcs import RPC
from kwil._utils.validation import request_validators


def get_request_formatters(method_name: RPCEndpoint) -> Callable[..., Any]:
    formatter_maps = (request_validators,)

    return compose(*[fm[method_name] for fm in formatter_maps if method_name in fm])


@curry
def extract_result(key: Any, response: Dict[str, Any]) -> Any:
    return response[key]


def to_bool_if_message_match(message) -> Callable[..., bool]:
    def if_match(response: Any) -> bool:
        return response.message == message

    return if_match


def ping_response_formatter(response: Dict[Any, Any]) -> str:
    return response.get("message", "shoot")


def tx_receipt_decode(response: Dict[str, Any]) -> Dict[str, Any]:
    response = response["receipt"]
    body = response["body"]
    del response["body"]
    # TODO: make server return a standard response, not ""
    if body == "":
        response["result"] = {}
        return response
    result = json.loads(base64.b64decode(body))
    response["result"] = result
    return response


def query_decode(response: Dict[str, Any]) -> Dict[str, Any]:
    if response["result"] == "":
        response["result"] = {}
        return response

    base64_response = response["result"]
    result = json.loads(base64.b64decode(base64_response))
    response["result"] = result
    return response


response_formatters: Dict[str, Callable[[Any], Any]] = {
    RPC.kwil_ping: ping_response_formatter,
    RPC.kwil_getSchema: extract_result("dataset"),
    RPC.kwil_getConfig: identity,
    RPC.kwil_getAccount: extract_result("account"),
    RPC.kwil_estimatePrice: extract_result("price"),
    RPC.kwil_broadcast: tx_receipt_decode,
    RPC.kwil_listDatabases: extract_result("databases"),
    RPC.kwil_query: query_decode,
    RPC.kwil_call: query_decode,
}


def get_response_formatters(
    method_name: RPCEndpoint, module: "Module"  # noqa: F821
) -> Callable[..., Any]:
    formatter_maps = (response_formatters,)

    return compose(
        *[
            formatter_map[method_name]
            for formatter_map in formatter_maps
            if method_name in formatter_map
        ]
    )
