import tokens
import requests


UP_api_token = tokens.UP_API_key


headers = {
    'Authorization': 'Bearer ' + UP_api_token,
}

response = requests.get('https://api.up.com.au/api/v1/util/ping', headers=headers)
