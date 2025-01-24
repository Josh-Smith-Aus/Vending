import requests
import json

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

def setup_webhook():
    url = "https://api.up.com.au/api/v1/webhooks"
    headers = {
        "Authorization": f"Bearer {config['up_api_token']}",
        "Content-Type": "application/json"
    }
    payload = {
        "data": {
            "attributes": {
                "url": config["ngrok_url"] + "/webhook",
                "description": "Raspberry Pi Webhook"
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("Webhook created successfully!")
    else:
        print(f"Failed to create webhook: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    setup_webhook()
