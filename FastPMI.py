# -*- coding: utf-8 -*-
import requests, json
from faker import Factory
fake = Factory.create('ru_RU')

def regPMI():
    url = "https://pmi.experium.ru/SupportSrv/SupportSrv.svc/Support/v1/pmi/registration"
    data = (fake.name(),fake.name(),'blablabla@dfgfdgdf.com','test123')
    for t in data:
        print t
    regdata = {'lastName':data[0],'firstName':data[1],'login':data[2],'confirmPassword':data[3],'password':data[3]}
    regreq = requests.post(url, json=regdata)
    print (regreq.status_code)
    print (regreq.text)
    response = json.loads(regreq.text)

    url2 = "https://pmi.experium.ru/SupportSrv/SupportSrv.svc/Support/v1/pmi/ra/submission"
    headers = {'Authorization':'Token %s'%response['token']}
    postdata1 = {"draft":True}

    postreq = requests.post(url2, headers=headers, json=postdata1)
    print (postreq.status_code)
    print (postreq.text)
    response1 = json.loads(postreq.text)
    postdata = {"token": response['token'], "attachedDocument": True, "draft": False, "lastChangeDate": "",
                "personal": {"firstName": data[1], "middleName": "", "lastName": data[0],
                             "birthDate": ""},
                "contacts": {"phone": "74565464565", "mobile": "74565465464", "email": data[3],
                             "mobileCode": "", "phoneCode": ""},
                "addresses": [{"countryCode": 1, "townkey": 19, "region": 4}], "education": [
            {"levelCode": 4, "institute": 3, "otherInstituteName": "", "speciality": "специальность",
             "startYearGraduation": 1988, "yearGraduation": 1999}],
                "graduateInfo": {"englishKnowLevel": 32, "businessArea": 15},
                "sourceInfo": {"sourceId": 4, "sourceOther": ""}, "id": response1['id']}

    postreq = requests.post(url2, headers=headers, json=postdata)
    print (postreq.status_code)
    print (postreq.text)

regPMI()
