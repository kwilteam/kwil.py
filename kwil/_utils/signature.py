from typing import Optional, Union

from eth_account import Account
from eth_utils import to_bytes, keccak as eth_utils_keccak
from hexbytes import (
    HexBytes,
)

from kwil_typing import HexStr
from kwil.types import Signature, SignatureType


def keccak(
    primitive: Union[bytes, int, bool, None] = None,
    text: Optional[str] = None,
    hexstr: Optional[HexStr] = None,
) -> HexBytes:
    if isinstance(primitive, (bytes, int, type(None))):
        input_bytes = to_bytes(primitive, hexstr=hexstr, text=text)
        return HexBytes(eth_utils_keccak(input_bytes))

    raise TypeError(
        f"You called keccak with first arg {primitive!r} and keywords "
        f"{{'text': {text!r}, 'hexstr': {hexstr!r}}}. You must call it with "
        "one of these approaches: keccak(text='txt'), keccak(hexstr='0x747874'), "
        "keccak(b'\\x74\\x78\\x74'), or keccak(0x747874)."
    )


def sign(data: bytes, private_key: HexStr) -> Signature:
    signature_type = SignatureType.PK_SECP256K1_UNCOMPRESSED
    message_hash_bytes = keccak(data)

    # message_hash_hex = message_hash_bytes.hex()
    # signable_message = messages.encode_defunct(message_hash_bytes)
    # signature_bytes = Account.sign_message(signable_message, private_key).signature
    # print("signature_bytes 000", [b for b in signature_bytes])

    signature_bytes = Account.signHash(message_hash_bytes, private_key).signature
    signature_byte_array = bytearray()
    signature_byte_array.extend(signature_bytes[:-1])

    # set V=0, to keep aligned with Go IMPL
    # https://github.com/ethereum/go-ethereum/blob/v1.10.21/crypto/secp256k1/secp256.go#L97
    signature_byte_array.append(signature_bytes[-1] - 27)
    return Signature(
        signature_bytes=bytes(signature_byte_array), signature_type=signature_type
    )
