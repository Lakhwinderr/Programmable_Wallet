import requests

walletSetId = "018a687d-ac2c-7148-a3b1-b6ecd5cc9b6a"
url = "https://api.circle.com/v1/w3s/walletSets/" + walletSetId

apiKey = "TEST_API_KEY:f957d16d834eb700d2ad81a672ddcb45:1697e1f073a52d9ff872e3008f4679b2"

headers = {
    "accept": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.get(url, headers=headers)

print(response.text)
id = response.json()["data"]["walletSet"]["id"]
# print(id)