from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Signature(_message.Message):
    __slots__ = ["signature_bytes", "signature_type"]
    SIGNATURE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    signature_bytes: bytes
    signature_type: str
    def __init__(self, signature_bytes: _Optional[bytes] = ..., signature_type: _Optional[str] = ...) -> None: ...

class Transaction(_message.Message):
    __slots__ = ["body", "sender", "serialization", "signature"]
    class Body(_message.Message):
        __slots__ = ["description", "fee", "nonce", "payload", "payload_type", "salt"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        FEE_FIELD_NUMBER: _ClassVar[int]
        NONCE_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
        SALT_FIELD_NUMBER: _ClassVar[int]
        description: str
        fee: str
        nonce: int
        payload: bytes
        payload_type: str
        salt: bytes
        def __init__(self, payload: _Optional[bytes] = ..., payload_type: _Optional[str] = ..., fee: _Optional[str] = ..., nonce: _Optional[int] = ..., salt: _Optional[bytes] = ..., description: _Optional[str] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SERIALIZATION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    body: Transaction.Body
    sender: bytes
    serialization: str
    signature: Signature
    def __init__(self, body: _Optional[_Union[Transaction.Body, _Mapping]] = ..., signature: _Optional[_Union[Signature, _Mapping]] = ..., sender: _Optional[bytes] = ..., serialization: _Optional[str] = ...) -> None: ...

class TransactionResult(_message.Message):
    __slots__ = ["code", "data", "events", "gas_used", "gas_wanted", "log"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    GAS_USED_FIELD_NUMBER: _ClassVar[int]
    GAS_WANTED_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    code: int
    data: bytes
    events: _containers.RepeatedScalarFieldContainer[bytes]
    gas_used: int
    gas_wanted: int
    log: str
    def __init__(self, code: _Optional[int] = ..., log: _Optional[str] = ..., gas_used: _Optional[int] = ..., gas_wanted: _Optional[int] = ..., data: _Optional[bytes] = ..., events: _Optional[_Iterable[bytes]] = ...) -> None: ...

class TransactionStatus(_message.Message):
    __slots__ = ["errors", "fee", "id", "status"]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedScalarFieldContainer[str]
    fee: str
    id: bytes
    status: str
    def __init__(self, id: _Optional[bytes] = ..., fee: _Optional[str] = ..., status: _Optional[str] = ..., errors: _Optional[_Iterable[str]] = ...) -> None: ...
