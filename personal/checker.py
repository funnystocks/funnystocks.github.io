# checker.py - How to interact with the ebay api (AI generated most of this for me)
# Edited by funnystocks (https://github.com/funnystocks)
# No restrictions on usage - this is released into the public domain - 6/2025
# THIS DOES NOT PERSIST EBAY DATA
import os
import requests
import base64
import json
from dotenv import load_dotenv
load_dotenv()
def grab_token():
    username = os.getenv("EBAY_APP_ID")
    password = os.getenv("EBAY_CERT_ID")
    token_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {base64.b64encode(str(username + ":" + password).encode('utf-8')).decode('utf-8')}"
    }
    token_payload = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    response = requests.post("https://api.ebay.com/identity/v1/oauth2/token", headers=token_headers, data=token_payload)
    token_data = response.json()
    access_token = token_data.get('access_token')
    return access_token
headers = {
    "Authorization": f"Bearer {grab_token()}",
    "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
    "Content-Type": "application/json",
    "Accept": "application/json"
}
params = {
    "q": "laptop",
    "limit": 5
}
response = requests.get("https://api.ebay.com/buy/browse/v1/item_summary/search", headers=headers, params=params)
results = response.json()
print(json.dumps(results))