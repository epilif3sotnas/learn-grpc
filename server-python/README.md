# Run

First of all, it is needed to generate the files for gRPC

```
cd {PATH_REPOSITORY}/server-python
python3 -m grpc_tools.protoc --proto_path=src/proto Hinterface.proto --python_out=src/stubs --grpc_python_out=src/stubs
```

Then you need to run the server

```
cd {PATH_REPOSITORY}/server-python
pipenv run start
```