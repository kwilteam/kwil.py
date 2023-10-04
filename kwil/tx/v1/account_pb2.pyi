from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["balance", "nonce", "public_key"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    balance: str
    nonce: int
    public_key: bytes
    def __init__(self, public_key: _Optional[bytes] = ..., balance: _Optional[str] = ..., nonce: _Optional[int] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ["public_key"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    def __init__(self, public_key: _Optional[bytes] = ...) -> None: ...

class GetAccountResponse(_message.Message):
    __slots__ = ["account"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...
