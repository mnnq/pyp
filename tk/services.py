import requests,configparser, cfg, random, string,os, sys
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(sys.executable),'configEcareApp.ini'))


def frDel(username,isocode):
    try:
        url = config['HOSTS']['FR']+config['PATHS']['FR_Delete']

        payload = {
            "userName": username,
            "iso2Code":isocode,
            "businessUnitType": "SSLA-DTH"
        }

        headersFR = {
            "Content-type": "application/json",
            "Authorization": "Basic "+cfg.myList['basic']
        }

        

        response = requests.post( url, json=payload, headers=headersFR)
        return response.json()
    except Exception as e:
        return e 


def frRead(accountid,isocode):
    try:
        url = config['HOSTS']['FR']+config['PATHS']['FR_Read']

        payload = {
            "accountID": accountid,
            "iso2Code":isocode
        }

        headersFR = {
            "Content-type": "application/json",
            "Authorization": "Basic "+cfg.myList['basic']
        }

        response = requests.post( url, json=payload, headers=headersFR)
        return response
    except Exception as e:
        return e    



def v360(accountid, isocode):
    client = BackendApplicationClient(client_id=cfg.myList['client_id'])
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=config['HOSTS']['TOKEN'], client_id=cfg.myList['client_id'],
            client_secret=cfg.myList['client_secret'])
    try:
        url = config['HOSTS']['QAM']+config['PATHS']['QAM_360']+str(accountid)

        headers = {
            "Metadata-SystemId": "eCareMobile",
            "metadata-sendercountry": isocode,
            "Content-type": "application/json",
            "Metadata-RequestId": "12345",
            "Metadata-UserId": "S_RG_QAM_ECMOBBKD",
            "Accept-Encoding": "gzip",
            "Authorization": "Bearer "+token['access_token']
        }

        response = requests.get( url, headers=headers)        
        response.cookies.clear()
        
        return response
    except Exception as e:      
        return e



def registro(accountid, isocode, email, password):
    try:
        url = config['HOSTS']['FR']+config['PATHS']['FR_Create']

        if not email:
            email = "".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(9))+"@gmail.com"
        if not password:
            password = "Directv2021"

        print(email)
        
        headersFR = {
            "Content-type": "application/json",
            "Authorization": "Basic "+cfg.myList['basic']
        }


        payload = {
            "iso2Code": isocode,
            "mail": email,
            "userName": email,
            "givenName": "ECARE",
            "accountID": accountid,
            "sn": "ECARE",
            "businessUnitType": "SSLA-DTH",
            "password": password
        }    

        
        v = v360(accountid, isocode)

        v.raise_for_status()

        
        if v.json()['GetCustomer360ViewResponse']['GetCustomer360ViewResult']['CustomerAgreement']['type']['id'] != "2":          
            payload['externalRefID'] = v.json()['GetCustomer360ViewResponse']['GetCustomer360ViewResult']['Customer']['IndividualRole']['IdentifiedBy']['IndividualIdentifications'][0]['cardNr']
           
        else:           
            z = v.json()['GetCustomer360ViewResponse']['GetCustomer360ViewResult']['CustomerPhysicalResourceList']['PhysicalResources']
            payload['smartCardNum'] = [d for d in z if d['serialNumber'].isdigit()][0]['serialNumber']
        
        
        response = requests.post( url, json=payload, headers=headersFR)

        response.raise_for_status()

        return {"user":response.json()['User'], "password":password}
    except Exception as e:
        return e

    
    