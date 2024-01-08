# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from apis import apis_pb2 as apis_dot_apis__pb2


class ProfileStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UserInfo = channel.unary_unary(
                '/profile.api.Profile/UserInfo',
                request_serializer=apis_dot_apis__pb2.UserInfoRequest.SerializeToString,
                response_deserializer=apis_dot_apis__pb2.UserInfoResponse.FromString,
                )
        self.BatchUserInfo = channel.unary_unary(
                '/profile.api.Profile/BatchUserInfo',
                request_serializer=apis_dot_apis__pb2.BatchUserInfoRequest.SerializeToString,
                response_deserializer=apis_dot_apis__pb2.BatchUserInfoResponse.FromString,
                )
        self.ActivateUser = channel.unary_unary(
                '/profile.api.Profile/ActivateUser',
                request_serializer=apis_dot_apis__pb2.ActivateUserRequest.SerializeToString,
                response_deserializer=apis_dot_apis__pb2.ActivateUserResponse.FromString,
                )
        self.BatchFollowStatus = channel.unary_unary(
                '/profile.api.Profile/BatchFollowStatus',
                request_serializer=apis_dot_apis__pb2.BatchFollowStatusRequest.SerializeToString,
                response_deserializer=apis_dot_apis__pb2.BatchFollowStatusResponse.FromString,
                )


class ProfileServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UserInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchUserInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActivateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchFollowStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProfileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UserInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UserInfo,
                    request_deserializer=apis_dot_apis__pb2.UserInfoRequest.FromString,
                    response_serializer=apis_dot_apis__pb2.UserInfoResponse.SerializeToString,
            ),
            'BatchUserInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchUserInfo,
                    request_deserializer=apis_dot_apis__pb2.BatchUserInfoRequest.FromString,
                    response_serializer=apis_dot_apis__pb2.BatchUserInfoResponse.SerializeToString,
            ),
            'ActivateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.ActivateUser,
                    request_deserializer=apis_dot_apis__pb2.ActivateUserRequest.FromString,
                    response_serializer=apis_dot_apis__pb2.ActivateUserResponse.SerializeToString,
            ),
            'BatchFollowStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchFollowStatus,
                    request_deserializer=apis_dot_apis__pb2.BatchFollowStatusRequest.FromString,
                    response_serializer=apis_dot_apis__pb2.BatchFollowStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'profile.api.Profile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Profile(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UserInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/profile.api.Profile/UserInfo',
            apis_dot_apis__pb2.UserInfoRequest.SerializeToString,
            apis_dot_apis__pb2.UserInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchUserInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/profile.api.Profile/BatchUserInfo',
            apis_dot_apis__pb2.BatchUserInfoRequest.SerializeToString,
            apis_dot_apis__pb2.BatchUserInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActivateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/profile.api.Profile/ActivateUser',
            apis_dot_apis__pb2.ActivateUserRequest.SerializeToString,
            apis_dot_apis__pb2.ActivateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchFollowStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/profile.api.Profile/BatchFollowStatus',
            apis_dot_apis__pb2.BatchFollowStatusRequest.SerializeToString,
            apis_dot_apis__pb2.BatchFollowStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
