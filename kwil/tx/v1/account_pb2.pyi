from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["address", "balance", "nonce"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    address: str
    balance: str
    nonce: int
    def __init__(self, address: _Optional[str] = ..., balance: _Optional[str] = ..., nonce: _Optional[int] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class GetAccountResponse(_message.Message):
    __slots__ = ["account"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...
