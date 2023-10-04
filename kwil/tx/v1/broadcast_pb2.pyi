from kwil.tx.v1 import tx_pb2 as _tx_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BroadcastRequest(_message.Message):
    __slots__ = ["tx"]
    TX_FIELD_NUMBER: _ClassVar[int]
    tx: _tx_pb2.Transaction
    def __init__(self, tx: _Optional[_Union[_tx_pb2.Transaction, _Mapping]] = ...) -> None: ...

class BroadcastResponse(_message.Message):
    __slots__ = ["tx_hash"]
    TX_HASH_FIELD_NUMBER: _ClassVar[int]
    tx_hash: bytes
    def __init__(self, tx_hash: _Optional[bytes] = ...) -> None: ...
