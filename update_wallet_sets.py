import requests
import get_wallet_set
#  replace the wallet set id to desired wallet set id
walletSetId = get_wallet_set.id
url = "https://api.circle.com/v1/w3s/developer/walletSets/" + walletSetId

# you can change the name here
updatedName = "ghw_wallet"
apiKey = "TEST_API_KEY:f957d16d834eb700d2ad81a672ddcb45:1697e1f073a52d9ff872e3008f4679b2"

payload = { "name": updatedName }
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)