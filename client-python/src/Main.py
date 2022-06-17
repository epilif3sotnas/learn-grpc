import grpc
# improve -> import from stubs
import Hinterface_pb2
import Hinterface_pb2_grpc

def main():
    with grpc.insecure_channel('localhost:5050') as channel:
        stub = Hinterface_pb2_grpc.HelloStub(channel)
        response = stub.helloWorld(Hinterface_pb2.helloWorldRequest(message = 'Hello World!'))
    print("Status: " + str(response.status))


if __name__ == '__main__':
    main()