from kwil.tx.v1 import tx_pb2 as _tx_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EstimatePriceRequest(_message.Message):
    __slots__ = ["tx"]
    TX_FIELD_NUMBER: _ClassVar[int]
    tx: _tx_pb2.Transaction
    def __init__(self, tx: _Optional[_Union[_tx_pb2.Transaction, _Mapping]] = ...) -> None: ...

class EstimatePriceResponse(_message.Message):
    __slots__ = ["price"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: str
    def __init__(self, price: _Optional[str] = ...) -> None: ...
