# check_webpages.py
import requests
import json

with open("webpages.json") as file:
    webpages = json.load(file)

for webpage in webpages:
    try:
        response = requests.get(webpage["url"], timeout=5)
        response.raise_for_status()
        print(f"{webpage['name']} is up and running!")
    except requests.exceptions.RequestException as error:
        print(f"{webpage['name']} is down: {error}")
