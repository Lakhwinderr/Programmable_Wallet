import requests
#replace the walletSetId to list the wallets of that wallet set.
walletSetId ="018a687d-ac2c-7148-a3b1-b6ecd5cc9b6a&pageSize=10"
url = "https://api.circle.com/v1/w3s/wallets?walletSetId=" + walletSetId

apiKey = "$ENV_API_KEY:ID:SECRET$"

headers = {
    "accept": "application/json",
    "authorization": "Bearer " + apiKey
}
response = requests.get(url, headers=headers)

print(response.text)

# for wallet in response.json()["data"]["wallets"]:
#     print(wallet["id"])