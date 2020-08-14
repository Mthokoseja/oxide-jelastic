import requests  # Required for RESTful comms
import json  # Required for Jelastic restful responses

# VARIABLES
jelastic_region_url = 'https://app.demo.jelastic.com/1.0'
jelastic_region_api_token = 'your_api_token_you_made_when_logged_in'
jelastic_appid = '1dd8d191d38fff45e62564fcf67fdcd6'

# REST - QUERIES
rest_getenv_url = ("{}/environment/control/rest/getenvs?session={}&appid={}").format(
    jelastic_region_url,
    jelastic_region_api_token,
    jelastic_appid
)

payload = {}
headers = {
    'Authorization': 'Bearer 2ddce07e785d4e9fb3e395cce53f0dac248e16d3',
    'Cookie': 'jrouter=b916bf4d3b39e6029fd403f21566f3f1'
}

# Handles response and convert to a parse-able json object
response = json.loads(requests.request("GET", rest_getenv_url, headers=headers, data=payload).text.encode('utf8'))

# Output the string to console
print(json.dumps(response, indent=4, sort_keys=True))
