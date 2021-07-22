from tkinter import *
from tkinter import ttk
from API.Contract_API import Contract
from WidgetMakers import WidgetAbstract
from datetime import datetime
from tkinter import messagebox

class PendingUI:
    """
    This class ceates the UI that displays all the contracts that are pending for the tutor to be signed after the student renews or reuses an old contract.
    """
    def __init__(self,root2):
        self.root2 = root2
        self.root = Toplevel()
        self.root.title("Pending Contracts")
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
        self.pending_contracts = None
        self.my_tree.pack(pady=10)
        self.root.protocol("WM_DELETE_WINDOW",self.close_window)
        self.treeview_generator()

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

        self.my_tree.tag_configure('expired',background='tomato')

        self.__pending()

        def on_double_click(event):

            item_id = event.widget.focus()
            item = event.widget.item(item_id)
            contract_id = item['values'][0]
            Contract().signed(contract_id)
            messagebox.showinfo('Signed','Contract Signed')
            self.root.destroy()
            self.root2.deiconify()
        self.my_tree.bind("<Double-Button-1>",on_double_click)

    def __pending(self):
        """"
        The contracts that are pending are displayed
        """
        count = 0
        pending = self.pending()
        for i in pending:
            time_string = i['expiryDate']
            expiry = datetime.strptime(time_string[:-1], '%Y-%m-%dT%H:%M:%S.%f')
            self.my_tree.insert(parent='', index='end', iid=count, values=(
                i['id'], (i['firstParty']['givenName'] + " " + i['firstParty']['familyName']),
                (i['subject']['name'] + " " + ":" + " " + i['subject']['description']), expiry))
            count += 1


    def pending(self):
        """
        Gets are the pending contracts
        """
        pending = Contract().pending_contracts(WidgetAbstract.username)
        return pending

    def close_window(self):
        self.root.destroy()
        self.root2.deiconify()


