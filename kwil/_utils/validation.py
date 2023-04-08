from typing import Any, cast, Dict

import eth_utils as etu

from kwil.exceptions import InvalidAddress
from kwil.types import Signature


def ignore(value: Any) -> None:
    return None


def identity(value: Any) -> Any:
    return value


def is_not_address_string(value: Any) -> bool:
    return (etu.is_string(value) and not etu.is_bytes(value) and not
            etu.is_checksum_address(value) and not etu.is_hex_address(value))


def validate_address(value: Any) -> None:
    """
    Helper function for validating an address. Here we use eth address validation.
    """
    if not isinstance(value, str):
        raise TypeError('Address {} must be provided as a string'.format(value))

    if not etu.is_hex_address(value):
        raise InvalidAddress("Address must be 20 bytes, as a hex string with a 0x prefix", value)

    if not etu.is_checksum_address(value):
        raise InvalidAddress("Address has a invalid checksum", value)


def validate_tx_params(value: Any) -> None:
    """
    Helper function for validating transaction parameters.
    """
    if not isinstance(value, dict):
        raise TypeError('Transaction parameters must be provided as a dictionary')


    if 'sender' in value:
        validate_address(value['sender'])

    if 'fee' in value and not isinstance(value['fee'], str):
        raise TypeError('Fee must be provided as an integer')

    if 'nonce' in value and not isinstance(value['nonce'], int):
        raise TypeError('Nonce must be provided as an integer')

    if 'payloadType' in value and not isinstance(value['payloadType'], int):
        raise TypeError('PayloadType must be provided as a integer')

    if 'payload' in value and not isinstance(value['payload'], bytes):
        raise TypeError('Payload must be provided as a string')

    if 'hash' in value and not isinstance(value['hash'], bytes):
        raise TypeError('Hash must be provided as an bytes')

    if 'signature' in value and not isinstance(value['signature'], dict):
        raise TypeError('Signature must be provided as an bytes')
