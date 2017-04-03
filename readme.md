Command to creat `<name>_pb2.py` files:
```
python -m grpc_tools.protoc -I./protocol --python_out=. --grpc_python_out=. ./protocol/customer.proto

```