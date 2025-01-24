from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load sensitive data from config.json
with open("config.json", "r") as f:
    config = json.load(f)

# Helper to load conditions
def load_conditions(filename="conditions.json"):
    with open(filename, "r") as file:
        return json.load(file)

# Helper to save transactions
def save_to_json_file(data, filename="transactions.json"):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file)
    with open(filename, "r") as file:
        existing_data = json.load(file)
    existing_data.append(data)
    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)

# Check if a transaction matches conditions
def check_conditions(transaction, conditions):
    for condition in conditions:
        if transaction["description"] == condition["description"] and transaction["amount"] == condition["amount"]:
            return True
    return False

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if not data:
        return jsonify({"message": "Invalid data"}), 400

    # Parse transaction details
    transaction = {
        "description": data["data"]["attributes"]["description"],
        "amount": float(data["data"]["attributes"]["amount"]["value"]),
        "timestamp": data["data"]["attributes"]["createdAt"]
    }

    # Check against conditions
    conditions = load_conditions()
    if check_conditions(transaction, conditions):
        save_to_json_file(transaction)
        return jsonify({"message": "Transaction matched and saved"}), 200
    else:
        return jsonify({"message": "No match"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
