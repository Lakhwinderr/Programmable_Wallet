import requests
import uuid_1
import generate_entity_secret_ciphertext
url = "https://api.circle.com/v1/w3s/developer/walletSets"

esc = generate_entity_secret_ciphertext.esc
uuid = uuid_1.uuid
apiKey = "TEST_API_KEY:f957d16d834eb700d2ad81a672ddcb45:1697e1f073a52d9ff872e3008f4679b2"
payload = {
    "idempotencyKey": uuid,
    "entitySecretCiphertext": esc
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)