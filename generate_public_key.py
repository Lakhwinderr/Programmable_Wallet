import requests

url = "https://api.circle.com/v1/w3s/config/entity/publicKey"
# paste your api key here
apiKey = "$ENV_API_KEY:ID:SECRET$"
headers = {
    "accept": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.get(url, headers=headers)

print(response.status_code)

key = response.json()["data"]['publicKey']


