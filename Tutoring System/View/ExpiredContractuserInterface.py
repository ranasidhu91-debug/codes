from tkinter import *
from DifferentTutorSameTerms import DifferentTutSameTermsUI
from NewTermsUI import Newterms
from WidgetMakers import WidgetAbstract
from LatestContracts import Latest
from Details.user_details import User_Details
class ExpiredContracts(WidgetAbstract):
    """
    This contract shows all the contracts that have expired.
    """
    def __init__(self,root2,contract):
        self.root2 = root2 # dashboard
        self.root = Toplevel()
        self.root.geometry("800x700")
        self.contract = contract
        self.root.title("Expired Contract"+ ":" + " " + self.contract.get_contract_id())
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        # self.id = id
        self.frame_generator()


    def frame_generator(self):
        labels = ["CONTRACT RENEWAL", "First Party", "Second Party", "Lesson", "Description","Session","Time_Day","Rate"]
        details = self.contract_details()
        y = 100
        for i in labels:
            if i == "CONTRACT RENEWAL":
                header = self.title(self.root)
                header.config(text=i,fg="black",bg="snow")
                header.place(x=400,y=50,anchor="center")
            else:
                label = self.label_maker(self.root)
                label.config(text=i)
                label.place(x=10,y=y)
                y+= 50

        y = 100
        for i in range(len(labels)-1):
            colons = self.colon_maker(self.root)
            colons.config(bg="snow")
            colons.place(x=250,y=y)
            y += 50

        y = 100
        for i in details:
            label2 = self.label_maker(self.root)
            label2.config(text=i)
            label2.place(x=300,y=y)
            y+= 50
        self.buttons()


    def contract_details(self):
        self.bid_id = self.contract.bid()
        self.session = self.contract.sessions()
        self.time_day = self.contract.time_day()
        self.rate = self.contract.contract_rate()
        details = [self.contract.firstPartyFullName(),self.contract.secondPartyFullName(),self.contract.get_lesson(),self.contract.get_description(),
                   self.session,self.time_day,self.rate]
        return details

    def buttons(self):
        same = self.button_maker(self.root)
        same.config(text="Same Tutor Previous Contracts",wraplength=160,command = lambda :[self.previous_contracts(),self.root.destroy()])
        same.place(x=50,y=500)

        same_tutor = self.button_maker(self.root)
        same_tutor.config(text="Same Tutor New Terms",wraplength=160,command = lambda :[self.same_new_terms(),self.root.destroy()])
        same_tutor.place(x=200,y=500)

        new_tutor_same_terms = self.button_maker(self.root)
        new_tutor_same_terms.config(text="Different Tutor Same Terms",wraplength=160,command = lambda :[self.different_tutor_same_terms(),self.root.destroy()])
        new_tutor_same_terms.place(x=350,y=500)


    def previous_contracts(self):
        Latest(self.root2,self.contract.get_firstParty()['userName'],self.contract.get_secondParty()['userName'],self.contract.get_lesson(),self.contract.get_description())

    def same_new_terms(self):
        Newterms(self.root2,self.contract.get_firstParty()['userName'],self.contract.get_secondParty()['userName'],self.contract.get_lesson(),self.contract.get_description())

    def different_tutor_same_terms(self):
        DifferentTutSameTermsUI(self.root2,self.contract.get_firstParty()['userName'],self.contract.get_lesson(),self.contract.get_description(),self.session,self.time_day,self.rate)

    def close_window(self):
        self.root.destroy()