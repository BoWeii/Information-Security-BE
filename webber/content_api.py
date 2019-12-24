from rest_framework import views, response
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_PKCS1_v1_5
import json
import base64
import rsa
from rest_framework.permissions import IsAuthenticated

pub = '''-----BEGIN PUBLIC KEY-----
MFswDQYJKoZIhvcNAQEBBQADSgAwRwJAYn8taNMlCb/ZvyI9kVqLfp+2yLFPihNU
3qR028hT9jMfphd35MN+dqochu8hwRZghGvWf7lgsDdhKo8TYJ/LzQIDAQAB
-----END PUBLIC KEY-----'''
pri = '''-----BEGIN RSA PRIVATE KEY-----
MIIBOgIBAAJAYn8taNMlCb/ZvyI9kVqLfp+2yLFPihNU3qR028hT9jMfphd35MN+
dqochu8hwRZghGvWf7lgsDdhKo8TYJ/LzQIDAQABAkAcAP6fJBEOwY4eKpUIo46v
lKc6TjdIEZD6sBVNe5prj+cWGXYSI061NnxyaolWHM4wRPnlr5xvsRkNih0kMIlh
AiEAxOjFLWchDlsnCKKhTDesBXHAx77I4+WjLMBkBQNvMXkCIQCADgfrSNgFu4O2
4TMBUHOLBW9p/9t6j7on0iutwq9L9QIhAIbyR3+QN/VQvvWKDyTe2oN4q/e4ZpDY
5fVbfLB65A9xAiAKsCEdFEFjiRkfRICbVXmvWs7HzCEng6OH+1TF9f/nmQIhAIyU
m7cJD3rIjQTEjq+prh5ghXJFPl4e/ivw71ahBqnU
-----END RSA PRIVATE KEY-----'''

# pub = pub.encode('utf-8')
key_pub = RSA.importKey(pub)
key_pri = RSA.importKey(pri)


class SignApiView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        print("data = ", data)
        result = verify(data)
        if result:
            return response.Response('successsssss')
        return response.Response('faileddddd')


def verify(data):
    try:
        signature = base64.b64decode(data['signature'])
        print("signature= ", signature)
        del data['signature']
        data_str = json.dumps(data).encode('utf-8')
        signer = Signature_PKCS1_v1_5.new(key_pub)
        digest = SHA.new()
        digest.update(data_str)
        print(type(signature))
        return signer.verify(digest, signature)
    except:
        return False
