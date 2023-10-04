from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListDatabasesRequest(_message.Message):
    __slots__ = ["owner"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    owner: bytes
    def __init__(self, owner: _Optional[bytes] = ...) -> None: ...

class ListDatabasesResponse(_message.Message):
    __slots__ = ["databases"]
    DATABASES_FIELD_NUMBER: _ClassVar[int]
    databases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, databases: _Optional[_Iterable[str]] = ...) -> None: ...
