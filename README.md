# LoTR SDK

## Dependencies
requests, json

## Installing
- install python 3 from python.org
- pip install requests
- pip install json
- python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps lotr_sdk_aastimson

## Use
- import lotr_sdk_aastimson
- api_token = "token from registering at https://the-one-api.dev"
- lotr = LotrSdk(api_token)
- lotr.book()

## Testing
- clone the GitHub source code
- edit lotr_sdk_aastimson.py and set api_token to yours from the-one-api.dev
- run lotr_sdk_aastimson.py