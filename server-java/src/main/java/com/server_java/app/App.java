package com.server_java.app;

import java.io.IOException;

import io.grpc.proto.Hinterface.helloWorldRequest;
import io.grpc.proto.Hinterface.helloWorldResponse;
import io.grpc.proto.HelloGrpc;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;

public class App {

    static class HelloImpl extends HelloGrpc.HelloImplBase {
        @Override
        public void helloWorld (helloWorldRequest req, StreamObserver<helloWorldResponse> res) {
            System.out.println(req);

            helloWorldResponse response = helloWorldResponse
                .newBuilder()
                .setStatus(true)
                .build();

            res.onNext(response);
            res.onCompleted();
        }
    }
    
    public static void main (String[] args) throws IOException, InterruptedException {
        Server server = ServerBuilder.forPort(5051)
            .addService(new HelloImpl())
            .build();

        System.out.println("Starting server...");
        server.start();
        System.out.println("Server started!");
        server.awaitTermination();
    }
}