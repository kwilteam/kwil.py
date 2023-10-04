from kwil.tx.v1 import tx_pb2 as _tx_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
ERROR: RequestStatus
OK: RequestStatus

class CurrentValidatorsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CurrentValidatorsResponse(_message.Message):
    __slots__ = ["validators"]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    validators: _containers.RepeatedCompositeFieldContainer[Validator]
    def __init__(self, validators: _Optional[_Iterable[_Union[Validator, _Mapping]]] = ...) -> None: ...

class Validator(_message.Message):
    __slots__ = ["power", "pubkey"]
    POWER_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    power: int
    pubkey: bytes
    def __init__(self, pubkey: _Optional[bytes] = ..., power: _Optional[int] = ...) -> None: ...

class ValidatorApprovalRequest(_message.Message):
    __slots__ = ["PubKey"]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    PubKey: bytes
    def __init__(self, PubKey: _Optional[bytes] = ...) -> None: ...

class ValidatorApprovalResponse(_message.Message):
    __slots__ = ["log", "status"]
    LOG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    log: str
    status: RequestStatus
    def __init__(self, status: _Optional[_Union[RequestStatus, str]] = ..., log: _Optional[str] = ...) -> None: ...

class ValidatorJoinRequest(_message.Message):
    __slots__ = ["tx"]
    TX_FIELD_NUMBER: _ClassVar[int]
    tx: _tx_pb2.Transaction
    def __init__(self, tx: _Optional[_Union[_tx_pb2.Transaction, _Mapping]] = ...) -> None: ...

class ValidatorJoinResponse(_message.Message):
    __slots__ = ["receipt"]
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    receipt: _tx_pb2.TransactionStatus
    def __init__(self, receipt: _Optional[_Union[_tx_pb2.TransactionStatus, _Mapping]] = ...) -> None: ...

class ValidatorJoinStatusRequest(_message.Message):
    __slots__ = ["pubkey"]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    pubkey: bytes
    def __init__(self, pubkey: _Optional[bytes] = ...) -> None: ...

class ValidatorJoinStatusResponse(_message.Message):
    __slots__ = ["approved_validators", "pending_validators", "power"]
    APPROVED_VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    PENDING_VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    approved_validators: _containers.RepeatedScalarFieldContainer[bytes]
    pending_validators: _containers.RepeatedScalarFieldContainer[bytes]
    power: int
    def __init__(self, approved_validators: _Optional[_Iterable[bytes]] = ..., pending_validators: _Optional[_Iterable[bytes]] = ..., power: _Optional[int] = ...) -> None: ...

class ValidatorLeaveRequest(_message.Message):
    __slots__ = ["tx"]
    TX_FIELD_NUMBER: _ClassVar[int]
    tx: _tx_pb2.Transaction
    def __init__(self, tx: _Optional[_Union[_tx_pb2.Transaction, _Mapping]] = ...) -> None: ...

class ValidatorLeaveResponse(_message.Message):
    __slots__ = ["receipt"]
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    receipt: _tx_pb2.TransactionStatus
    def __init__(self, receipt: _Optional[_Union[_tx_pb2.TransactionStatus, _Mapping]] = ...) -> None: ...

class RequestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
