# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Hinterface_pb2 as Hinterface__pb2


class HelloStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.helloWorld = channel.unary_unary(
                '/hello.Hello/helloWorld',
                request_serializer=Hinterface__pb2.helloWorldRequest.SerializeToString,
                response_deserializer=Hinterface__pb2.helloWorldResponse.FromString,
                )


class HelloServicer(object):
    """Missing associated documentation comment in .proto file."""

    def helloWorld(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'helloWorld': grpc.unary_unary_rpc_method_handler(
                    servicer.helloWorld,
                    request_deserializer=Hinterface__pb2.helloWorldRequest.FromString,
                    response_serializer=Hinterface__pb2.helloWorldResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.Hello', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hello(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def helloWorld(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.Hello/helloWorld',
            Hinterface__pb2.helloWorldRequest.SerializeToString,
            Hinterface__pb2.helloWorldResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
