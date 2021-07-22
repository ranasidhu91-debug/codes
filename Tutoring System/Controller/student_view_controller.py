from tkinter import *

from AllContracts import All_Contracts
from BiddingUI.StudentView.OpenBidUI import OpenBidUI
from BiddingUI.StudentView.ViewStudentBids import ViewStudentBids
from BiddingUI.TutorView import view_all_bids
from BiddingUI.TutorView.view_subscribed_bidsUI import ViewSubscribedBidsUI
from Dashboard import Dashboard
from ExpiringContracts import ExpiringUI
from PendingContractUI import PendingUI
from WidgetMakers import WidgetAbstract


class StudentViewController:
    def __init__(self, dashboard: Dashboard):
        """
        Student view controller class which generates the dashboard for the student when
        a student is detected in the system
        :param dashboard: an instance of the dashboard class is passed
        """
        self.dashboard = dashboard
        self.student_frame()

    def student_frame(self) -> None:
        """
        the method that generates all the labels, buttons etc which the student can interact with
        """

        self.dashboard.title_header = self.dashboard.title(self.dashboard.frame)
        self.dashboard.title_header.config(text="Tutoring System")
        self.dashboard.title_header.pack()

        if self.dashboard.expiring_contracts:
            self.dashboard.notification_button = self.dashboard.button_maker(self.dashboard.frame)
            # edit this later
            self.dashboard.notification_button.config(text="Some contracts are about to expire",font=12,bd=0,fg="#d77337",command=lambda :[ExpiringUI(self.dashboard.root,self.dashboard.isTutor,self.dashboard.expiring_contracts)])
            self.dashboard.notification_button.pack(side=TOP,anchor=NE)

        self.dashboard.bidding_button = self.dashboard.button_maker(self.dashboard.frame)
        self.dashboard.bidding_button.config(text="Make A Bid", command=lambda: [OpenBidUI(self.dashboard.root), self.dashboard.root.withdraw()])
        self.dashboard.bidding_button.pack()

        self.dashboard.view_my_bids = self.dashboard.button_maker(self.dashboard.frame)
        self.dashboard.view_my_bids.config(text="View My Bids",command=lambda: [ViewStudentBids(self.dashboard.root), self.dashboard.root.withdraw()])
        self.dashboard.view_my_bids.pack()

        self.dashboard.all_contracts= self.dashboard.button_maker(self.dashboard.frame)
        self.dashboard.all_contracts.config(text="View All Contracts", command=lambda : [(All_Contracts(self.dashboard.root, self.dashboard.user_details.isTutor())), self.dashboard.root.withdraw()])
        self.dashboard.all_contracts.pack()