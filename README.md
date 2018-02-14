# Installation
Before beginning, ensure that you are running Python 2.7 and that you have pip and virtualenv installed.

```
git clone https://github.com/valentinewallace/litstream_client.git 
cd litstream_client
virtualenv deskenv
source deskenv/bin/activate
```

Edit lines 7 and 9 of `client.py` to contain the correct `LND_PORT` for your node, and the correct `PATH_TO_TLS_CERT` for the path to your tls.cert file. 

Install the dependencies required for Python gRPC:

`pip install grpcio grpcio-tools googleapis-common-protos`

Install the dependencies required for litstream:

`pip install flask flask-cors`

Clone the Google API repository, which is required due to the use of google/api/annotations.proto:

`git clone https://github.com/googleapis/googleapis.git`

Download the lnd rpc.proto file:

`curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/rpc.proto`

Compile the proto file:

`python -m grpc_tools.protoc --proto_path=googleapis:. --python_out=. --grpc_python_out=. rpc.proto`

Set the FLASK_APP environment variable and run the server:

```
export FLASK_APP=client.py
flask run --host=0.0.0.0
```

Now you should be able to visit http://ec2-52-53-90-150.us-west-1.compute.amazonaws.com/ and watch vids for testnet $$ :)
