from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Action(_message.Message):
    __slots__ = ["auxiliaries", "inputs", "mutability", "name", "public", "statements"]
    AUXILIARIES_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    MUTABILITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    auxiliaries: _containers.RepeatedScalarFieldContainer[str]
    inputs: _containers.RepeatedScalarFieldContainer[str]
    mutability: str
    name: str
    public: bool
    statements: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., public: bool = ..., inputs: _Optional[_Iterable[str]] = ..., statements: _Optional[_Iterable[str]] = ..., mutability: _Optional[str] = ..., auxiliaries: _Optional[_Iterable[str]] = ...) -> None: ...

class Attribute(_message.Message):
    __slots__ = ["type", "value"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: str
    value: str
    def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Column(_message.Message):
    __slots__ = ["attributes", "name", "type"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    name: str
    type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...) -> None: ...

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
    type: str
    def __init__(self, name: _Optional[str] = ..., columns: _Optional[_Iterable[str]] = ..., type: _Optional[str] = ...) -> None: ...

class Table(_message.Message):
    __slots__ = ["columns", "indexes", "name"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[Column]
    indexes: _containers.RepeatedCompositeFieldContainer[Index]
    name: str
    def __init__(self, name: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[Column, _Mapping]]] = ..., indexes: _Optional[_Iterable[_Union[Index, _Mapping]]] = ...) -> None: ...
