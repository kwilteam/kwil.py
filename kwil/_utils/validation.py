from typing import Any, Dict, Callable

from toolz import compose, identity
import eth_utils as etu

from kwil.exceptions import InvalidAddress
from kwil._utils.utils import apply_validator_at_index
from kwil._utils.rpcs import GRPC
from kwil.types import RPCEndpoint


def is_not_address_string(value: Any) -> bool:
    return (
        etu.is_string(value)
        and not etu.is_bytes(value)
        and not etu.is_checksum_address(value)
        and not etu.is_hex_address(value)
    )


def validate_query(value: Any) -> None:
    """
    Helper function for validating a query.
    """
    if not isinstance(value, str):
        raise TypeError("Query {} must be provided as a string".format(value))


def validate_db_identifier(value: Any) -> None:
    """
    Helper function for validating a database identifier.
    """
    if not isinstance(value, str):
        raise TypeError(
            "Database identifier {} must be provided as a string".format(value)
        )

    if not value.startswith("x"):
        raise TypeError('Database identifier {} must start with "x"'.format(value))

    if not len(value) == 57:  # sha224 is 28 bytes, so 56 hex chars + 1 prefix
        raise TypeError("Database identifier {} must be 29 bytes".format(value))


def validate_address(value: Any) -> None:
    """
    Helper function for validating an address. Here we use eth address validation.
    """
    if not isinstance(value, str):
        raise TypeError("Address {} must be provided as a string".format(value))

    if not etu.is_hex_address(value):
        raise InvalidAddress(
            "Address must be 20 bytes, as a hex string with a 0x prefix", value
        )

    if not etu.is_checksum_address(value):
        raise InvalidAddress("Address has a invalid checksum", value)


def validate_tx_params(value: Any) -> None:
    """
    Helper function for validating transaction parameters.
    """
    if not isinstance(value, dict):
        raise TypeError("Transaction parameters must be provided as a dictionary")

    if "sender" in value:
        validate_address(value["sender"])

    if "fee" in value and not isinstance(value["fee"], str):
        raise TypeError("Fee must be provided as an integer")

    if "nonce" in value and not isinstance(value["nonce"], int):
        raise TypeError("Nonce must be provided as an integer")

    if "payloadType" in value and not isinstance(value["payloadType"], int):
        raise TypeError("PayloadType must be provided as a integer")

    if "payload" in value and not isinstance(value["payload"], bytes):
        raise TypeError("Payload must be provided as a string")

    if "hash" in value and not isinstance(value["hash"], bytes):
        raise TypeError("Hash must be provided as an bytes")

    if "signature" in value and not isinstance(value["signature"], dict):
        raise TypeError("Signature must be provided as an bytes")


request_validators: Dict[RPCEndpoint, Callable[..., Any]] = {
    GRPC.kwil_ping: identity,
    GRPC.kwil_getConfig: identity,
    GRPC.kwil_getSchema: apply_validator_at_index(validate_db_identifier, 0),
    GRPC.kwil_getAccount: apply_validator_at_index(validate_address, 0),
    GRPC.kwil_listDatabase: apply_validator_at_index(validate_address, 0),
    GRPC.kwil_broadcast: apply_validator_at_index(validate_tx_params, 0),
    GRPC.kwil_estimatePrice: apply_validator_at_index(validate_tx_params, 0),
    GRPC.kwil_query: compose(
        apply_validator_at_index(validate_db_identifier, 0),
        apply_validator_at_index(validate_query, 1),
    ),
}
