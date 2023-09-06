import requests
import get_wallet_set
#  replace the wallet set id to desired wallet set id
walletSetId = get_wallet_set.id
url = "https://api.circle.com/v1/w3s/developer/walletSets/" + walletSetId

# you can change the name here
updatedName = "ghw_wallet"
apiKey = "$ENV_API_KEY:ID:SECRET$"
payload = { "name": updatedName }
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + apiKey
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)