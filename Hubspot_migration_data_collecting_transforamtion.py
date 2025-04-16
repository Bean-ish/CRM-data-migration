
# ==== ingesting data ====
# e.g. importing 3 datasets from kaggle using APIs

import kagglehub
from kagglehub import KaggleDatasetAdapter
import requests
import pandas as pd


# customer data
customer_data_file_path = 'accounts.csv'

df_company = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "innocentmfa/crm-sales-opportunities",
    customer_data_file_path,
)

print("First 5 records:", df_company.head())


# sales team data
salesteam_data_file_path = 'sales_teams.csv'

df_contact = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "innocentmfa/crm-sales-opportunities",
    salesteam_data_file_path,
)

print("First 5 records:", df_contact.head())


# deals data
deals_data_file_path = 'sales_pipeline.csv'

df_deal = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "innocentmfa/crm-sales-opportunities",
    deals_data_file_path,
)

print("First 5 records:", df_deal.head())


# # ==== export into csv files for bulk importing ====

# df_customer.to_csv("company_import.csv", index=False)
# df_steam.to_csv("steam_import.csv", index=False)
# df_deals.to_csv("deals_import.csv", index=False)





# ==== cleaning and transformation ====

# follow the requirements or each object types when uploading
# create external_id in each objects is the best practice in data modeling

# mapping sales team to contacts with extra marker "is_sales_agent"
# must have first name, last name, or email

df_contact['sales_agent'] = df_contact['sales_agent'].str.strip()

df_contact[['first_name', 'last_name']] = df_contact['sales_agent'].str.split(' ', n = 1, expand = True)

df_contact['external_id'] = pd.Series(range(1, len(df_contact) + 1))

#TODO turn sales_agent to email to serve as PK
df_contact['sales_agent_email'] = df_contact['sales_agent'].str.replace(' ', '').str.lower() + '@abc.com'

df_contact.drop(columns=['sales_agent'], inplace=True)



# mapping sales record into deals object
# must have deal_stage and pipeline (using default for this upload)
df_deal['pipeline'] = 'default'

# array(['Won', 'Engaging', 'Lost', 'Prospecting'], dtype=object)

deal_stage_mapping = {
    "Prospecting": "1423633125",
    "Engaging": "appointment_scheduled",
    "Won": "closedwon",
    "Lost": "closedlost"
}

df_deal['deal_stage'] = df_deal['deal_stage'].map(deal_stage_mapping)

#TODO turn sales_agent into emails
df_deal['sales_agent_email'] = df_deal['sales_agent'].str.replace(' ', '').str.lower() + '@abc.com'

df_deal.drop(columns=['sales_agent'], inplace=True)





# mapping accounts to company objects
# must have name 

df_company['external_id'] = pd.Series(range(1, len(df_company) + 1))

df_company.drop(columns=['subsidiary_of'], inplace=True)



# # ==== export into csv files for bulk importing ====

df_company.to_csv("company_import_clean.csv", index=False)
df_contact.to_csv("contact_import_clean.csv", index=False)
df_deal.to_csv("deal_import_clean.csv", index=False)










       