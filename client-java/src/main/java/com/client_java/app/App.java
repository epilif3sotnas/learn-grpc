package com.client_java.app;

import java.util.concurrent.TimeUnit;

import io.grpc.proto.HelloGrpc;
import io.grpc.proto.Hinterface.helloWorldRequest;
import io.grpc.proto.Hinterface.helloWorldResponse;

import io.grpc.Channel;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;

public class App {

    private final HelloGrpc.HelloBlockingStub blockingStub;

    public App (Channel channel) {
        blockingStub = HelloGrpc.newBlockingStub(channel);
    }

    public void helloWorld (String message) {
        helloWorldRequest req = helloWorldRequest.newBuilder().setMessage(message).build();
        helloWorldResponse res;

        try {
            res = blockingStub.helloWorld(req);
            System.out.println(res);
        } catch (StatusRuntimeException ex) {
            ex.printStackTrace();
        }
    }

    public static void main (String[] args) throws InterruptedException {
        ManagedChannel channel = ManagedChannelBuilder
                                    .forAddress("localhost", 5051)
                                    .usePlaintext()
                                    .build();
        
        try {
            App client = new App(channel);
            client.helloWorld("Hello World!");
        } finally {
            channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
        }

    }
}