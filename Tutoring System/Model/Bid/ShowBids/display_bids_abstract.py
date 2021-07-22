import tkinter as tk
from abc import ABC, abstractmethod
from datetime import datetime

from Details.user_details import User_Details


class DisplayBids(ABC):
    """
    An interface class that contains concrete methods to show all the open and available bids.
    """
    def __init__(self, frame, current_user):
        """
        creates the View and gets the username
        """
        self.frame = frame
        self.current_user = current_user
        self.user_details = User_Details(self.current_user).get_user_in_system()

    @abstractmethod
    def show_bids(self):
        """
        Shows all the bids present that are present and open in the system.
        """
        pass


    @abstractmethod
    def get_bids(self):
        """
        An abstract method that is implemented when another class implements this class.
        """
        pass

    @abstractmethod
    def detailed_bid_view(self, bid_item, current_user):
        """
        An abstract method that is implemented when another class implements this class.
        """
        pass

    @abstractmethod
    def subscription(self, bid_item):
        """
        :param bid_item:
        :return:
        """
        pass

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
