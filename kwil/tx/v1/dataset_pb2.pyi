from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

BTREE_INDEX_TYPE: IndexType
DEFAULT: AttributeType
DESCRIPTOR: _descriptor.FileDescriptor
INT_DATA_TYPE: DataType
INVALID_ATTRIBUTE: AttributeType
INVALID_DATA_TYPE: DataType
INVALID_INDEX_TYPE: IndexType
MAX: AttributeType
MAX_LENGTH: AttributeType
MIN: AttributeType
MIN_LENGTH: AttributeType
NOT_NULL: AttributeType
NULL_DATA_TYPE: DataType
PRIMARY_KEY: AttributeType
STRING_DATA_TYPE: DataType
UNIQUE: AttributeType
UNIQUE_BTREE_INDEX_TYPE: IndexType

class Action(_message.Message):
    __slots__ = ["inputs", "name", "public", "statements"]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.RepeatedScalarFieldContainer[str]
    name: str
    public: bool
    statements: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., public: bool = ..., inputs: _Optional[_Iterable[str]] = ..., statements: _Optional[_Iterable[str]] = ...) -> None: ...

class Attribute(_message.Message):
    __slots__ = ["type", "value"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: AttributeType
    value: bytes
    def __init__(self, type: _Optional[_Union[AttributeType, str]] = ..., value: _Optional[bytes] = ...) -> None: ...

class Column(_message.Message):
    __slots__ = ["attributes", "name", "type"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    name: str
    type: DataType
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[DataType, str]] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

class Dataset(_message.Message):
    __slots__ = ["actions", "name", "owner", "tables"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    name: str
    owner: str
    tables: _containers.RepeatedCompositeFieldContainer[Table]
    def __init__(self, owner: _Optional[str] = ..., name: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[Table, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class GetSchemaRequest(_message.Message):
    __slots__ = ["dbid"]
    DBID_FIELD_NUMBER: _ClassVar[int]
    dbid: str
    def __init__(self, dbid: _Optional[str] = ...) -> None: ...

class GetSchemaResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: Dataset
    def __init__(self, dataset: _Optional[_Union[Dataset, _Mapping]] = ...) -> None: ...

class Index(_message.Message):
    __slots__ = ["columns", "name", "type"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]
    name: str
    type: IndexType
    def __init__(self, name: _Optional[str] = ..., columns: _Optional[_Iterable[str]] = ..., type: _Optional[_Union[IndexType, str]] = ...) -> None: ...

class Table(_message.Message):
    __slots__ = ["columns", "indexes", "name"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    indexes: _containers.RepeatedCompositeFieldContainer[Index]
    name: str
    def __init__(self, name: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ..., indexes: _Optional[_Iterable[_Union[Index, _Mapping]]] = ...) -> None: ...

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AttributeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IndexType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
