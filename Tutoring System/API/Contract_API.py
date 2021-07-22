
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

import requests

from API import Abstract_API_methods as API
from API.api_key import api_key
from API.root_url import root_url

contract_url = root_url + "/contract"

class Contract(API.Abstracts):
    """
    This class inherits from API.Abstracts and implements Contract Related API REQUESTS
    """
    def get(self):
        response = requests.get(
            url= contract_url,
            headers={'Authorization': api_key}
        )
        json_data = response.json()
        return json_data

    def post(self,firstPartyID,secondPartyID,subjectID,bidID,sessions,rate,time_day,months,paymentInfo=None,lessonInfo=None):
        response = requests.post(
            url=contract_url,
            headers= {'Authorization': api_key},
            json={
                "firstPartyId":firstPartyID,
                "secondPartyId": secondPartyID,
                "subjectId":subjectID,
                "dateCreated": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
                "expiryDate": (datetime.now() + relativedelta(months=months)).strftime('%Y-%m-%dT%H:%M:%S.%f'),
                "paymentInfo":{},
                "lessonInfo":{},
                'additionalInfo':{
                    "bid" : bidID,
                    "session":sessions,
                    "rate": rate,
                    "time_day":time_day
                }
            }
        )

        return response.status_code

    def get_by_id(self, id):
        response = requests.get(
            url=contract_url + "/" + id,
            headers = {'Authorization': api_key}
        )
        json_data = response.json()
        return json_data

    def get_single_contract_id(self,first_username,second_username,subject_id):
        data = self.get()
        for i in data:
            if i['firstParty']['userName'] == first_username and i['secondParty']['userName'] == second_username and i['subject']['id'] == subject_id:
                return i['id']

    def signed(self,id):
        # self.patch_sign(id)
        response = requests.post(
            url=contract_url + "/" + id + "/sign",
            headers={'Authorization': api_key},
            json={
                "dateSigned": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
            }
        )
        return response.status_code

    def patch_sign(self,id):
        response = requests.patch(
            url=contract_url + "/" + id,
            headers={'Authorization': api_key},
            json={
                "dateSigned": {}
            }
        )
        return response.status_code

    def all_contracts_by_user(self,username):
        all = self.get()
        contracts = []
        for i in all:
            if i["firstParty"]["userName"] == username or i["secondParty"]["userName"] == username:
                if i not in contracts:
                    contracts.append(i)
        return contracts

    def active_contracts(self,username):
        all = self.all_contracts_by_user(username)
        if not all:
            return []
        active = []
        for i in all:
            if i['dateSigned']:
                expirydate = i['expiryDate']
                expiry = datetime.strptime(expirydate[:-1],'%Y-%m-%dT%H:%M:%S.%f')
                if expiry > datetime.now():
                    active.append(i)
            return active


    def expiring_contracts(self,username):
        user_contracts = self.all_contracts_by_user(username)
        if not user_contracts:
            return []
        expiring_contracts = []
        for i in user_contracts:
            time_string = i["expiryDate"]
            expiry_date = datetime.strptime(time_string[:-1],'%Y-%m-%dT%H:%M:%S.%f')
            current = datetime.now()
            if (expiry_date - current) > timedelta(minutes=5):
                expiring_contracts.append(i)
        return expiring_contracts

    def pending_contracts(self,username):
        all = self.all_contracts_by_user(username)
        if not all:
            return []
        pending = []
        for i in all:
            time_string = i["expiryDate"]
            expiry_date = datetime.strptime(time_string[:-1], '%Y-%m-%dT%H:%M:%S.%f')
            current = datetime.now()
            if expiry_date < current:
                continue
            else:
                if i['dateSigned'] == None:
                    pending.append(i)
        return pending