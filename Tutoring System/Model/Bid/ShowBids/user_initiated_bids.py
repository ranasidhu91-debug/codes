from abc import ABC

from API import User_api
from View.BiddingUI.StudentView import single_bid_view_student
from .display_bids_abstract import DisplayBids

from WidgetMakers import WidgetAbstract

class UserInitiatedBids(DisplayBids, ABC,WidgetAbstract):
    """
    AS class that implements the DisplayBids interface and creates it's own concrete
    """
    def show_bids(self):
        """
        Shows all the bids present that are present and open in the system.
        """
        bids = self.get_bids()
        y=50
        for item in bids:
            if self.isOpen(item) and self.isAvailable(item):
                bid_buttons = self.button_maker(self.frame)
                bid_buttons.config(text=item['subject']['description'],command=lambda arg=item, current_user=self.current_user: self.detailed_bid_view(arg, current_user), height="4", width="25")
                bid_buttons.place(x=30, y=y)
                y+=140

    def get_bids(self):
        """
        This method returns all the bids created by a specific user
        """
        return User_api.User().get_user_initiated_bids(self.current_user)['initiatedBids']

    def detailed_bid_view(self, bid_item, current_user):
        """
        This method allows a bid to be viewed in more detail
        """
        single_bid_view_student.SingleBidViewStudent(bid_item, current_user)

    def subscription(self, bid_item):
        pass

    # def back(self):
    #     back_button = self.button_maker(self.root)
    #     back_button.config(text="Back",command=lambda :[self.root.destroy(),self.root2.deiconify()])
    #     back_button.pack()
    #
    #
