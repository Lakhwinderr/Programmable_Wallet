import requests
id = "0aec90eb-40d9-4a71-b0d4-c34a70563d1b"
url = "https://api.circle.com/v1/w3s/wallets/" + id

apiKey = "TEST_API_KEY:f957d16d834eb700d2ad81a672ddcb45:1697e1f073a52d9ff872e3008f4679b2"

headers = {
    "accept": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.get(url, headers=headers)

print(response.text)