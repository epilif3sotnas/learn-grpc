# Run

First of all, it is needed to generate the files for gRPC

```
cd {PATH_REPOSITORY}/client-python
python3 -m grpc_tools.protoc --proto_path=src/proto Hinterface.proto --python_out=src/stubs --grpc_python_out=src/stubs
```

Then you need to run the client

```
cd {PATH_REPOSITORY}/client-python/src
python3 Main.py
```