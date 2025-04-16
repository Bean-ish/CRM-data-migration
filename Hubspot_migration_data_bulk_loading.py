
import requests
import pandas as pd
import os
import json

# ==== create a private app, configure scope (access write APIs) ====

ACCESS_TOKEN = '/'







# ==== match your column names with object property names ====
# # GET request to get a JSON file containing property names

# # GET companies

# url = "https://api.hubapi.com/crm/v3/properties/companies"
# headers = {
#     "Authorization": f"Bearer {ACCESS_TOKEN}",
#     "Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     properties = response.json()
#     print(properties)
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)

# # examine the JSON file

# print(json.dumps(properties, indent=2))

# # extract only names and descriptions, then ctrl + F

# for prop in properties.get('results', []):
#     print(f"Name: {prop.get('name')}")
#     print(f"Description: {prop.get('description')}")
#     print(f"Type: {prop.get('type')}")


# # GET users

# url = "https://api.hubapi.com/crm/v3/properties/companies"
# headers = {
#     "Authorization": f"Bearer {ACCESS_TOKEN}",
#     "Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     properties = response.json()
#     print(properties)
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)

# # examine the JSON file

# print(json.dumps(properties, indent=2))

# # extract only names and descriptions, then ctrl + F

# for prop in properties.get('results', []):
#     print(f"Name: {prop.get('name')}")
#     print(f"Description: {prop.get('description')}")
#     print(f"Type: {prop.get('type')}")


# # GET deals

# url = "https://api.hubapi.com/crm/v3/properties/deals"
# headers = {
#     "Authorization": f"Bearer {ACCESS_TOKEN}",
#     "Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     properties = response.json()
#     print(properties)
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)

# # examine the JSON file

# print(json.dumps(properties, indent=2))

# # extract only names and descriptions, then ctrl + F

# for prop in properties.get('results', []):
#     print(f"Name: {prop.get('name')}")
#     print(f"Description: {prop.get('description')}")
#     print(f"Type: {prop.get('type')}")








# ==== load data ====

# make a POST request to companies to populate company object table
url = "https://api.hubapi.com/crm/v3/imports"


# headers
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
    # ,"Content-Type": "multipart/form-data"
}

# data files for companies
# object type id 0-2 for companies, 0-3 for deals, 0-1 for contacts
data = {
    "name": "data migration inital loading",
    "importOperations": {
        "0-2": "CREATE",
        "0-3": "CREATE",
        "0-1": "CREATE"
    },
    "dateFormat": "YEAR_MONTH_DAY",
    "files": [
        
        # company file
        {
        "fileName": "company_import_clean.csv",
        "fileFormat": "CSV",
        "fileImportPage": {
            "hasHeader": True,
            "columnMappings": [
            {
                "columnObjectTypeId": "0-2",
                "columnName": "account",
                "propertyName": "name",
                "associationIdentifierColumn": True # acting as PK when create associations
            },
            {
                "columnObjectTypeId": "0-2",
                "columnName": "sector",
                "propertyName": "industry"
            },
            {
                "columnObjectTypeId": "0-2",
                "columnName": "year_established",
                "propertyName": "founded_year"
            },
            {
                "columnObjectTypeId": "0-2",
                "columnName": "revenue",
                "propertyName": "annualrevenue"
            },
            {
                "columnObjectTypeId": "0-2",
                "columnName": "employees",
                "propertyName": "numberofemployees"
            },
            {
                "columnObjectTypeId": "0-2",
                "columnName": "office_location",
                "propertyName": "country"
            },
            {
                "columnObjectTypeId": "0-2",
                "columnName": "external_id",
                "propertyName": "external_id"
            },
            ]
        }
        },
        # deals file
        {
        "fileName": "deal_import_clean.csv",
        "fileFormat": "CSV",
        "fileImportPage": {
            "hasHeader": True,
            "columnMappings": [
            {
            "columnObjectTypeId": "0-3",
            "columnName": "opportunity_id",
            "propertyName": "dealname" # acts as PK when create associations
            },
            # {
            # "columnObjectTypeId": "0-3",
            # "columnName": "sales_agent_email",
            # "propertyName": "sales_agent" # acts as FK to agent (contact) table when create associations
            # },
            {
            "columnObjectTypeId": "0-3",
            "columnName": "product",
            "propertyName": "product" # acts as FK to product table when create associations
            },
            # {
            # "columnObjectTypeId": "0-3",
            # "columnName": "account",
            # "propertyName": "company" # acts as FK to company table when create associations
            # },
            # associations begin
            { # contacts
            "columnObjectTypeId": "0-3",
            "toColumnObjectTypeId": "0-1",
            "columnName": "sales_agent_email",
            "propertyName": None,
            "foreignKeyType": {
              "associationTypeId": 3,
              "associationCategory": "HUBSPOT_DEFINED"
            }
            },
            { # company
            "columnObjectTypeId": "0-3",
            "toColumnObjectTypeId": "0-2",
            "columnName": "account",
            "propertyName": None,
            "foreignKeyType": {
              "associationTypeId": 5,
              "associationCategory": "HUBSPOT_DEFINED"
            }
            },
            # associations end here
            {
            "columnObjectTypeId": "0-3",
            "columnName": "deal_stage",
            "propertyName": "dealstage"
            },
            {
            "columnObjectTypeId": "0-3",
            "columnName": "engage_date",
            "propertyName": "engage_date__legacy_"
            },
            {
            "columnObjectTypeId": "0-3",
            "columnName": "close_date",
            "propertyName": "close_date__legacy_"
            },
            {
            "columnObjectTypeId": "0-3",
            "columnName": "close_value",
            "propertyName": "amount" # amount
            },
            {
            "columnObjectTypeId": "0-3",
            "columnName": "pipeline",
            "propertyName": "pipeline"
            }
            ]
        }
        },
        # contact file
        # I ran out of free custom properties and they don't let me delete old ones so have to use sales manager to indicate if it's a sales agent
        {
        "fileName": "contact_import_clean.csv",
        "fileFormat": "CSV",
        "fileImportPage": {
            "hasHeader": True,
            "columnMappings": [
            {
            "columnObjectTypeId": "0-1",
            "columnName": "sales_agent_email",
            "propertyName": "email",
            "associationIdentifierColumn": True  # acting as PK when create associations
            },
            {
            "columnObjectTypeId": "0-1",
            "columnName": "first_name",
            "propertyName": "firstname"
            },
            {
            "columnObjectTypeId": "0-1",
            "columnName": "last_name",
            "propertyName": "lastname"
            },
            {
            "columnObjectTypeId": "0-1",
            "columnName": "manager",
            "propertyName": "manager"
            },
            {
            "columnObjectTypeId": "0-1",
            "columnName": "regional_office",
            "propertyName": "state" # state/region
            }, # array(['Central', 'East', 'West'], dtype=object)
            {
            "columnObjectTypeId": "0-1",
            "columnName": "external_id",
            "propertyName": "external_contact_id"
            }
            ]
        }
        }
    
    
    ]
}




metadata = json.dumps(data) # from python format to JSON payload 

payload = {"importRequest": metadata}



relative_path = ["./company_import_clean.csv", "./deal_import_clean.csv", "./contact_import_clean.csv"]
current_dir = os.getcwd()



from contextlib import ExitStack

with ExitStack() as stack:
    files = [
        (
            'files',
            (
                os.path.basename(path),
                stack.enter_context(open(os.path.join(current_dir, path), 'rb')),
                'text/csv'
            )
        )
        for path in relative_path
    ]

    response = requests.request('POST',url, data=payload, files=files, headers=headers)


print(response.text.encode('utf8'))
print(response.status_code)