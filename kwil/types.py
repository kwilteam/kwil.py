from typing import (
    Any,
    List,
    Dict,
    NewType,
    TypeVar,
    TypedDict,
    Callable,
)
from enum import IntEnum

from kwil_typing import (
    DBIdentifier,
    HexAddress,
)


class RPCResponse(TypedDict, total=False):
    error: Any
    result: Any


URI = NewType("URI", str)
RPCEndpoint = NewType("RPCEndpoint", str)
Nonce = NewType("Nonce", int)
TReturn = TypeVar("TReturn")
TParams = TypeVar("TParams")
Middleware = Callable[[RPCEndpoint, Any], RPCResponse]


class DatasetIdentifier(TypedDict, total=True):
    owner: str
    name: str


class TxPayloadType(IntEnum):
    INVALID_PAYLOAD_TYPE = 100
    DEPLOY_DATABASE = 101
    MODIFY_DATABASE = 102
    DROP_DATABASE = 103
    EXECUTE_ACTION = 104
    END_PAYLOAD_TYPE = 105

    def __str__(self):
        return f"{self.name}"


class SignatureType(IntEnum):
    SIGNATURE_TYPE_INVALID = 0
    PK_SECP256K1_UNCOMPRESSED = 1
    ACCOUNT_SECP256K1_UNCOMPRESSED = 2
    END_SIGNATURE_TYPE = 3

    def __str__(self):
        return f"{self.name}"


class ColumnType(IntEnum):
    INVALID_COLUMN_TYPE = 100
    NULL = 101
    TEXT = 102
    INT = 103
    END_COLUMN_TYPE = 104

    def __str__(self):
        return f"{self.name}"


class AttributeType(IntEnum):
    INVALID_ATTRIBUTE_TYPE = 0
    PRIMARY_KEY = 1
    UNIQUE = 2
    NOT_NULL = 3
    DEFAULT = 4
    MIN = 5
    MAX = 6
    MIN_LENGTH = 7
    MAX_LENGTH = 8
    END_ATTRIBUTE_TYPE = 4

    def __str__(self):
        return f"{self.name}"


class IndexType(IntEnum):
    INVALID_INDEX_TYPE = 100
    BTREE = 101
    UNIQUE_BTREE = 102
    END_INDEX_TYPE = 103

    def __str__(self):
        return f"{self.name}"


class Signature(TypedDict, total=True):
    signature_bytes: bytes
    signature_type: SignatureType


class TxParams(TypedDict, total=False):
    hash: bytes
    payloadType: TxPayloadType
    payload: bytes
    fee: str
    nonce: Nonce
    signature: Signature
    sender: str


class TxReceipt(TypedDict, total=False):
    hash: bytes
    fee: str
    body: Dict[str, Any]
    result: Dict[str, Any]


class AccountInfo(TypedDict, total=False):
    address: HexAddress
    nonce: Nonce
    balance: str


class AttributeSchema(TypedDict, total=False):
    type: AttributeType
    value: bytes


class ColumnSchema(TypedDict, total=False):
    name: str
    type: ColumnType
    attributes: List[AttributeSchema]


class IndexSchema(TypedDict, total=False):
    name: str
    columns: List[str]
    type: IndexType


class TableSchema(TypedDict, total=False):
    name: str
    columns: List[ColumnSchema]
    indexes: List[IndexSchema]


class ActionSchema(TypedDict, total=False):
    name: str
    public: bool
    inputs: List[str]
    statements: List[str]


class DBSchema(TypedDict, total=False):
    owner: HexAddress
    name: str
    tables: List[TableSchema]
    actions: List[ActionSchema]


class ServiceConfig(TypedDict, total=False):
    chainCode: int
    providerAddress: HexAddress
    poolAddress: HexAddress


class ActionExecution(TypedDict, total=False):
    action: str
    dbID: DBIdentifier
    params: List[Dict[str, Any]]


class ActionParamDataType(IntEnum):
    INVALID_DATA_TYPE = 100
    NULL = 101
    TEXT = 102
    INT = 103
    END_DATA_TYPE = 104

    def __str__(self):
        return f"{self.name}"


class ActionParamValue(TypedDict, total=False):
    value: Any
    dataType: ActionParamDataType
    bytes: str
