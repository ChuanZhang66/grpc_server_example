import time
from concurrent import futures

import grpc

from apis import apis_rs_pb2 as apis_pb2
from apis import apis_rs_pb2_grpc as apis_pb2_grpc


class TestServicer(apis_pb2_grpc.TestServiceServicer):
    def TestFunc(self, request, context):
        request = getattr(apis_pb2, "TestFuncRequest")(id=1, name="2")
        response = getattr(apis_pb2, "TestFuncResponse")(id=request.id, name=request.name)
        return response


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    apis_pb2_grpc.add_TestServiceServicer_to_server(TestServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print('waiting to be requested.')
    serve()
