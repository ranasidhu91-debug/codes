from Details import user_details

from WidgetMakers import WidgetAbstract
from tkinter import *
from API.Contract_API import Contract

class Dashboard(WidgetAbstract):
    """
    This class creates the main Screen View that the users would see. If the user is a student, then the student would be able to
    view bids that have been created or make a new bid.
    """
    def __init__(self,name,contract_nos):
        """
        This is the constructor class that creates the View and also stores the instance variables of the class.
        """
        self.root = Toplevel()
        self.name = name
        self.root.configure(bg="CadetBlue4")
        self.root.geometry("500x300")
        self.frame = Frame(self.root, bg="CadetBlue4")
        self.user_details = user_details.User_Details(WidgetAbstract.username)
        self.isTutor = user_details.User_Details(WidgetAbstract.username).isTutor()
        self.contract_nos = contract_nos
        self.expiring_contracts = Contract().expiring_contracts(WidgetAbstract.username)
        self.frame_generator()
        self.frame.pack()
        self.root.protocol("WM_DELETE_WINDOW", WidgetAbstract.root.destroy)
        self.view_all_bids_button = self.button_maker(self.frame)


        self.notification_button = None
        self.title_header = None

        # tutor
        self.view_all_bids_button = None
        self.view_subscribed_bids = None

        # student
        self.bidding_button = None
        self.view_my_bids = None



