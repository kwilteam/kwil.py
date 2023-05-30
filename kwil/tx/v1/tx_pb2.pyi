from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACCOUNT_SECP256K1_UNCOMPRESSED: SignatureType
DESCRIPTOR: _descriptor.FileDescriptor
END_SIGNATURE_TYPE: SignatureType
INVALID_SINATURE_TYPE: SignatureType
PK_SECP256K1_UNCOMPRESSED: SignatureType

class Signature(_message.Message):
    __slots__ = ["signature_bytes", "signature_type"]
    SIGNATURE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    signature_bytes: bytes
    signature_type: int
    def __init__(self, signature_bytes: _Optional[bytes] = ..., signature_type: _Optional[int] = ...) -> None: ...

class Tx(_message.Message):
    __slots__ = ["fee", "hash", "nonce", "payload", "payload_type", "sender", "signature"]
    FEE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    fee: str
    hash: bytes
    nonce: int
    payload: bytes
    payload_type: int
    sender: str
    signature: Signature
    def __init__(self, hash: _Optional[bytes] = ..., payload_type: _Optional[int] = ..., payload: _Optional[bytes] = ..., nonce: _Optional[int] = ..., signature: _Optional[_Union[Signature, _Mapping]] = ..., fee: _Optional[str] = ..., sender: _Optional[str] = ...) -> None: ...

class TxReceipt(_message.Message):
    __slots__ = ["body", "fee", "tx_hash"]
    BODY_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    TX_HASH_FIELD_NUMBER: _ClassVar[int]
    body: bytes
    fee: str
    tx_hash: bytes
    def __init__(self, tx_hash: _Optional[bytes] = ..., fee: _Optional[str] = ..., body: _Optional[bytes] = ...) -> None: ...

class SignatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
