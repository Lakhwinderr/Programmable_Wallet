import requests

from bs4 import BeautifulSoup

# Send an HTTP GET request to the website
url = "https://www.uuidgenerator.net/"
response = requests.get(url)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the UUID element on the page (you may need to inspect the HTML structure of the page)
    uuid_element = soup.find("span", {"id": "generated-uuid"})

    # Extract the UUID
    if uuid_element:
        uuid = uuid_element.text.strip()
        print("UUID:", uuid)
    else:
        print("UUID not found on the page.")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
