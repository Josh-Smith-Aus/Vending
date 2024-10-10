import tokens
import requests


UP_api_token = tokens.UP_API_key


headers = {
    'Authorization': 'Bearer '+ UP_api_token,
}

response = requests.get('https://api.up.com.au/api/v1/accounts?page[size]=1', headers=headers)


data = response.json()
print(data.get('data').get('companyName'))