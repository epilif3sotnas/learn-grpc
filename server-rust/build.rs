fn main () {
    protoc_rust_grpc::Codegen::new()
        .out_dir("src/proto")
        .input("src/proto/Hinterface.proto")
        .rust_protobuf(true)
        .run()
        .expect("protoc-rust-grpc");
}