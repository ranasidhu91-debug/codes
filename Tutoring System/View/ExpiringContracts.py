from tkinter import *
from tkinter import ttk
from WidgetMakers import WidgetAbstract


class ExpiringUI(WidgetAbstract):
    """
    This class shows all the contracts that are about to expire within the month.
    """
    def __init__(self,root2,istutor,contracts):
        self.root2 = root2
        self.contracts = contracts
        self.istutor = istutor
        self.root = Toplevel()
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
        self.treeview_generator()
        self.root.protocol("WM_DELETE_WINDOW",self.close_window)

    def treeview_generator(self):
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

        self.show_contracts()


    def show_contracts(self):
        count = 0
        for i in self.contracts:
            if self.istutor:
                self.my_tree.insert(parent='', index='end', iid=count, values=(i['id'], (i['firstParty']['givenName'] + " " + i['firstParty']['familyName']),(i['subject']['name'] + " " + ":" + " " + i['subject']['description'])))
            else:
                self.my_tree.insert(parent='', index='end', iid=count, values=(
                i['id'], (i['secondParty']['givenName'] + " " + i['secondParty']['familyName']),
                (i['subject']['name'] + " " + ":" + " " + i['subject']['description'])))
            count += 1

    def close_window(self):
        self.root.destroy()
        self.root2.deiconify()

