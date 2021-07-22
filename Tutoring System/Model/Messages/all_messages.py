import tkinter as tk

from API.Bid_API import Bid
from abc import ABC, abstractmethod


class AllMessages(ABC):
    def __init__(self, first_party, second_party, root, bid, current_user, tutor_offer):
        self.first_party = first_party #bid initiator
        self.second_party = second_party
        self.root = root
        self.bid = bid
        self.current_user = current_user
        self.tutor_offer = tutor_offer


    def display_all_messages(self):
        get_bid = Bid().get_bid_messages(self.bid)
        bid_messages = get_bid['messages']
        column = 100
        last = len(bid_messages) - 1
        for i in range(len(bid_messages)):
            if self.is_first_party(bid_messages[last]) or self.is_second_party(bid_messages[last]):
                tk.Label(self.root, text=bid_messages[last]['content'] + " Posted By: " + bid_messages[last]['poster']['userName']).place(x=100, y=column)
                last -= 1
                column+=50

    @abstractmethod
    def is_first_party(self, message):
        # print(self.current_user)
        # print(message)
        # return self.current_user == message['additionalInfo']['firstParty']
        pass

    @abstractmethod
    def is_second_party(self, message):
        # return self.current_user == message['additionalInfo']['secondParty']
        pass

