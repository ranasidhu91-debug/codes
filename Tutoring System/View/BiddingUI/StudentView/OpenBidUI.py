#
from tkinter import *
from tkinter import messagebox,simpledialog

from API import Subject_API as SA
from Details import user_details
from Model.Bid import Bid_Creation
from WidgetMakers import WidgetAbstract


class OpenBidUI(WidgetAbstract):
    """
    This class creates the View that would allow the student to input details regarding the subject help is needed in.
    """
    def __init__(self,root2):
        """
        Constructor class that creates the View  and obtains the details of the user by calling the user_details class
        """
        self.root2 = root2
        self.root = Toplevel()
        self.__user_details = user_details.User_Details(WidgetAbstract.username)
        self.root.geometry("900x450")
        self.root.title("Bid For A Tutor")
        self.__frame = Frame(self.root)
        self.root.resizable(True,True)
        self.__frame.place(x=5, y=5,width=890,height=440)
        self.lesson = None
        self.lesson_description = None
        self.time_day = None
        self.sessions = None
        self.rate = None
        self.submit_button = None
        self.frame_generator()
        self.bid_description()
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.isOthers = None

    def frame_generator(self):

        texts = ["Place Your Bid","Required lesson","Number of sessions/week","Preferred Time and Day","Rate(/hour or /session)"]
        x = 10
        y = 100
        font = "Goudy Old Style",20,"bold"
        for i in texts:
            if i == "Place Your Bid":
                # title_header = self.title(self.__frame)
                title_header = self.label_maker(self.__frame)
                title_header.config(text="Place Your Bid",font=("Times",35,"bold"))
                title_header.pack()
            else:
                Label(self.__frame,text=i,font=(font)).place(x=x,y=y)
                # Label(self.root, text=i, font=(font)).place(x=x, y=y)
                y += 50

        y=100
        for i in range(4):
            self.colon_maker(self.__frame).place(x=300,y=y)
            # self.colon_maker(self.root).place(x=300, y=y)
            y += 50

    def all_subjects(self):
        subjects = SA.Subject_API().get_all_subjects()
        subjects.append("Other")
        return subjects

    def bid_description(self):
        selection = StringVar()
        choices = self.all_subjects()
        selection.set("Select your subject and the description")
        a = OptionMenu(self.__frame,selection,*choices)
        # a = OptionMenu(self.root, selection, *choices)
        a.config(width=45)
        a.place(x=350,y=100)

        other_button = self.button_maker(self.__frame)
        # other_button = self.button_maker(self.root)
        other_button.config(text="Click Me",state="disabled")
        other_button.place(x=675,y=100,height=30,width=80)

        self.submit_button = self.button_maker(self.__frame)
        # self.submit_button = self.button_maker(self.root)
        self.submit_button.config(text="Submit Bid",state="disabled",width=24, height="2")
        self.submit_button.place(x=400, y=400)
        def my_show(*args):
            if selection.get() == "Other":
                other_button.config(state="active",command=other_description)
            else:
                if "Other" in selection.get():
                    self.isOthers = True
                    word = self.__words(selection.get())
                    self.lesson = word[0]
                    self.lesson_description = word[1]
                    other_button.config(state="disabled")
                else:
                    self.isOthers = False
                    word = self.__words(selection.get())
                    self.lesson = word[0]
                    self.lesson_description = word[1].lstrip()
                    other_button.config(state="disabled")
        selection.trace('w',my_show)

        def other_description():
            lesson = simpledialog.askstring("Lessons","Please Enter Your Lesson")
            if lesson:
                description = simpledialog.askstring("Description","Please Enter Your Description")
                selection.set("Other" + " " + ":" + " " + lesson + " " + description)

        sessions_string = StringVar()
        sessions = self.Entry_maker(self.__frame)
        # sessions = self.Entry_maker(self.root)
        sessions.config(textvariable=sessions_string)
        sessions.place(x=350, y=165)

        time_day_string = StringVar()
        time_day = self.Entry_maker(self.__frame)
        # time_day = self.Entry_maker(self.root)
        time_day.config(state="disabled",textvariable=time_day_string)
        time_day.place(x=350, y=215)

        rate_string = StringVar()
        rate = self.Entry_maker(self.__frame)
        # rate = self.Entry_maker(self.root)
        rate.config(state="disabled",textvariable=rate_string)
        rate.place(x=350, y=265)

        def sessions(*args):
            if sessions_string.get():
                time_day.config(state="normal")
                self.sessions = sessions_string.get()
            else:
                time_day.config(state="disabled")
        def preference(*args):
            if time_day_string.get():
                rate.config(state="normal")
                self.time_day = time_day_string.get()
            else:
                rate.config(state="disabled")
        def rate_activation(*args):
            if rate_string.get():
                self.rate = rate_string.get()
                self.submit_button.config(state="active")
            else:
                self.submit_button.config(state="disabled")

        sessions_string.trace('w',sessions)
        time_day_string.trace('w',preference)
        rate_string.trace('w',rate_activation)
        self.send_bid()

    def __words(self,words):
        """
        this method gets the data from required lesson and returns  a list. The first parameter is the lesson and the second
        parameter is the description
        :return: a list of Subject[Lesson][Description]
        """

        if "Other" in words:
            variable = words.replace('Other : ',"")
            variable = variable.split(' ',1)
        else:
            word = words.lstrip()
            word = word.replace('(','')
            word = word.replace(')','')
            word = word.replace("'","")
            word = word.replace(',',' ')
            variable = word.split(' ',1)
        return variable

    def send_bid(self):
        self.submit_button.config(command=lambda:[Bid_Creation.studentBidCreation(WidgetAbstract.username,self.lesson,self.lesson_description,self.time_day,self.sessions,self.isOthers,self.rate).createBid(),self.__show_message(),self.root.destroy(),self.root2.deiconify()],width=24, height="2")


    def __show_message(self):
        """
        If the bid submission is successful, this message is displayed.
        """
        messagebox.showinfo("Bid Submission", "Your Bid request has been submitted")

    def close_window(self):
        self.root2.deiconify()
        self.root.destroy()


