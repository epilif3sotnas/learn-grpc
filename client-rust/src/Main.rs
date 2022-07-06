use client_rust::Hinterface::*;
use client_rust::Hinterface_grpc::*;

use grpc::ClientStub;
use grpc::ClientStubExt;

use futures::executor;

fn main() {
    let config = Default::default();
    let client = HelloClient::new_plain("::1", 5053, config).unwrap();

    let mut req = helloWorldRequest::new();
    req.set_message("Hello world!".to_string());

    let res = client.hello_world(grpc::RequestOptions::new(), req)
                    .join_metadata_result();

    // This prints the metadata and should only print status: true
    println!("{:?}", executor::block_on(res));
}
