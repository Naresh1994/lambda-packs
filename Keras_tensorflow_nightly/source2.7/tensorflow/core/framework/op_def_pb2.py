# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/op_def.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import attr_value_pb2 as tensorflow_dot_core_dot_framework_dot_attr__value__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/op_def.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n&tensorflow/core/framework/op_def.proto\x12\ntensorflow\x1a*tensorflow/core/framework/attr_value.proto\x1a%tensorflow/core/framework/types.proto\"\xb8\x05\n\x05OpDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\tinput_arg\x18\x02 \x03(\x0b\x32\x18.tensorflow.OpDef.ArgDef\x12,\n\noutput_arg\x18\x03 \x03(\x0b\x32\x18.tensorflow.OpDef.ArgDef\x12\'\n\x04\x61ttr\x18\x04 \x03(\x0b\x32\x19.tensorflow.OpDef.AttrDef\x12.\n\x0b\x64\x65precation\x18\x08 \x01(\x0b\x32\x19.tensorflow.OpDeprecation\x12\x0f\n\x07summary\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x16\n\x0eis_commutative\x18\x12 \x01(\x08\x12\x14\n\x0cis_aggregate\x18\x10 \x01(\x08\x12\x13\n\x0bis_stateful\x18\x11 \x01(\x08\x12\"\n\x1a\x61llows_uninitialized_input\x18\x13 \x01(\x08\x1a\x9f\x01\n\x06\x41rgDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\"\n\x04type\x18\x03 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x11\n\ttype_attr\x18\x04 \x01(\t\x12\x13\n\x0bnumber_attr\x18\x05 \x01(\t\x12\x16\n\x0etype_list_attr\x18\x06 \x01(\t\x12\x0e\n\x06is_ref\x18\x10 \x01(\x08\x1a\xbd\x01\n\x07\x41ttrDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12,\n\rdefault_value\x18\x03 \x01(\x0b\x32\x15.tensorflow.AttrValue\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bhas_minimum\x18\x05 \x01(\x08\x12\x0f\n\x07minimum\x18\x06 \x01(\x03\x12-\n\x0e\x61llowed_values\x18\x07 \x01(\x0b\x32\x15.tensorflow.AttrValue\"5\n\rOpDeprecation\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x13\n\x0b\x65xplanation\x18\x02 \x01(\t\"\'\n\x06OpList\x12\x1d\n\x02op\x18\x01 \x03(\x0b\x32\x11.tensorflow.OpDefB,\n\x18org.tensorflow.frameworkB\x0bOpDefProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_attr__value__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])




_OPDEF_ARGDEF = _descriptor.Descriptor(
  name='ArgDef',
  full_name='tensorflow.OpDef.ArgDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.OpDef.ArgDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='tensorflow.OpDef.ArgDef.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.OpDef.ArgDef.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_attr', full_name='tensorflow.OpDef.ArgDef.type_attr', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_attr', full_name='tensorflow.OpDef.ArgDef.number_attr', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_list_attr', full_name='tensorflow.OpDef.ArgDef.type_list_attr', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_ref', full_name='tensorflow.OpDef.ArgDef.is_ref', index=6,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=483,
  serialized_end=642,
)

_OPDEF_ATTRDEF = _descriptor.Descriptor(
  name='AttrDef',
  full_name='tensorflow.OpDef.AttrDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.OpDef.AttrDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.OpDef.AttrDef.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_value', full_name='tensorflow.OpDef.AttrDef.default_value', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='tensorflow.OpDef.AttrDef.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_minimum', full_name='tensorflow.OpDef.AttrDef.has_minimum', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum', full_name='tensorflow.OpDef.AttrDef.minimum', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowed_values', full_name='tensorflow.OpDef.AttrDef.allowed_values', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=645,
  serialized_end=834,
)

_OPDEF = _descriptor.Descriptor(
  name='OpDef',
  full_name='tensorflow.OpDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.OpDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_arg', full_name='tensorflow.OpDef.input_arg', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_arg', full_name='tensorflow.OpDef.output_arg', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr', full_name='tensorflow.OpDef.attr', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deprecation', full_name='tensorflow.OpDef.deprecation', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary', full_name='tensorflow.OpDef.summary', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='tensorflow.OpDef.description', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_commutative', full_name='tensorflow.OpDef.is_commutative', index=7,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_aggregate', full_name='tensorflow.OpDef.is_aggregate', index=8,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_stateful', full_name='tensorflow.OpDef.is_stateful', index=9,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allows_uninitialized_input', full_name='tensorflow.OpDef.allows_uninitialized_input', index=10,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OPDEF_ARGDEF, _OPDEF_ATTRDEF, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=834,
)


_OPDEPRECATION = _descriptor.Descriptor(
  name='OpDeprecation',
  full_name='tensorflow.OpDeprecation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorflow.OpDeprecation.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='explanation', full_name='tensorflow.OpDeprecation.explanation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=836,
  serialized_end=889,
)


_OPLIST = _descriptor.Descriptor(
  name='OpList',
  full_name='tensorflow.OpList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='tensorflow.OpList.op', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=891,
  serialized_end=930,
)

_OPDEF_ARGDEF.fields_by_name['type'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_OPDEF_ARGDEF.containing_type = _OPDEF
_OPDEF_ATTRDEF.fields_by_name['default_value'].message_type = tensorflow_dot_core_dot_framework_dot_attr__value__pb2._ATTRVALUE
_OPDEF_ATTRDEF.fields_by_name['allowed_values'].message_type = tensorflow_dot_core_dot_framework_dot_attr__value__pb2._ATTRVALUE
_OPDEF_ATTRDEF.containing_type = _OPDEF
_OPDEF.fields_by_name['input_arg'].message_type = _OPDEF_ARGDEF
_OPDEF.fields_by_name['output_arg'].message_type = _OPDEF_ARGDEF
_OPDEF.fields_by_name['attr'].message_type = _OPDEF_ATTRDEF
_OPDEF.fields_by_name['deprecation'].message_type = _OPDEPRECATION
_OPLIST.fields_by_name['op'].message_type = _OPDEF
DESCRIPTOR.message_types_by_name['OpDef'] = _OPDEF
DESCRIPTOR.message_types_by_name['OpDeprecation'] = _OPDEPRECATION
DESCRIPTOR.message_types_by_name['OpList'] = _OPLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpDef = _reflection.GeneratedProtocolMessageType('OpDef', (_message.Message,), dict(

  ArgDef = _reflection.GeneratedProtocolMessageType('ArgDef', (_message.Message,), dict(
    DESCRIPTOR = _OPDEF_ARGDEF,
    __module__ = 'tensorflow.core.framework.op_def_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.OpDef.ArgDef)
    ))
  ,

  AttrDef = _reflection.GeneratedProtocolMessageType('AttrDef', (_message.Message,), dict(
    DESCRIPTOR = _OPDEF_ATTRDEF,
    __module__ = 'tensorflow.core.framework.op_def_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.OpDef.AttrDef)
    ))
  ,
  DESCRIPTOR = _OPDEF,
  __module__ = 'tensorflow.core.framework.op_def_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.OpDef)
  ))
_sym_db.RegisterMessage(OpDef)
_sym_db.RegisterMessage(OpDef.ArgDef)
_sym_db.RegisterMessage(OpDef.AttrDef)

OpDeprecation = _reflection.GeneratedProtocolMessageType('OpDeprecation', (_message.Message,), dict(
  DESCRIPTOR = _OPDEPRECATION,
  __module__ = 'tensorflow.core.framework.op_def_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.OpDeprecation)
  ))
_sym_db.RegisterMessage(OpDeprecation)

OpList = _reflection.GeneratedProtocolMessageType('OpList', (_message.Message,), dict(
  DESCRIPTOR = _OPLIST,
  __module__ = 'tensorflow.core.framework.op_def_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.OpList)
  ))
_sym_db.RegisterMessage(OpList)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\013OpDefProtosP\001\370\001\001'))
# @@protoc_insertion_point(module_scope)
