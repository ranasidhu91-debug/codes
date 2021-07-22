from tkinter import messagebox
from abc import ABC

from API import Bid_API
from API.Bid_API import Bid
from View.BiddingUI.TutorView import SingleBidViewUI
from .display_bids_abstract import DisplayBids
from WidgetMakers import WidgetAbstract


class TutorBids(DisplayBids, ABC, WidgetAbstract):
    """
    This method implements the DisplayBids interface and adds two other methods.
    """
    def show_bids(self):
        """
        Shows all the bids present that are present and open in the system.
        """
        bids = self.get_bids()
        y = 50
        for item in bids:
            if self.isOpen(item) and self.isAvailable(item):
                bid_buttons = self.button_maker(self.frame)
                bid_buttons.config(text=item['subject']['description'],command = lambda bid_item = item, current_user = self.current_user: self.detailed_bid_view(bid_item, current_user), height="4", width="25")
                bid_buttons.place(x=20, y=y)
                subscribe_button = self.button_maker(self.frame)
                subscribe_button.config(text="Subscribe",command = lambda bid_item=item: self.subscription(bid_item), height="4", width="25")
                subscribe_button.place(x=400, y=y)
                y += 150

    def get_bids(self):
        """
        Gets all the bids that the tutor is subscribed to
        """
        return Bid_API.Bid().get()

    def detailed_bid_view(self, bid_item, current_user):
        """
        Allows one single bid to be viewed
        """
        SingleBidViewUI.singleBidViewUI(bid_item, current_user)

    def subscription(self, bid_item):
        subscribers = bid_item['additionalInfo']['bidSubscribers']
        if self.current_user in subscribers:
            return messagebox.showinfo("Uh oh..", "you have already subscribed to this bid")
        Bid().patch_bid_subscriber(bid_item, self.current_user)







