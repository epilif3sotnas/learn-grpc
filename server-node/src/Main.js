var PROTO_PATH = __dirname + '/proto/Hinterface.proto';

var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');

var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    }
);

var hello_proto = grpc.loadPackageDefinition(packageDefinition).hello;

function helloWorld (call, callback) {
    console.log(call.request);
    callback(null, {status: true});
}

function main () {
    var server = new grpc.Server();
    server.addService(hello_proto.Hello.service, {helloWorld: helloWorld});
    server.bindAsync('localhost:5052', grpc.ServerCredentials.createInsecure(), () => {
        console.log("Server starting...");
        server.start();
        console.log("Server started!");
    });
}

main()