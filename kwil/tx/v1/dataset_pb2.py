# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kwil/tx/v1/dataset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18kwil/tx/v1/dataset.proto\x12\x02tx\" \n\x10GetSchemaRequest\x12\x0c\n\x04\x64\x62id\x18\x01 \x01(\t\"/\n\x11GetSchemaResponse\x12\x1a\n\x06schema\x18\x01 \x01(\x0b\x32\n.tx.Schema\"\x81\x01\n\x06Schema\x12\r\n\x05owner\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x06tables\x18\x03 \x03(\x0b\x32\t.tx.Table\x12\x1b\n\x07\x61\x63tions\x18\x04 \x03(\x0b\x32\n.tx.Action\x12\"\n\nextensions\x18\x05 \x03(\x0b\x32\x0e.tx.Extensions\"N\n\x05Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\n.tx.Column\x12\x1a\n\x07indexes\x18\x03 \x03(\x0b\x32\t.tx.Index\"G\n\x06\x43olumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12!\n\nattributes\x18\x03 \x03(\x0b\x32\r.tx.Attribute\"(\n\tAttribute\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"4\n\x05Index\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x02 \x03(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"s\n\x06\x41\x63tion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06public\x18\x02 \x01(\x08\x12\x0e\n\x06inputs\x18\x03 \x03(\t\x12\x12\n\nstatements\x18\x04 \x03(\t\x12\x12\n\nmutability\x18\x05 \x01(\t\x12\x13\n\x0b\x61uxiliaries\x18\x06 \x03(\t\"\x95\x01\n\nExtensions\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x0einitialization\x18\x02 \x03(\x0b\x32\x1e.tx.Extensions.ExtensionConfig\x12\r\n\x05\x61lias\x18\x03 \x01(\t\x1a\x32\n\x0f\x45xtensionConfig\x12\x10\n\x08\x61rgument\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB5Z3github.com/kwilteam/kwil-db/api/protobuf/tx/v1;txpbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kwil.tx.v1.dataset_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/kwilteam/kwil-db/api/protobuf/tx/v1;txpb'
  _GETSCHEMAREQUEST._serialized_start=32
  _GETSCHEMAREQUEST._serialized_end=64
  _GETSCHEMARESPONSE._serialized_start=66
  _GETSCHEMARESPONSE._serialized_end=113
  _SCHEMA._serialized_start=116
  _SCHEMA._serialized_end=245
  _TABLE._serialized_start=247
  _TABLE._serialized_end=325
  _COLUMN._serialized_start=327
  _COLUMN._serialized_end=398
  _ATTRIBUTE._serialized_start=400
  _ATTRIBUTE._serialized_end=440
  _INDEX._serialized_start=442
  _INDEX._serialized_end=494
  _ACTION._serialized_start=496
  _ACTION._serialized_end=611
  _EXTENSIONS._serialized_start=614
  _EXTENSIONS._serialized_end=763
  _EXTENSIONS_EXTENSIONCONFIG._serialized_start=713
  _EXTENSIONS_EXTENSIONCONFIG._serialized_end=763
# @@protoc_insertion_point(module_scope)
