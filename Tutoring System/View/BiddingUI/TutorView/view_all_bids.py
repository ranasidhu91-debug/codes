from tkinter import *
from Model.Bid.ShowBids.tutor_bids import TutorBids
from WidgetMakers import WidgetAbstract

class ViewAllBids(WidgetAbstract):
    """
    This class allows the tutor to view all the bids that are active in the system so far.
    """
    def __init__(self,root2):
        """
        This constructor class takes in a username and creates the View to view all the bids present.
        """
        self.root2 = root2
        self.root = Toplevel()
        self.root.geometry("400x400")
        self.root.resizable(True,True)
        self.show_all_bids()
        self.root.protocol("WM_DELETE_WINDOW", self.close_button)

    def show_all_bids(self):
        """
        This method allows all the bids that are active to be displayed
        """
        TutorBids(self.root,WidgetAbstract.username).show_bids()

    def close_button(self):
        self.root.destroy()
        self.root2.deiconify()


# if __name__ == '__main__':
#     root = tk.Tk()
#     ViewAllBids(root)
#     root.mainloop()