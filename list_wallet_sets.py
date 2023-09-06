import requests


#update the dates in the url below to get the wallet sets in that time range
url = "https://api.circle.com/v1/w3s/walletSets?from=2023-01-01T12%3A04%3A05Z&to=2024-01-01T12%3A04%3A05Z&pageSize=10"

apiKey = "$ENV_API_KEY:ID:SECRET$"
headers = {
    "accept": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.get(url, headers=headers)

print(response.text)