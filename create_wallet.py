

import generate_entity_secret_ciphertext
import get_wallet_set
import uuid_1
idempotencyKey = uuid_1.uuid
blockchains = ["MATIC-MUMBAI"]
count = 1 
entitySecretCiphertext =  generate_entity_secret_ciphertext.esc
walletSetId = get_wallet_set.id

import requests

url = "https://api.circle.com/v1/w3s/developer/wallets"

payload = {
    "count": count,
    "blockchains": blockchains,
    "entitySecretCiphertext": entitySecretCiphertext,
    "walletSetId": walletSetId,
    "idempotencyKey": idempotencyKey
}
apiKey = "TEST_API_KEY:f957d16d834eb700d2ad81a672ddcb45:1697e1f073a52d9ff872e3008f4679b2"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.post(url, json=payload, headers=headers)
print("\n")
print(response.status_code)
print(response.text)