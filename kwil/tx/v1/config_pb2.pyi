from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetConfigRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetConfigResponse(_message.Message):
    __slots__ = ["chain_code", "pool_address", "provider_address"]
    CHAIN_CODE_FIELD_NUMBER: _ClassVar[int]
    POOL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    chain_code: int
    pool_address: str
    provider_address: str
    def __init__(self, chain_code: _Optional[int] = ..., provider_address: _Optional[str] = ..., pool_address: _Optional[str] = ...) -> None: ...
