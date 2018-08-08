# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workflow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='workflow.proto',
  package='workflow',
  syntax='proto3',
  serialized_pb=_b('\n\x0eworkflow.proto\x12\x08workflow\"\xa7\x01\n\x08Workflow\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x14\n\x0c\x66\x61\x63tory_name\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12&\n\x05state\x18\x04 \x01(\x0e\x32\x17.workflow.WorkflowState\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x12\r\n\x05\x65rror\x18\x06 \x01(\t\x12\x12\n\nstart_time\x18\x07 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x03\"\x8f\x02\n\x12WorkflowCheckpoint\x12\x14\n\x0c\x63ode_version\x18\x01 \x01(\x05\x12\x36\n\x05tasks\x18\x02 \x03(\x0b\x32\'.workflow.WorkflowCheckpoint.TasksEntry\x12<\n\x08settings\x18\x03 \x03(\x0b\x32*.workflow.WorkflowCheckpoint.SettingsEntry\x1a<\n\nTasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.workflow.Task:\x02\x38\x01\x1a/\n\rSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xac\x01\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x05state\x18\x02 \x01(\x0e\x32\x13.workflow.TaskState\x12\x32\n\nattributes\x18\x03 \x03(\x0b\x32\x1e.workflow.Task.AttributesEntry\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*6\n\rWorkflowState\x12\x0e\n\nNotStarted\x10\x00\x12\x0b\n\x07Running\x10\x01\x12\x08\n\x04\x44one\x10\x02*>\n\tTaskState\x12\x12\n\x0eTaskNotStarted\x10\x00\x12\x0f\n\x0bTaskRunning\x10\x01\x12\x0c\n\x08TaskDone\x10\x02\x62\x06proto3')
)

_WORKFLOWSTATE = _descriptor.EnumDescriptor(
  name='WorkflowState',
  full_name='workflow.WorkflowState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NotStarted', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Running', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Done', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=647,
  serialized_end=701,
)
_sym_db.RegisterEnumDescriptor(_WORKFLOWSTATE)

WorkflowState = enum_type_wrapper.EnumTypeWrapper(_WORKFLOWSTATE)
_TASKSTATE = _descriptor.EnumDescriptor(
  name='TaskState',
  full_name='workflow.TaskState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TaskNotStarted', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TaskRunning', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TaskDone', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=703,
  serialized_end=765,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATE)

TaskState = enum_type_wrapper.EnumTypeWrapper(_TASKSTATE)
NotStarted = 0
Running = 1
Done = 2
TaskNotStarted = 0
TaskRunning = 1
TaskDone = 2



_WORKFLOW = _descriptor.Descriptor(
  name='Workflow',
  full_name='workflow.Workflow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='workflow.Workflow.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='factory_name', full_name='workflow.Workflow.factory_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='workflow.Workflow.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='workflow.Workflow.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workflow.Workflow.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workflow.Workflow.error', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='workflow.Workflow.start_time', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='workflow.Workflow.end_time', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=29,
  serialized_end=196,
)


_WORKFLOWCHECKPOINT_TASKSENTRY = _descriptor.Descriptor(
  name='TasksEntry',
  full_name='workflow.WorkflowCheckpoint.TasksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='workflow.WorkflowCheckpoint.TasksEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='workflow.WorkflowCheckpoint.TasksEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=421,
)

_WORKFLOWCHECKPOINT_SETTINGSENTRY = _descriptor.Descriptor(
  name='SettingsEntry',
  full_name='workflow.WorkflowCheckpoint.SettingsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='workflow.WorkflowCheckpoint.SettingsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='workflow.WorkflowCheckpoint.SettingsEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=470,
)

_WORKFLOWCHECKPOINT = _descriptor.Descriptor(
  name='WorkflowCheckpoint',
  full_name='workflow.WorkflowCheckpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code_version', full_name='workflow.WorkflowCheckpoint.code_version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='workflow.WorkflowCheckpoint.tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='workflow.WorkflowCheckpoint.settings', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORKFLOWCHECKPOINT_TASKSENTRY, _WORKFLOWCHECKPOINT_SETTINGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=470,
)


_TASK_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='workflow.Task.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='workflow.Task.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='workflow.Task.AttributesEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=596,
  serialized_end=645,
)

_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='workflow.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='workflow.Task.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='workflow.Task.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='workflow.Task.attributes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workflow.Task.error', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASK_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=645,
)

_WORKFLOW.fields_by_name['state'].enum_type = _WORKFLOWSTATE
_WORKFLOWCHECKPOINT_TASKSENTRY.fields_by_name['value'].message_type = _TASK
_WORKFLOWCHECKPOINT_TASKSENTRY.containing_type = _WORKFLOWCHECKPOINT
_WORKFLOWCHECKPOINT_SETTINGSENTRY.containing_type = _WORKFLOWCHECKPOINT
_WORKFLOWCHECKPOINT.fields_by_name['tasks'].message_type = _WORKFLOWCHECKPOINT_TASKSENTRY
_WORKFLOWCHECKPOINT.fields_by_name['settings'].message_type = _WORKFLOWCHECKPOINT_SETTINGSENTRY
_TASK_ATTRIBUTESENTRY.containing_type = _TASK
_TASK.fields_by_name['state'].enum_type = _TASKSTATE
_TASK.fields_by_name['attributes'].message_type = _TASK_ATTRIBUTESENTRY
DESCRIPTOR.message_types_by_name['Workflow'] = _WORKFLOW
DESCRIPTOR.message_types_by_name['WorkflowCheckpoint'] = _WORKFLOWCHECKPOINT
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.enum_types_by_name['WorkflowState'] = _WORKFLOWSTATE
DESCRIPTOR.enum_types_by_name['TaskState'] = _TASKSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Workflow = _reflection.GeneratedProtocolMessageType('Workflow', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOW,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Workflow)
  ))
_sym_db.RegisterMessage(Workflow)

WorkflowCheckpoint = _reflection.GeneratedProtocolMessageType('WorkflowCheckpoint', (_message.Message,), dict(

  TasksEntry = _reflection.GeneratedProtocolMessageType('TasksEntry', (_message.Message,), dict(
    DESCRIPTOR = _WORKFLOWCHECKPOINT_TASKSENTRY,
    __module__ = 'workflow_pb2'
    # @@protoc_insertion_point(class_scope:workflow.WorkflowCheckpoint.TasksEntry)
    ))
  ,

  SettingsEntry = _reflection.GeneratedProtocolMessageType('SettingsEntry', (_message.Message,), dict(
    DESCRIPTOR = _WORKFLOWCHECKPOINT_SETTINGSENTRY,
    __module__ = 'workflow_pb2'
    # @@protoc_insertion_point(class_scope:workflow.WorkflowCheckpoint.SettingsEntry)
    ))
  ,
  DESCRIPTOR = _WORKFLOWCHECKPOINT,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.WorkflowCheckpoint)
  ))
_sym_db.RegisterMessage(WorkflowCheckpoint)
_sym_db.RegisterMessage(WorkflowCheckpoint.TasksEntry)
_sym_db.RegisterMessage(WorkflowCheckpoint.SettingsEntry)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _TASK_ATTRIBUTESENTRY,
    __module__ = 'workflow_pb2'
    # @@protoc_insertion_point(class_scope:workflow.Task.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _TASK,
  __module__ = 'workflow_pb2'
  # @@protoc_insertion_point(class_scope:workflow.Task)
  ))
_sym_db.RegisterMessage(Task)
_sym_db.RegisterMessage(Task.AttributesEntry)


_WORKFLOWCHECKPOINT_TASKSENTRY.has_options = True
_WORKFLOWCHECKPOINT_TASKSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_WORKFLOWCHECKPOINT_SETTINGSENTRY.has_options = True
_WORKFLOWCHECKPOINT_SETTINGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_TASK_ATTRIBUTESENTRY.has_options = True
_TASK_ATTRIBUTESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
