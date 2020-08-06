"""
Authenticate With Coinbase API

Code snippet mostly from: https://docs.pro.coinbase.com/#authentication
"""

import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase

#Credentials from public coinbase sandbox: https://public.sandbox.pro.coinbase.com
# no need to secure these, they aren't linked to real funds. just a testing     api
API_SECRET = "KCTvny2IXySh8blJwM3fe3RaS9gu03aAVlQqENJFepQhJRQNqdISzZdjqxGwzQpByaqwMr/3FIdeRi8a8FPmZA=="
API_PASS = "password"
API_KEY = "355779993adce0beeae3508b7c06d9ee"

# Create custom authentication for Exchange, we shouldn't have to edit this
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

api_url = 'https://api-public.sandbox.pro.coinbase.com/'
auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)  # import this into any calls that need auth (like trades)
