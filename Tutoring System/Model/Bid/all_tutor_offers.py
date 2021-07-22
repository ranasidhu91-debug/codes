import tkinter as tk
from tkinter import Toplevel
from View import MessagesUI
from tkinter import messagebox
from Details.user_details import User_Details
from ContractCreationUserInterface import ContractCreationUI


class AllTutorOffers:
    """
    This class displays all the offers that tutors have made for a particular bid
    """
    def __init__(self):
        self.root = Toplevel().withdraw()


    def tutor_offer_button(self, single_bid_item, username,frame):
        """

        """
        column = 1
        for item in single_bid_item['additionalInfo']['tutorBidOffers']:
            row = 15
            if single_bid_item['initiator']['userName'] == username:
                tk.Button(frame, text="Buy Offer", command = lambda arg = single_bid_item, offer = item: self.student_agree_offer(arg, offer), width="25", height="2", padx="4").grid(row=row, column=column)
            tk.Label(frame, text="Time and Day: " + item['timeDay'], height="4", width="25").grid(row=row + 1, column=column)
            tk.Label(frame, text="Sessions per week: " + item['sessionsPerWeek'], height="4", width="25").grid(row=row + 2, column=column)
            tk.Label(frame, text="Lesson Rate: " + item['lessonRate'], height="4", width="25").grid(row=row + 3, column=column)
            tk.Label(frame, text="Offered By: " + item['offeredBy'], height="4", width="25").grid(row=row + 4, column=column)
            if self.is_student(username):
                tk.Button(frame, text="Message Tutor", command = lambda arg = single_bid_item, user = username, tutor_bid_offer=item: self.view_messages(arg, user, tutor_bid_offer), width="25", height="2").grid(row=row + 5, column=column)
            else:
                tk.Button(frame, text="Message Student",command=lambda arg=single_bid_item, user=username, tutor_bid_offer=item: self.view_messages(arg, user, tutor_bid_offer),width="25", height="2").grid(row=row + 5, column=column)
            column+=1


    def student_agree_offer(self, bid, offer):
        """
        Creates the credentials of the bid that would be passed onto the contract and creates the contract if the student
        decides to agree to an offer
        """
        bidID = bid['id']
        first_party_username = bid['initiator']['userName']
        second_party_username = offer['offeredBy']
        subject_lesson = bid['subject']['name']
        subject_description = bid['subject']['description']
        bidinfo = bid['additionalInfo']['bidInfo']
        sessions = bidinfo['sessionsPerWeek']
        rate = bidinfo['lessonRate']
        timeday = bidinfo['timeDay']
        options = messagebox.askquestion("Verification",
                                         "You are about to agree to the offer. Proceed?")
        if options == 'yes':
            # ContractUI.ContractUI(first_party_username, second_party_username, subject_lesson, subject_description, bid)
            ContractCreationUI(self.root,first_party_username,second_party_username,sessions,rate,timeday,subject_lesson,subject_description,bidID)

    def view_messages(self, bid, username, tutor_bid_offer):
        """
        Displays the messages between the student and tutor
        """
        MessagesUI.MessagesUI(bid, username, tutor_bid_offer)

    def is_student(self, username):
        user = User_Details(username).get_user_in_system()
        return user['isStudent']





