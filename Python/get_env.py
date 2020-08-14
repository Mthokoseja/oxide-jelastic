import requests  # Required for RESTful comms
import json  # Required for Jelastic restful responses

# VARIABLES
jelastic_region_url = 'https://app.demo.jelastic.com/1.0'
jelastic_region_api_token = 'api_token'
jelastic_appid = '1dd8d191d38fff45e62564fcf67fdcd6'

# REST - QUERIES
rest_getenv_url = "{}/environment/control/rest/getenvs?session={}&appid={}".format(
    jelastic_region_url,
    jelastic_region_api_token,
    jelastic_appid
)

payload = {}
headers = {

}

# Handles response and convert to a parse-able json object
response = json.loads(requests.request("GET", rest_getenv_url, headers=headers, data=payload).text.encode('utf8'))

# Output the string to console
print(json.dumps(response, indent=4, sort_keys=True))
