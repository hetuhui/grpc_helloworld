# grpc_helloworld
### Test repository to understand gRPC and protobuf
(_NOTE: This is not a full fledged working example, the POST data equivalent works. Data Querying-One related to Streaming hasn't been implemented properly and may not be updated further. This project was just an exercise to understand protobuf and grpc._)

Command to create `<name>_pb2.py` files:
```
python -m grpc_tools.protoc -I./protocol --python_out=. --grpc_python_out=. ./protocol/customer.proto
```

Run the commands:

- Run the server:
   * `python server.py`
- Run the client: 
    * `python client.py`
