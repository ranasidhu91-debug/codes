from abc import ABC
from tkinter import *
from Model.Bid.ShowBids.view_subscribed_bids import ViewSubscribedBids
from WidgetMakers import WidgetAbstract


class ViewSubscribedBidsUI(WidgetAbstract, ABC):
    def __init__(self, username,root):
        """
        This constructor class takes in a username and creates the View to view all the bids present.
        """
        self.root2 = root
        self.__username = username
        self.root = Toplevel()
        self.root.title("My subscribed bids")
        self.root.geometry("1280x720")
        self.bid_buttons = ViewSubscribedBids(self.root,self.__username)
        self.root.after(0, self.show_subscribed_bids)
        self.root.protocol("WM_DELETE_WINDOW",self.close_window)

    def show_subscribed_bids(self):
        """
        This method allows all the bids that are active to be displayed
        """
        self.bid_buttons.create_buttons()
        self.bid_buttons.show_bids()
        self.root.after(10000, self.show_subscribed_bids)


    def close_window(self):
        self.root.destroy()
        self.root2.deiconify()
