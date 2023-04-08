import base64
import json
from typing import Dict, Any, Callable, List, Generator

from toolz import curry, compose

from kwil.types import (RPCResponse, RPCEndpoint)
from kwil._utils.rpcs import GRPC
from kwil._utils.validation import validate_address, validate_tx_params, ignore, identity


@curry
def apply_validator_at_index(fn: Callable[..., Any], index: int, value: List[Any]) -> Any:
    if index >= len(value):
        raise IndexError(
            "Not enough values to apply validator. {0}<{1}".format(len(value), index))
    for i, item in enumerate(value):
        if i == index:
            fn(item)


request_validators: Dict[RPCEndpoint, Callable[..., Any]] = {
    GRPC.kwil_ping: ignore,
    GRPC.kwil_getSchema: ignore,
    GRPC.kwil_getConfig: ignore,
    GRPC.kwil_listDatabase: apply_validator_at_index(validate_address, 0),
    GRPC.kwil_getAccount: apply_validator_at_index(validate_address, 0),
}


def get_request_formatters(method_name: RPCEndpoint) -> Callable[..., Any]:
    formatter_maps = (
        request_validators,
    )

    return compose(
        *[formatter_map[method_name] for formatter_map in formatter_maps if method_name in formatter_map])


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
    result = json.loads(base64.b64decode(response["body"]))
    response["body"] = result
    return response


response_formatters: Dict[str, Callable[[Any], Any]] = {
    GRPC.kwil_ping: ping_response_formatter,
    # GRPC.kwil_getSchema: extract_result,
    GRPC.kwil_getConfig: identity,
    GRPC.kwil_getAccount: extract_result("account"),
    GRPC.kwil_estimatePrice: extract_result("price"),
    GRPC.kwil_broadcast: tx_receipt_decode,
}


def get_response_formatters(method_name: RPCEndpoint, module: "Module") -> Callable[..., Any]:
    formatter_maps = (
        response_formatters,
    )

    return compose(
        *[formatter_map[method_name] for formatter_map in formatter_maps if method_name in formatter_map])