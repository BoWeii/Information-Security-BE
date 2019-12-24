from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5 as Signature_PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import urllib.parse
import base64
import json
from hashlib import sha256

KEY = RSA.generate(1024, e=65537)
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
PUBLIC_KEY = KEY.publickey().exportKey("PEM")


# PRIVATE_KEY = KEY.exportKey().decode()


def verify(data):
    try:
        signature = base64.b64decode(data['signature'])
        del data['signature']
        data_str = json.dumps(data) + ""
        data_str = data_str.encode()
        #  print(data_str)
        signer = Signature_PKCS1_v1_5.new(key_pub)
        digest = SHA256.new()
        digest.update(data_str)
        return signer.verify(digest, signature)
    except:
        return False


def sign_test():
    '''parsed_data = []
       for key, value in data.items():
           parsed_data.append('{}={}'.format(key, value))

       parsed_str = '&'.join(parsed_data)'''

    data = {'msg': 'thisisamessage'}
    data_str = json.dumps(data)
    data_str = data_str.encode()
    signer = Signature_PKCS1_v1_5.new(key_pri)
    digest = SHA256.new()
    digest.update(data_str)
    signature = base64.b64encode(signer.sign(digest))
    data['signature'] = signature
    print(verify(data))


if __name__ == '__main__':
    sign_test()
