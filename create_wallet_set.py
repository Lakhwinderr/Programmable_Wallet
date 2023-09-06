import requests
import uuid_1
import generate_entity_secret_ciphertext
url = "https://api.circle.com/v1/w3s/developer/walletSets"

esc = generate_entity_secret_ciphertext.esc
uuid = uuid_1.uuid
apiKey = "$ENV_API_KEY:ID:SECRET$"
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