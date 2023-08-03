from kwil.tx.v1 import tx_pb2 as _tx_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CallRequest(_message.Message):
    __slots__ = ["payload", "sender", "signature"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    sender: str
    signature: _tx_pb2.Signature
    def __init__(self, payload: _Optional[bytes] = ..., signature: _Optional[_Union[_tx_pb2.Signature, _Mapping]] = ..., sender: _Optional[str] = ...) -> None: ...

class CallResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bytes
    def __init__(self, result: _Optional[bytes] = ...) -> None: ...
