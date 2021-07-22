from API import Contract_API
from Details import user_details,subject_details
from tkinter import messagebox
class Contract_creation:
    """
    This class creates the contracts that would be agreed by the student should the student decide to accept the offer made.
    """
    def __init__(self,firstPartyUsername,secondPartyUsername, subject_lesson,subject_description, bid, paymentInfo=None, lessonInfo=None):
        """
        This constructor class creates the details that would be inserted into the contract.
        """
        self.first = firstPartyUsername
        self.second = secondPartyUsername
        self.subject_lesson = subject_lesson
        self.subject_description = subject_description

        self.paymentInfo = paymentInfo
        self.lessonInfo = lessonInfo
        self.bid = bid

    def firstPartyName(self):
        """
        This method returns the Name of the student
        """
        return user_details.User_Details(self.first).get_givenName() + " " + user_details.User_Details(self.first).get_familyName()
    #
    def secondPartyName(self):
        """
        This method returns the name of the tutor
        """
        return user_details.User_Details(self.second).get_givenName() + " " + user_details.User_Details(
            self.second).get_familyName()
    #
    def firstPartyID(self):
        """
        This method returns the ID of the student
        """
        return user_details.User_Details(self.first).get_userid()
    #
    def secondPartyId(self):
        """
        This method returns the ID ofthe tutor
        """
        return user_details.User_Details(self.second).get_userid()
    #
    def subjectID(self):
        """
        This method returns the subject ID of the lesson agreed upon in the contract.
        """
        return subject_details.Subject_Details(self.subject_lesson,self.subject_description).get_subject_id()

    def bid_details(self):
        """
        This method returns the bid
        """
        return self.bid

    def bid_id(self):
        """
        This method returns the ID of the bid that was accepted
        """
        return self.bid['id']

    def new_contract(self):
        """
        This method creates the contract by posting it onto the system using RESTAPI.
        """
        firstPartyId = self.firstPartyID()
        secondPartyID = self.secondPartyId()
        subjectID = self.subjectID()
        Contract_API.Contract().post(firstPartyId,secondPartyID, subjectID, self.bid['id'])



    




