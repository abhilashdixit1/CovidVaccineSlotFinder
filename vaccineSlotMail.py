import requests
import json
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Edit these variables as per your need

FROM_USER = '<from email id>'
PASSWORD = '<password of from email id>'
TO_USER = '<to email id>'
MIN_AGE=55

#Constants

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
CURDATE=datetime.datetime.today().strftime("%d-%m-%Y")

def mailto(email_content):
    from_user = FROM_USER
    to_user = TO_USER
    password = PASSWORD
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_user, password)
    subject = 'Vaccine Slots availability'
    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['TO'] = to_user
    msg['Subject'] = subject
    msg.attach(MIMEText(email_content,'html'))
    text = msg.as_string()
    server.sendmail(from_user,to_user,text)
    server.close()

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
        

    districtId = input("Please enter the district Id:\n")
    districtName=""
    for doc in response['districts']:
        if(str(doc['district_id']).strip()==districtId.strip()):
            districtName=doc['district_name']
    
    fetchVaccineSlots(districtId,districtName)

    
def fetchVaccineSlots(districtId,districtName):

    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(districtId, CURDATE)
    response = requests.get(URL,headers=HEADERS)
    if response.ok:
        resp_json = response.json()
        data="""<html>
        <head>
        <style>
        </style>
        </head>
        <body>
        <p>Hi!</p>
        <p>Here is your requested vaccine slot avilability detail:</p>	
        <pre>"""

        str=""
        if resp_json["centers"]:
            for center in resp_json["centers"]:
                for session in center["sessions"]:
                    if session["min_age_limit"] <= MIN_AGE and session["available_capacity"]>0 :
                        str+="\t"+center["name"]
                        str+="\n\t"+center["address"]+"\n\t"+session["date"]+"\t Price: "+center["fee_type"]+"\n"
                        str+="\t Available Capacity: {}".format(session["available_capacity"])+"\n"
                        str+="\t Min Age Limit: {}".format(session["min_age_limit"])+"\n"
                        if(session["vaccine"] != ''):
                            str+="\t Vaccine: "+session["vaccine"]+"\n\n"
                        print(str)
        if(str==""):
            print("No slots Avilable on :{}".format(CURDATE))
            data+="<h4> Available vaccine slots in "+districtName+" as of "+CURDATE+"</h4>"
            str+="Sorry no available slot for your district on given date..!!"
            mailto(data+str+"</pre><p>Stay home, Stay Safe..!!</p><p>VacBot</p></body></html>")
        else:
            data+="<h4> Available vaccine slots in "+districtName+" as of "+CURDATE+"</h4>"
            mailto(data+str+"</pre><p>Stay home, Stay Safe..!!</p><p>VacBot</p></body></html>")
            
if __name__ == "__main__":
    fetchStateAndDistrictDetail()
            




