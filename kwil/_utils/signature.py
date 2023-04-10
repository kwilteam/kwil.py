from eth_account import Account

from web3 import Web3

from kwil.kwil_typing.kvm import HexStr
from kwil.types import Signature, SignatureType



def sign(data: bytes, private_key: HexStr) -> Signature:
    signature_type = SignatureType.PK_SECP256K1_UNCOMPRESSED
    message_hash_bytes = Web3.keccak(data)

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
    return Signature(signature_bytes=bytes(signature_byte_array), signature_type=signature_type)