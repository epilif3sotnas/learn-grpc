import grpc
# improve -> import from stubs
import Hinterface_pb2
import Hinterface_pb2_grpc

from concurrent import futures

class Hello (Hinterface_pb2_grpc.HelloServicer):

    def helloWorld (self, request, context):
        print(request)
        return Hinterface_pb2.helloWorldResponse(status = True)

def server ():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Hinterface_pb2_grpc.add_HelloServicer_to_server(Hello(), server)
    server.add_insecure_port('[::]:5050')
    print("Server starting...")
    server.start()
    print("Server started!")
    server.wait_for_termination()

if __name__ == "__main__":
    server()