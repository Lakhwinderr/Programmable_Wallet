import requests


#update the dates in the url below to get the wallet sets in that time range
url = "https://api.circle.com/v1/w3s/walletSets?from=2023-01-01T12%3A04%3A05Z&to=2024-01-01T12%3A04%3A05Z&pageSize=10"

apiKey = "TEST_API_KEY:f957d16d834eb700d2ad81a672ddcb45:1697e1f073a52d9ff872e3008f4679b2"

headers = {
    "accept": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.get(url, headers=headers)

print(response.text)