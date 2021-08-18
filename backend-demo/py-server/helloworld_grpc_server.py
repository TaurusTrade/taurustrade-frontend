from concurrent import futures
import time
import grpc
import hello_pb2
import hello_pb2_grpc

# 实现 proto 文件中定义的 HelloWorldServiceServicer
class Greeter(hello_pb2_grpc.HelloWorldServiceServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def SayHello(self, request, context):
        return hello_pb2.HelloResponse(message = 'hello {msg}'.format(msg = request.name))


def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloWorldServiceServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
