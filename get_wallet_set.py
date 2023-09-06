import requests

walletSetId = "018a687d-ac2c-7148-a3b1-b6ecd5cc9b6a"
url = "https://api.circle.com/v1/w3s/walletSets/" + walletSetId

apiKey = "$ENV_API_KEY:ID:SECRET$"
headers = {
    "accept": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.get(url, headers=headers)

print(response.text)
id = response.json()["data"]["walletSet"]["id"]
# print(id)