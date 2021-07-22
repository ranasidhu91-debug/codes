from User_api import User
from Contract_API import Contract


class User_Details:
    def __init__(self,username):
        self.__user_in_system = User().get_individual_user(username)
        self.all_contracts = Contract().all_contracts_by_user(username)
        self.username = username

    def get_user_in_system(self):
        return self.__user_in_system

    def get_userid(self):
        return self.__user_in_system["id"]

    def get_fullName(self):
        return self.get_givenName() + " " + self.get_familyName()

    def get_givenName(self):
        return self.__user_in_system["givenName"]

    def get_familyName(self):
        return self.__user_in_system["familyName"]

    def isStudent(self):
        return self.__user_in_system["isStudent"]

    def isTutor(self):
        return self.__user_in_system["isTutor"]

    def active(self):
        return Contract().active_contracts(self.username)

    def user_latest_contracts(self):
        latest = []
        if len(self.all_contracts) < 6:
            return self.all_contracts
        else:
            length = len(self.all_contracts)
            for i in range(length):
                for j in range(0,length-i-1):
                    contract1 = self.all_contracts[j]
                    contract2 = self.all_contracts[j+1]
                    date1 = contract1["dateSigned"]
                    date2 = contract2["dateSigned"]
                    if date1 is None or date2 is None:
                        date1 = contract1['dateCreated']
                        date2 = contract2['dateCreated']
                    if date1 < date2:
                        self.all_contracts[j],self.all_contracts[j+1] = self.all_contracts[j+1],self.all_contracts[j]
            for i in range(5):
                latest.append(self.all_contracts[i])
            return latest

    def user_expiring_contracts(self):
        return Contract().expiring_contracts(self.username)








