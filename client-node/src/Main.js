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

function main () {
    var client = new hello_proto.Hello('localhost:5052', grpc.credentials.createInsecure());
    client.helloWorld({message: 'Hello World!'}, function (err, res) {
        console.log(res);
    });
}

main();