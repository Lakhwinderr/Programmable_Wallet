import requests
id = "0aec90eb-40d9-4a71-b0d4-c34a70563d1b"
url = "https://api.circle.com/v1/w3s/wallets/" + id

apiKey = "$ENV_API_KEY:ID:SECRET$"
headers = {
    "accept": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.get(url, headers=headers)

print(response.text)