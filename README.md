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
