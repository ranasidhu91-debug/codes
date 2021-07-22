from abc import ABC
from datetime import datetime
from API.Bid_API import Bid
from View.BiddingUI.TutorView import SingleBidViewUI
from WidgetMakers import WidgetAbstract


class ViewSubscribedBids(ABC,WidgetAbstract):
    def __init__(self, frame, username):
        self.frame = frame
        self.current_user = username
        self.button_dict = {}

    def show_bids(self):
        """
        Shows all the bids present that are present and open in the system.
        """
        # bids = self.get_bids()
        y=50
        for button,item in self.button_dict.items():
            if self.isOpen(item) and self.isAvailable(item):
                # student_bids = self.button_maker(self.frame)
                button.config(text=item['subject']['description'],command=lambda arg1=item, arg2=self.current_user:self.detailed_bid_view(arg1, arg2),height="4", width="25")
                button.place(x=30, y=y)
                y+=150
        # self.frame.after(1000, self.show_bids())

    def get_bids(self):
        all_bids = Bid().get()
        user_subscribed_bids = []
        for item in all_bids:
            bid_subscribers = item['additionalInfo']['bidSubscribers']
            for subscriber in bid_subscribers:
                if self.current_user == subscriber:
                    user_subscribed_bids.append(item)
        return user_subscribed_bids

    def detailed_bid_view(self, bid_item, current_user):
        """
        Allows one single bid to be viewed
        """
        SingleBidViewUI.singleBidViewUI(bid_item, current_user)

    def isOpen(self, item):
        """
        Determines if the bid is still open
        """
        current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        bid_close_date = item['dateClosedDown']
        return current_time < bid_close_date

    def isAvailable(self, item):
        """
        Determines if the bid is still available
        """
        return item['additionalInfo']['bidAvailability']

    def create_buttons(self):
        if self.button_dict is not None:
            for widget in self.frame.winfo_children():
                widget.destroy()

        self.button_dict = {}
        bids_array = self.get_bids()
        for item in bids_array:
            self.button_dict[self.button_maker(self.frame)] = item

