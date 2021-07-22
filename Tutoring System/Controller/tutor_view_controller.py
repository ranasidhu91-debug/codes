from tkinter import NE, TOP

from AllContracts import All_Contracts
from BiddingUI.TutorView import view_all_bids
from BiddingUI.TutorView.view_subscribed_bidsUI import ViewSubscribedBidsUI
from Dashboard import Dashboard
from ExpiringContracts import ExpiringUI
from PendingContractUI import PendingUI
from WidgetMakers import WidgetAbstract


class TutorViewController:
    def __init__(self, dashboard: Dashboard):
        """
        Tutor view controller class which generates the dashboard for the tutor when
        a tutor is detected in the system
        :param dashboard: an instance of the dashboard class is passed
        """
        self.dashboard = dashboard
        self.tutor_frame()

    def tutor_frame(self):
        """
        the method that generates all the labels, buttons etc which the tutor can interact with
        """

        self.dashboard.title_header = self.dashboard.title(self.dashboard.frame)
        self.dashboard.title_header.config(text="Tutoring System")
        self.dashboard.title_header.pack()

        if self.dashboard.expiring_contracts:
            notification_button = self.dashboard.button_maker(self.dashboard.frame)
            # edit this later
            notification_button.config(text="Some contracts are about to expire",font=12,bd=0,fg="#d77337",command=lambda :[ExpiringUI(self.dashboard.root,self.dashboard.expiring_contracts)])
            notification_button.pack(side=TOP,anchor=NE)

        self.dashboard.pending_button = self.dashboard.button_maker(self.dashboard.frame)
        self.dashboard.pending_button.config(text="Pending Contracts", wraplength=120,command=lambda: [PendingUI(self.dashboard.root), self.dashboard.root.withdraw()])
        self.dashboard.pending_button.pack()

        self.dashboard.view_subscribed_bids = self.dashboard.button_maker(self.dashboard.frame)
        self.dashboard.view_subscribed_bids.config(text="View My subscribed bids", command=lambda:[ViewSubscribedBidsUI(self.dashboard.username,self.dashboard.root),self.dashboard.root.withdraw()])
        self.dashboard.view_subscribed_bids.pack()

        self.dashboard.view_all_bids_button = self.dashboard.button_maker(self.dashboard.frame)
        self.dashboard.view_all_bids_button.config(text="View All Student Bids", command=lambda:[view_all_bids.ViewAllBids(self.dashboard.root),self.dashboard.root.withdraw()])
        self.dashboard.view_all_bids_button.pack()

        self.dashboard.all_contracts= self.dashboard.button_maker(self.dashboard.frame)
        self.dashboard.all_contracts.config(text="View All Contracts", command=lambda : [(All_Contracts(self.dashboard.root, self.dashboard.user_details.isTutor())), self.dashboard.root.withdraw()])
        self.dashboard.all_contracts.pack()



