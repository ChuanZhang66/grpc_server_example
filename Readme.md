## Install packages.
```bash
pip install -r requirements.txt
```

## Generate grpc files.
```bash
python -m grpc_tools.protoc -I apis=./apis --python_out=. --grpc_python_out=. ./apis/apis_rs.proto
```

## Run server.
```bash
python main.py
```
