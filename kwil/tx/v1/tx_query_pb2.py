# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kwil/tx/v1/tx_query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kwil.tx.v1 import tx_pb2 as kwil_dot_tx_dot_v1_dot_tx__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19kwil/tx/v1/tx_query.proto\x12\x02tx\x1a\x13kwil/tx/v1/tx.proto\"*\n\x0eTxQueryRequest\x12\x18\n\x07tx_hash\x18\x01 \x01(\x0cR\x07tx_hash\"\x81\x01\n\x0fTxQueryResponse\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12\x1b\n\x02tx\x18\x03 \x01(\x0b\x32\x0f.tx.Transaction\x12\x33\n\ttx_result\x18\x04 \x01(\x0b\x32\x15.tx.TransactionResultR\ttx_resultB5Z3github.com/kwilteam/kwil-db/api/protobuf/tx/v1;txpbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kwil.tx.v1.tx_query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/kwilteam/kwil-db/api/protobuf/tx/v1;txpb'
  _TXQUERYREQUEST._serialized_start=54
  _TXQUERYREQUEST._serialized_end=96
  _TXQUERYRESPONSE._serialized_start=99
  _TXQUERYRESPONSE._serialized_end=228
# @@protoc_insertion_point(module_scope)