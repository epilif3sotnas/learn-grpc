import grpc
import stubs.Hinterface_pb2 as Hinterface_pb2
import stubs.Hinterface_pb2_grpc as Hinterface_pb2_grpc

def main():
    with grpc.insecure_channel('localhost:5050') as channel:
        stub = Hinterface_pb2_grpc.HelloStub(channel)
        response = stub.helloWorld(Hinterface_pb2.helloWorldRequest(message = 'Hello World!'))
    print(response)

if __name__ == '__main__':
    main()