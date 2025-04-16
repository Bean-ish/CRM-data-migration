
#### notes for multi-file bulk importing

1. clean and transform your data into import ready tables
    - [ ]  follow the requirement for each object when uploading, must have fields [reference](https://knowledge.hubspot.com/import-and-export/set-up-your-import-file#required-properties)
    - [ ]  convert date data if you need to but you usually don’t as they support slash as well, also make sure to check the data in df format cuz excel doesn’t display the real value it changes the date format
    - [ ]  match each column to a property (make sure you have the internal property names) : either *use properties API to retrieve all properties and parse the JSON to get a list* OR *check the available properties in your GUI*
    - [ ]  create external ids for each objects if you are actively managing a relationship between HubSpot data and another external data storage such as the original database you are migrating from (internal ids only gets created after loading and can’t be added manually)

2. configures the data model in HubSpot
    
    for each object, you need to:
    
    - [ ]  manage custom properties for legacy data (you can’t import data that will be automatically assigned by HubSpot like “date created”, if you want to preserve historical data in data migration, you need to create custom columns “date created (legacy)”)
    - [ ]  create other custom properties for your data columns

3. save files into acceptable format (e.g. csv)

4. configure importing sessions and metadata <br/>
    (1) metadata should be a JSON string then wrapped in a dictionary like this `payload = {”importRequest”: json.dumps(metadata)}`<br/>
    (2) in your header you shouldn’t include  `,"Content-Type": "multipart/form-data”` without the wall, also they automatically add this for you when you are posting multiple files so it is not really necessary<br/> 
    (3) you shouldn’t assign the alternative id type to columns that allows duplicates in HubSpot<br/>
    (4) also note that you cannot import any values that are auto calculated by hubspot and they actually don’t tell you you can’t until you loading fails which is why they SUCK big time<br/>
    
5. mapping out associations between tables <br/>
   The thing is the number of your objects in column-mapping has to = the number of columns in you data file. So if you want to use a column to create an association (acting as FK) but then also want the data in regular column format you have to duplicate the column and map them out twice <br/>
   Find you association type and id by either calling schema or property API or checking the doc WHICH IS NOT COMPLETE FOR SOME REASON???

7. send GET request to check the property names to the object and make sure the data type, rules, and internal names match
