import requests

import API.Abstract_API_methods as API
from API import Contract_API
from API.api_key import api_key
from API.root_url import root_url

user_url = root_url + "/user"


class User(API.Abstracts):
    """
    This class inherits from API.Abstracts and implements concrete classes to interact with the system using RESTAPI requests.
    """
    def get(self):
        """
        This method returns all the users in the system
        """
        response = requests.get(
            url= user_url,
            headers={'Authorization': api_key}
        )
        json_data = response.json()
        return json_data

    def post_login(self, username, password):
        """
        This method creates the a new username and password
        """
        response = requests.post(
            url=user_url + "/login",
            headers = {'Authorization':api_key},
            params={'jwt':'true'},
            data={
                'userName':username,
                'password':password
            }
        )
        return response.status_code

    def get_individual_user(self,username):
        """
        This method gets the user based on the username
        """
        users = self.get()
        for i in users:
            if i["userName"] == username:
                return i

    def get_by_id(self, id):
        """
        This method returns a user using the id
        """
        response = requests.get(
            url = user_url,
            headers= {'Authorization': api_key}
        )
        json_data = response.json()
        return json_data

    def put_new_user(self,givenName, familyName,username,password,isStudent,isTutor):
        """
        This method creates a new user
        """
        response = requests.post(
            url=user_url,
            headers= {'Authorization':api_key},
            data={
                "givenName" : givenName,
                "familyName" : familyName,
                "userName" : username,
                "password":password,
                "isStudent": isStudent,
                "isTutor":isTutor
            }
        )
        return response.status_code

    def get_user_initiated_bids(self, username):
        """
        This method returns the bids created by one user.
        """
        user = self.get_individual_user(username)
        response = requests.get(
            url=user_url + "/" + user['id'],
            headers={'Authorization': api_key},
            params={'fields': 'initiatedBids'}
        )
        return response.json()

    # def user_bid_subscription(self, username):
    #     user = self.get_individual_user(username)
    #     response = requests.patch(
    #         url=user_url + "/" + user['id'],
    #         headers= {'Authorization':api_key},
    #         json={
    #             "givenName" : user['givenName'],
    #             "familyName" : user['familyName'],
    #             "password":user['password'],
    #             "isStudent": user['isStudent'],
    #             "isTutor":user['isTutor'],
    #             "isAdmin":user['isAdmin'],
    #             "additionalInfo":{
    #                 "subscribedBids": []
    #             }
    #         }
    #     )
    #     return response.status_code

    # fix this. this is wrong. this calculates all the contracts and not the active contracts.
    def user_contracts_nos(self, id):
        contracts = Contract_API.Contract().get()
        contract_nos = 0
        for i in contracts:
            if i['firstParty']['id'] == id:
                contract_nos += 1
        return contract_nos