use std::thread;

use server_rust::Hinterface::*;
use server_rust::Hinterface_grpc::*;

use grpc::ServerRequestSingle;
use grpc::ServerResponseUnarySink;
use grpc::ServerHandlerContext;

pub struct HelloImpl;

impl Hello for HelloImpl {

    fn hello_world (&self, o: ServerHandlerContext<>, req: ServerRequestSingle<helloWorldRequest>, 
        res: ServerResponseUnarySink<helloWorldResponse>) -> grpc::Result<()> {
        
        println!("{:?}", req.message);
        let mut r = helloWorldResponse::new();
        r.set_status(true);
        res.finish(r);
        Ok(())
    }
}

fn main () {
    let mut server = grpc::ServerBuilder::new_plain();
    server.http.set_port(5053);
    server.add_service(HelloServer::new_service_def(HelloImpl));

    println!("Starting server...");
    let _server = server.build().expect("Server");
    println!("Server started!");

    loop {
        thread::park();
    }
}