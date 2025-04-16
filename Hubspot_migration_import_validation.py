
import requests
import os
import json



id = '144445575'
url = 'https://api.hubapi.com/crm/v3/imports/' + id

ACCESS_TOKEN = '/'

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}


response = requests.get(url, headers = headers)

if response.status_code == 200:
    print(json.dumps(response.json(), indent=2))
    
else: 
    print(f"Error {response.status_code}: {response.text}")

# data = response.json()

