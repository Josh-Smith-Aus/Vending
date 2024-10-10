import requests
import json
import tokens
import requests

headers = {
    'Authorization': 'Bearer ' + tokens.UP_API_key,
}

response = requests.get(
    'https://api.up.com.au/api/v1/transactions?page[size]=1&filter[status]=SETTLED',
    headers=headers,
)

data = json.loads(response.text)
# add indentation
#json_object = json.dumps(data)#, indent=10)

with open("record.json", "w") as outfile:
    json.dump(data, outfile)