########################################################################################################################
#                                           Jelastic - Sample Script - GetEnv                                          #
# -------------------------------------------------------------------------------------------------------------------- #
#                                                                                                                      #
# INTRODUCTION:                                                                                                        #
#   This script is a sample script to start you off with communicating to a Jelastic region.                           #
#   The script requires that you have created an API token in the Jelastic UI, as you will need to provide it in       #
#   the variables section.                                                                                             #
#                                                                                                                      #
# -------------------------------------------------------------------------------------------------------------------- #
#                                                                                                                      #
# DETAILS:                                                                                                             #
#   This script will connect, using the python REST API, and pull your environment details.                            #
#                                                                                                                      #
# -------------------------------------------------------------------------------------------------------------------- #
#                                                                                                                      #
# CHANGELOG                                                                                                            #
# v1.0 - 14 August 2020 (Richard Raymond)                                                                              #
#   - Initial version                                                                                                  #
#                                                                                                                      #
########################################################################################################################
import requests  # Required for RESTful comms
import json  # Required for Jelastic restful responses

# VARIABLES
jelastic_region_url = 'https://app.demo.jelastic.com/1.0'
jelastic_region_api_token = '2ddce07e785d4e9fb3e395cce53f0dac248e16d3'
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
