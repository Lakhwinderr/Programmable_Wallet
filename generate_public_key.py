import requests

url = "https://api.circle.com/v1/w3s/config/entity/publicKey"
# paste your api key here
apiKey = "TEST_API_KEY:f957d16d834eb700d2ad81a672ddcb45:1697e1f073a52d9ff872e3008f4679b2"
headers = {
    "accept": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.get(url, headers=headers)

print(response.status_code)

key = response.json()["data"]['publicKey']


