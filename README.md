# grpc_helloworld
### Test repository to understand gRPC and protobuf

Command to create `<name>_pb2.py` files:
```
python -m grpc_tools.protoc -I./protocol --python_out=. --grpc_python_out=. ./protocol/customer.proto
```

Run the commands:

- Run the server:
   * `python server.py`
- Run the client: 
    * `python client.py`
