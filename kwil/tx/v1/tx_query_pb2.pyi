from kwil.tx.v1 import tx_pb2 as _tx_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TxQueryRequest(_message.Message):
    __slots__ = ["tx_hash"]
    TX_HASH_FIELD_NUMBER: _ClassVar[int]
    tx_hash: bytes
    def __init__(self, tx_hash: _Optional[bytes] = ...) -> None: ...

class TxQueryResponse(_message.Message):
    __slots__ = ["hash", "height", "tx", "tx_result"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    TX_RESULT_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    height: int
    tx: _tx_pb2.Transaction
    tx_result: _tx_pb2.TransactionResult
    def __init__(self, hash: _Optional[bytes] = ..., height: _Optional[int] = ..., tx: _Optional[_Union[_tx_pb2.Transaction, _Mapping]] = ..., tx_result: _Optional[_Union[_tx_pb2.TransactionResult, _Mapping]] = ...) -> None: ...
