import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
import grpc
from flask import Flask
from flask_cors import CORS

# Change this to the port your lightning node is running on: default 10009
LND_PORT = "10009"
# Change this to the path to your tls.cert, but keep /home/<user> format, not ~
PATH_TO_TLS_CERT = '/home/valentine/.lnd/tls.cert'

SERVER_PUBKEY = "03a2102f6978b9e5c6a2dd39697f95b36a7992a60ca65e0316dcd517108e8da171"
SERVER_HOST = "52.53.90.150:9735"
cert = open(PATH_TO_TLS_CERT).read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('localhost:' + LND_PORT, creds)
stub = lnrpc.LightningStub(channel)

# Add server as peer.
listpeers_req = ln.ListPeersRequest()
listpeers_res = stub.ListPeers(listpeers_req)
already_peers = False
for peer in listpeers_res.peers:
    if peer.pub_key == SERVER_PUBKEY:
        already_peers = True
if not already_peers:  
    ln_addr = ln.LightningAddress(pubkey=SERVER_PUBKEY, host=SERVER_HOST)
    req = ln.ConnectPeerRequest(addr=ln_addr)
    res = stub.ConnectPeer(req)

app = Flask(__name__)
CORS(app)

@app.route('/<string:invoice>')
def pay_invoice(invoice):
    send_req = ln.SendRequest(payment_request=invoice)
    sent_payment = stub.SendPaymentSync(send_req)
    if "unable to find a path to destination" in sent_payment.payment_error:
        return sent_payment.payment_error
    return invoice
