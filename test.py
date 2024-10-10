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


#use format below to get data  needed
print(data["data"][0]["attributes"]["amount"]["value"])

# add indentation
json_object = json.dumps(data, indent=1)

with open("record.json", "w") as outfile:
    json.dump(json_object, outfile)