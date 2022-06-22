package com.server_java.app;

import java.io.IOException;

import com.server_java.app.grpc.Hinterface.helloWorldRequest;
import com.server_java.app.grpc.Hinterface.helloWorldResponse;
import com.server_java.app.grpc.HelloGrpc;

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