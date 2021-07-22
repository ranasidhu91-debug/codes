from tkinter import Toplevel
from Model.Bid.ShowBids import user_initiated_bids
from WidgetMakers import WidgetAbstract


class ViewStudentBids(WidgetAbstract):
    """
    A class to view student bids.
    """
    def __init__(self,root2):
        """
        Constructor that creates the View and calls the show_student_bids method to display the bids made by student.
        """
        self.root2 = root2
        self.root = Toplevel()
        self.root.geometry("1280x720")
        self.show_student_bids()
        self.root.protocol("WM_DELETE_WINDOW",self.close_button)
    def show_student_bids(self):
        """
        Shows the bids created by the student.
        """
        student_bids = user_initiated_bids.UserInitiatedBids(self.root, WidgetAbstract.username)
        student_bids.show_bids()

    def close_button(self):
        self.root.destroy()
        self.root2.deiconify()
