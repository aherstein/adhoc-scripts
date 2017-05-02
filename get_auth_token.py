#!/usr/bin/python

import os
import requests
import base64
import argparse

# Parse args
parser = argparse.ArgumentParser(description='Get auth token')
parser.add_argument('--key', type=str, required=True, help='Client key')
parser.add_argument('--secret', type=str, required=True, help='Client secret')
args = parser.parse_args()

# Check auth uri
if 'AUTH_URI' not in os.environ or os.environ['AUTH_URI'] == '':
    os.environ['AUTH_URI'] = 'https://api.compligo.com/v1/auth/client'

# Get auth
basic_auth = args.key + ':' + args.secret
auth = requests.post(os.environ['AUTH_URI'], timeout=2, headers={
    "Authorization": 'Basic: ' + base64.b64encode(basic_auth),
    "Content-Type": "application/x-www-form-urlencoded"
})
token = auth.text
print(token)
