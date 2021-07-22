from API.Bid_API import Bid
from Model.Bid import all_tutor_offers
from Model.Bid import student_bid_info
from tkinter import Toplevel
from WidgetMakers import WidgetAbstract

class SingleBidViewStudent(WidgetAbstract):
    """
    Get a more detailed view of a particular bid that the current user has created.
    The user can also check which tutors have made offers on their bid
    """
    def __init__(self, bid_item, current_user):
        self.root = Toplevel()
        self.bid_item = bid_item
        self.username = current_user
        self.root.geometry("1280x720")
        student_bid_info.StudentBidInfo().display_bid_details(self.bid_item, self.root)
        self.display_bidders()


    def display_bidders(self):
        bid = Bid().get_by_id(self.bid_item['id'])
        all_tutor_offers.AllTutorOffers().tutor_offer_button(bid, self.username, self.root)