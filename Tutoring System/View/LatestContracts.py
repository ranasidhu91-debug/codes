from tkinter import *
from tkinter import ttk
from WidgetMakers import WidgetAbstract
from Details.user_details import User_Details
from Details.contract_details import Contract_Details
from datetime import datetime
from ContractCreationUserInterface import ContractCreationUI

class Latest:
    """
    This class shows all the latest 5 contracts that the user has
    """
    def __init__(self,root2,firstpartyusername,secondpartyusername,lesson,description,contractNos = None):
        self.root2 = root2 #dashboard
        self.root = Toplevel()
        self.root.title("Latest Contracts")
        self.root.config(bg="snow2")
        self.root.resizable(False,False)
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",
                             background="#D3D3D3",
                             foreground="black",
                             rowheight=25,
                             fieldbackground="#D3D3D3"
                             )
        self.style.map('Treeview',background=[('selected','blue')])
        self.my_tree = ttk.Treeview(self.root)

        self.firstusername = firstpartyusername
        self.secondusername = secondpartyusername

        self.my_tree.pack(pady=10)
        self.lesson = lesson
        self.description = description

        self.root.geometry("725x300")
        self.contractNos = contractNos
        self.treeview_generator2()
        self.root.protocol("WM_DELETE_WINDOW",self.close_window)

    def treeview_generator2(self):
        """
        generates the frame to store the list of contracts
        """
        self.my_tree['columns'] = ["ContractID","Tutor","Subject","Expiry Date"]
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("ContractID",anchor=W,width=175)
        self.my_tree.column("Tutor",anchor=CENTER,width=175)
        self.my_tree.column("Subject",anchor=W,width=175)
        self.my_tree.column("Expiry Date",anchor=W,width=175)

        self.my_tree.heading("#0",text='',anchor=W)
        self.my_tree.heading("ContractID",text="ContractID",anchor=W)
        self.my_tree.heading("Tutor",text="Tutor",anchor=CENTER)
        self.my_tree.heading("Subject",text="Subject",anchor=W)
        self.my_tree.heading("Expiry Date",text="Expiry Date",anchor=W)

        self.my_tree.tag_configure('expired',background='tomato')

        self.__latest_contracts()

        def on_double_click(event):
            item_id = event.widget.focus()
            item = event.widget.item(item_id)
            contract_id = item['values'][0]
            contract = Contract_Details(contract_id)
            rate = contract.contract_rate()
            time_day = contract.time_day()
            sessions = contract.sessions()
            expiry = contract.get_expiryDate()
            expiryDate = datetime.strptime(expiry[:-1],'%Y-%m-%dT%H:%M:%S.%f')
            creation = contract.get_dateCreated()
            createdDate = datetime.strptime(creation[:-1],'%Y-%m-%dT%H:%M:%S.%f')
            duration = expiryDate - createdDate
            ContractCreationUI(self.root2,self.firstusername,self.secondusername,sessions,rate,time_day,self.lesson,self.description,renew=True)
            self.root.destroy()

        self.my_tree.bind("<Double-Button-1>", on_double_click)
        self.__if_view_latest()


    def __if_view_latest(self):
        """
        Generates the list of contracts
        """
        count = 0
        for i in self.__latest_contracts():
            time_string = i['expiryDate']
            expiry = datetime.strptime(time_string[:-1], '%Y-%m-%dT%H:%M:%S.%f')
            if expiry < datetime.now():
                self.my_tree.insert(parent='', index='end', iid=count, values=(
                i['id'], (i['secondParty']['givenName'] + " " + i['secondParty']['familyName']),
                (i['subject']['name'] + " " + ":" + " " + i['subject']['description']), expiry), tags=('expired',))
            else:
                self.my_tree.insert(parent='', index='end', iid=count, values=(
                i['id'], (i['secondParty']['givenName'] + " " + i['secondParty']['familyName']),
                (i['subject']['name'] + " " + ":" + " " + i['subject']['description']), expiry))

            count += 1

    def __latest_contracts(self):
        """
        returns the latest contracts
        """
        contracts = User_Details(WidgetAbstract.username).user_latest_contracts()
        return contracts

    def close_window(self):
        """
        closes the window
        """
        self.root2.deiconify()
        self.root.destroy()


