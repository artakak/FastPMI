# -*- coding: utf-8 -*-
import requests, json
import random
from faker import Factory
import threading

fake = Factory.create('ru_RU')
fake_US = Factory.create()
count = 0
s = requests.Session()
def regPMI():
    global count
    global s
    url = "http://webtest.experium.ru:90/SupportSrv/SupportSrv.svc/Support/v1/pmi/registration"
    data = (fake.last_name_female(),fake.first_name_female(), fake_US.safe_email(), 'test123', fake.first_name_male()+u'овна')
    #for t in data:
        #print t
    regdata = {'lastName':data[0],'firstName':data[1],'login':data[2],'confirmPassword':data[3],'password':data[3]}
    regreq = s.post(url, json=regdata)
    print (regreq.status_code)
    #print (regreq.text)
    response = json.loads(regreq.text)

    url2 = "http://webtest.experium.ru:90/SupportSrv/SupportSrv.svc/Support/v1/pmi/gr/submission"
    headers = {'Authorization':'Token %s'%response['token']}
    postdata1 = {"draft":True}

    postreq = s.post(url2, headers=headers, json=postdata1)
    print (postreq.status_code)
    #print (postreq.text)
    response1 = json.loads(postreq.text)
    postdata = {"token": response['token'], "attachedDocument": True, "draft": False, "lastChangeDate": "",
                "personal": {"firstName": data[1], "middleName": data[4], "lastName": data[0],
                             "birthDate": ""},
                "contacts": {"phone": "74565464565", "mobile": "74565465464", "email": data[3],
                             "mobileCode": "", "phoneCode": ""},
                "addresses": [{"countryCode": 1, "townkey": 19, "region": 4}], "education": [
            {"levelCode": 4, "institute": 3, "otherInstituteName": "", "speciality": "специальность",
             "startYearGraduation": 1988, "yearGraduation": 1999}],
                "graduateInfo": {"englishKnowLevel": 32, "businessArea": 12},
                "sourceInfo": {"sourceId": 4, "sourceOther": ""}, "id": response1['id']}

    postreq = s.post(url2, headers=headers, json=postdata)
    print (postreq.status_code)
    count+=1
    print ('***%d***'%count)
    #print (postreq.text)

def tread():
    for _ in range(10000):
        try:
            regPMI()
        except: pass

for _ in range(4):
    threading.Thread(target=tread).start()