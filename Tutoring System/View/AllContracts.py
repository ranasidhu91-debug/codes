
from tkinter import *
from tkinter import ttk
from WidgetMakers import WidgetAbstract

from Details.contract_details import Contract_Details
from datetime import datetime
from ExpiredContractuserInterface import ExpiredContracts
from Contract_API import Contract

class All_Contracts(WidgetAbstract):
    """
    This class shows all the contracts the user has ever signed.
    """
    def __init__(self,root2,isTutor,contractNos = None):
        self.root2 = root2 #dashboard
        self.root = Toplevel()
        self.root.title("All Contracts")
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

        self.my_tree.pack(pady=10)
        self.isTutor = isTutor

        self.root.geometry("725x300")
        self.contractNos = contractNos
        self.root.protocol("WM_DELETE_WINDOW",self.close_window)
        self.treeview_generator1()

    def treeview_generator1(self):
        self.my_tree['columns'] = ["ContractID","Party","Subject","Expiry Date"]
        self.my_tree.column("#0",width=0,stretch=NO)
        self.my_tree.column("ContractID",anchor=W,width=175)
        self.my_tree.column("Party",anchor=CENTER,width=175)
        self.my_tree.column("Subject",anchor=W,width=175)
        self.my_tree.column("Expiry Date",anchor=W,width=175)

        self.my_tree.heading("#0",text='',anchor=W)
        self.my_tree.heading("ContractID",text="ContractID",anchor=W)
        self.my_tree.heading("Party",text="Party",anchor=CENTER)
        self.my_tree.heading("Subject",text="Subject",anchor=W)
        self.my_tree.heading("Expiry Date",text="Expiry Date",anchor=W)

        self.my_tree.tag_configure('expired',background='tomato')

        self.__if_view_all()

        def on_double_click(event):
            if not self.isTutor:
                item_id = event.widget.focus()
                item = event.widget.item(item_id)
                contract_id = item['values'][0]
                contract = Contract_Details(contract_id)
                contract_expiry = contract.get_expiryDate()
                con_expiry = datetime.strptime(contract_expiry[:-1],'%Y-%m-%dT%H:%M:%S.%f')
                if con_expiry < datetime.now():
                    ExpiredContracts(self.root2,contract)
                    self.root.destroy()
                    # self.frame.destroy()
                else:
                    pass
        self.my_tree.bind("<Double-Button-1>",on_double_click)

    def __if_view_all(self):
        count = 0
        for i in self.__all_contracts():
            time_string = i['expiryDate']
            expiry = datetime.strptime(time_string[:-1], '%Y-%m-%dT%H:%M:%S.%f')
            if expiry < datetime.now():
                if self.isTutor:
                    self.my_tree.insert(parent='', index='end', iid=count, values=(
                        i['id'], (i['firstParty']['givenName'] + " " + i['firstParty']['familyName']),
                        (i['subject']['name'] + " " + ":" + " " + i['subject']['description']), expiry),
                                        tags=('expired',))
                else:
                    self.my_tree.insert(parent='', index='end', iid=count, values=(
                    i['id'], (i['secondParty']['givenName'] + " " + i['secondParty']['familyName']),
                    (i['subject']['name'] + " " + ":" + " " + i['subject']['description']), expiry), tags=('expired',))
            else:
                if self.isTutor:
                    self.my_tree.insert(parent='', index='end', iid=count, values=(
                        i['id'], (i['firstParty']['givenName'] + " " + i['firstParty']['familyName']),
                        (i['subject']['name'] + " " + ":" + " " + i['subject']['description']), expiry))
                else:
                    self.my_tree.insert(parent='', index='end', iid=count, values=(
                    i['id'], (i['secondParty']['givenName'] + " " + i['secondParty']['familyName']),
                    (i['subject']['name'] + " " + ":" + " " + i['subject']['description']), expiry))
            count += 1


    def __all_contracts(self):
        return Contract().all_contracts_by_user(WidgetAbstract.username)

    def close_window(self):
        self.root.destroy()
        self.root2.deiconify()



