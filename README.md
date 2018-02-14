# About

Litstream is meant to be an example of what online video monetization would look like with lightning network + streaming payments. The website is hosted at 
http://ec2-52-53-90-150.us-west-1.compute.amazonaws.com/ and clients are required to be running a server connected to their lnd node in order to watch videos. 

*NOTE:* requires a payment path between your node and 03a2102f6978b9e5c6a2dd39697f95b36a7992a60ca65e0316dcd517108e8da171@52.53.90.150:9735 so you may need to create a channel on your end.

*NOTE 2:*: lnd node must be running with macaroons disabled, soz! 

# Installation
Before beginning, ensure that you are running Python 2.7 and that you have pip and virtualenv installed.

```
git clone https://github.com/valentinewallace/litstream_client.git 
cd litstream_client
virtualenv deskenv
source deskenv/bin/activate
```

Next, **edit lines 7 and 9** of `client.py` to contain the correct `LND_PORT` for your node, and the correct `PATH_TO_TLS_CERT` for the path to your tls.cert file. 

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
