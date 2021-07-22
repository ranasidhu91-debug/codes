from tkinter import Toplevel

from ContractCreationUserInterface import ContractCreationUI
from Model.Bid import all_tutor_offers
from Model.Bid import tutor_bid
from WidgetMakers import WidgetAbstract


class singleBidViewUI(WidgetAbstract):
    def __init__(self,single_bid_item, username):
        self.single_bid_frame = Toplevel()
        self.single_bid_frame.geometry("1280x720")
        self.single_bid_frame.title(single_bid_item['subject']['description'])
        self.single_bid_item = single_bid_item
        self.username = username

        self.bid_info_labels()
        self.tutor_offer_labels()
        self.bid_offer_entries()
        self.buy_out_bid()



    def bid_info_labels(self):
        bid_initiator = self.single_bid_item['initiator']['userName']
        bid_info = self.single_bid_item['additionalInfo']['bidInfo']

        required_lesson = self.label_maker(self.single_bid_frame)
        required_lesson.config(text="Required lesson: " + bid_info['requiredLesson'], height="4", width="50")
        required_lesson.grid(row=1, column=7)
        time_day = self.label_maker(self.single_bid_frame)
        time_day.config(text="Preferred time and day: " + bid_info['timeDay'], height="4", width="50")
        time_day.grid(row=3, column=7)
        number_of_sessions = self.label_maker(self.single_bid_frame)
        number_of_sessions.config(text="Number of sessions per week: " + bid_info['sessionsPerWeek'], height="4", width="50")
        number_of_sessions.grid(row=5,column=7)
        rate = self.label_maker(self.single_bid_frame)
        rate.config(text="Rate(per hour or per session): " + bid_info['lessonRate'], height="4", width="50")
        rate.grid(row=7, column=7)
        poster = self.label_maker(self.single_bid_frame)
        poster.config(text="Posted by: " + bid_initiator, height="4", width="50")
        poster.grid(row=9, column=7)

        # bid_viewer = user_details.User_Details(username).isTutor()

    def tutor_offer_labels(self):
        time_day = self.label_maker(self.single_bid_frame)
        time_day.config(text="Preferred time and day: ", height="4", width="25")
        time_day.grid(row=1, column=1)
        sessions = self.label_maker(self.single_bid_frame)
        sessions.config(text="Number of sessions per week: ", height="4", width="25")
        sessions.grid(row=3, column=1)
        rate = self.label_maker(self.single_bid_frame)
        rate.config(text="Rate(per hour or per session): ", height="4", width="25")
        rate.grid(row=5, column=1)

    def bid_offer_entries(self):
        time_day = self.Entry_maker(self.single_bid_frame)
        time_day.grid(row=1, column=2)
        sessions_per_week = self.Entry_maker(self.single_bid_frame)
        sessions_per_week.grid(row=3, column=2)
        rate = self.Entry_maker(self.single_bid_frame)
        rate.grid(row=5, column=2)

        # Button for tutor to submit their bid offer
        make_bid_offer_button = self.button_maker(self.single_bid_frame)
        make_bid_offer_button.config(text="Make Bid Offer", command=lambda: {tutor_bid.tutor_bid(
                                                                           time_day.get(),
                                                                           sessions_per_week.get(),
                                                                           rate.get()).make_bid_offer(self.username, self.single_bid_item), all_tutor_offers.AllTutorOffers().tutor_offer_button(self.single_bid_item, self.username, self.single_bid_frame)}, width="15", height="2")
        make_bid_offer_button.grid(row=11, column=2)


    def buy_out_bid(self):
        # Tutor can instantly buy out any bid if they agree with student terms and conditions
        first_party_name = self.single_bid_item['initiator']['userName']
        second_party_name = self.username
        subject_description = self.single_bid_item['subject']['description']
        subject_lesson = self.single_bid_item['subject']['name']
        additional_info = self.single_bid_item['additionalInfo']['bidInfo']
        time_day = additional_info['timeDay']
        sessions = additional_info["sessionsPerWeek"]
        rate = additional_info['lessonRate']
        bidID = self.single_bid_item['id']

        buy_out_bid = self.button_maker(self.single_bid_frame)
        buy_out_bid.config(text="Buy Out Bid", command=lambda: {ContractCreationUI(self.single_bid_frame,first_party_name,second_party_name,sessions,rate,time_day,subject_lesson, subject_description, bidID)}, width="15", height="2")
        buy_out_bid.grid(row=13, column=2)

        all_tutor_offers.AllTutorOffers().tutor_offer_button(self.single_bid_item, self.username, self.single_bid_frame)
