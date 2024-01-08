import json
import time
import grpc
from concurrent import futures

from apis import apis_rs_pb2 as apis_pb2
from apis import apis_rs_pb2_grpc as apis_pb2_grpc


class ProfileServicer(apis_pb2_grpc.ProfileServicer):
    def UserInfo(self, request, context):
        response = apis_pb2.UserInfoResponse(user_id=1, username=2)
        return response

    def BatchUserInfo(self, request, context):
        response = apis_pb2.BatchUserInfoResponse
        return response(response=json.dumps({}))

    def BatchFollowStatus(self, request, context):
        response = apis_pb2.BatchFollowStatusResponse
        return response(response=json.dumps({}))

    def ActivateUser(self, request, context):
        Response = apis_pb2.ActivateUserResponse
        return Response(result="f", message="")

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    apis_pb2_grpc.add_ProfileServicer_to_server(ProfileServicer(), server)
    server.add_insecure_port('[::]:50056')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print('waiting to be requested.')
    serve()
