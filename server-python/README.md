## Run

Commands to run the project:

```
cd {PATH_REPOSITORY}/server-python;
python3 -m grpc_tools.protoc --proto_path=src/proto Hinterface.proto --python_out=src/stubs --grpc_python_out=src/stubs;
pipenv install;
pipenv run start;
```
