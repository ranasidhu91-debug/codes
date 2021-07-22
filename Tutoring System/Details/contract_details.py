from API import Contract_API

class Contract_Details:
    def __init__(self,id):
        self.__details = Contract_API.Contract().get_by_id(id)

    def get_contract_id(self):
        return self.__details["id"]

    def get_firstParty(self):
        return self.__details["firstParty"]

    def firstPartyFullName(self):
        return self.get_firstParty()['givenName'] + " " + self.get_firstParty()['familyName']

    def get_secondParty(self):
        return self.__details["secondParty"]

    def secondPartyFullName(self):
        return self.get_secondParty()['givenName'] + " " + self.get_secondParty()['familyName']

    def get_subject(self):
        return self.__details["subject"]

    def get_lesson(self):
        return self.get_subject()['name']

    def get_description(self):
        return self.get_subject()['description']

    def get_dateCreated(self):
        return self.__details["dateCreated"]

    def get_expiryDate(self):
        return self.__details["expiryDate"]

    def get_paymentInfo(self):
        return self.__details["paymentInfo"]

    def get_lessonInfo(self):
        return self.__details["lessonInfo"]

    def get_additionalInfo(self):
        return self.__details["additionalInfo"]

    def bid(self):
        return self.get_additionalInfo()['bid']

    def contract_rate(self):
        return self.get_additionalInfo()['rate']

    def sessions(self):
        return self.get_additionalInfo()['session']

    def time_day(self):
        return self.get_additionalInfo()['time_day']



