
import requests
import json
import pandas as pd

ACCESS_TOKEN = '/'


# ==== get associations of contacts ====

url = 'https://api.hubapi.com/crm-object-schemas/v3/schemas/contacts'

# url = 'https://api.hubapi.com/crm/v4/associations/company/contact/labels'

headers = {
    'Authorization': f"Bearer {ACCESS_TOKEN}",
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

# Check the response status and data
if response.status_code == 200:
    # print(json.dumps(response.json(), indent=2))
    message = 'retrieved'
    print(message)
    
else: 
    print(f"Error {response.status_code}: {response.text}")

data = response.json()

# df = pd.DataFrame(data['associations'])


    

