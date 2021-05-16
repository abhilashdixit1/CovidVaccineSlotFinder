import requests
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
def fetchStateAndDistrictDetail():
    respState = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states', headers=HEADERS)
    response = json.loads(respState.text)
    print("|----------------|-------------------------------|")
    print("|  State Id      |                 State Name    |")
    print("|----------------|-------------------------------|")
    for doc in response['states']:
        print(doc['state_id'],"              |  ",doc['state_name'])
        print("|----------------|-------------------------------|")
        
    stateId = input("Please enter the state Id:\n")


    districtUrl ="https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(stateId)
    respDistricts = requests.get(districtUrl, headers=HEADERS)
    response = json.loads(respDistricts.text)

    for doc in response['districts']:
        print(doc['district_id'],"              |  ",doc['district_name'])
        print("|----------------|-------------------------------|")
        
    
            
if __name__ == "__main__":
    fetchStateAndDistrictDetail()
            




