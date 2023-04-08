from kwil.tx.v1 import tx_pb2 as _tx_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BroadcastRequest(_message.Message):
    __slots__ = ["tx"]
    TX_FIELD_NUMBER: _ClassVar[int]
    tx: _tx_pb2.Tx
    def __init__(self, tx: _Optional[_Union[_tx_pb2.Tx, _Mapping]] = ...) -> None: ...

class BroadcastResponse(_message.Message):
    __slots__ = ["receipt"]
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    receipt: _tx_pb2.TxReceipt
    def __init__(self, receipt: _Optional[_Union[_tx_pb2.TxReceipt, _Mapping]] = ...) -> None: ...
