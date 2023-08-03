from typing import List, Dict, Any
import base64
import json
import hashlib


from eth_account.signers.local import LocalAccount

from kwil.types import (
    ActionParamValue,
    ActionParamDataType,
    CallParam,
    CallSigningPayload,
    CallActionPayload,
)
from kwil._utils.signature import sign

action_param_text_byte = ActionParamDataType.TEXT.to_bytes(1, byteorder="little")
action_param_int_byte = ActionParamDataType.INT.to_bytes(1, byteorder="little")


def encode_param(_type: bytes, _value: bytes) -> str:
    # encode type and value as base64 string
    bs = bytearray()
    bs.extend(_type)
    bs.extend(_value)
    encoded = base64.b64encode(bs).decode("utf-8")
    return encoded


def _encode_action_value(value: Any) -> ActionParamValue:
    if isinstance(value, str):
        encoded = encode_param(action_param_text_byte, value.encode())
        return ActionParamValue(
            value=value,
            dataType=ActionParamDataType.TEXT,
            bytes=encoded,
        )
    elif isinstance(value, int):
        encoded = encode_param(
            action_param_int_byte, value.to_bytes(8, byteorder="little")
        )
        return ActionParamValue(
            value=value,
            dataType=ActionParamDataType.INT,
            bytes=encoded,
        )
    else:
        raise ValueError(f"Unsupported type {type(value)}")


def encode_action_inputs(inputs: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    encoded_inputs = []
    for input in inputs:
        encoded_input = {}
        for key, value in input.items():
            encoded_value = _encode_action_value(value)
            encoded_input[key] = encoded_value["bytes"]
        encoded_inputs.append(encoded_input)
    return encoded_inputs


def sign_call_action(payload: CallActionPayload, wallet: LocalAccount) -> CallParam:
    """
    Sign a call action payload with a wallet, and return a CallParam object.
    If no wallet is provided, return a CallParam object without a signature.
    """
    if wallet:
        # backward compatibility
        signing_payload = CallSigningPayload(
            action=payload["action"],
            dbid=payload["dbid"],
            params=payload["args"],
        )

        payload = json.dumps(signing_payload).encode()
        payload_bytes = json.dumps(signing_payload).encode()
        payload_hash = hashlib.sha384(payload_bytes)

        payload_hash_bytes = payload_hash.digest()

        sig = sign(payload_hash_bytes, wallet.key)
        return CallParam(
            payload=payload,
            signature=sig,
            sender=wallet.address,
        )
    else:
        return CallParam(payload=payload)

