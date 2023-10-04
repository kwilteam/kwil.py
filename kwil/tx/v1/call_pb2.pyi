from kwil.tx.v1 import tx_pb2 as _tx_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CallRequest(_message.Message):
    __slots__ = ["body", "sender", "serialization", "signature"]
    class Body(_message.Message):
        __slots__ = ["description", "payload"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        description: str
        payload: bytes
        def __init__(self, description: _Optional[str] = ..., payload: _Optional[bytes] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SERIALIZATION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    body: CallRequest.Body
    sender: bytes
    serialization: str
    signature: _tx_pb2.Signature
    def __init__(self, body: _Optional[_Union[CallRequest.Body, _Mapping]] = ..., signature: _Optional[_Union[_tx_pb2.Signature, _Mapping]] = ..., sender: _Optional[bytes] = ..., serialization: _Optional[str] = ...) -> None: ...

class CallResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bytes
    def __init__(self, result: _Optional[bytes] = ...) -> None: ...
