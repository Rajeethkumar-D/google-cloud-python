# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/firestore_v1beta1/proto/event_flow_document_change.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.firestore_v1beta1.proto import common_pb2 as google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_common__pb2
from google.cloud.firestore_v1beta1.proto import document_pb2 as google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/firestore_v1beta1/proto/event_flow_document_change.proto',
  package='google.firestore.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\nEgoogle/cloud/firestore_v1beta1/proto/event_flow_document_change.proto\x12\x18google.firestore.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x31google/cloud/firestore_v1beta1/proto/common.proto\x1a\x33google/cloud/firestore_v1beta1/proto/document.protoB\xa2\x01\n\x1c\x63om.google.firestore.v1beta1B\x1c\x45ventFlowDocumentChangeProtoP\x01ZAgoogle.golang.org/genproto/googleapis/firestore/v1beta1;firestore\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_common__pb2.DESCRIPTOR,google_dot_cloud_dot_firestore__v1beta1_dot_proto_dot_document__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.google.firestore.v1beta1B\034EventFlowDocumentChangeProtoP\001ZAgoogle.golang.org/genproto/googleapis/firestore/v1beta1;firestore\252\002\036Google.Cloud.Firestore.V1Beta1'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)