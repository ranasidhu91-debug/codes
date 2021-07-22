from tkinter import *
from tkinter import messagebox,simpledialog
from WidgetMakers import WidgetAbstract
from Details.user_details import User_Details
from Details.subject_details import Subject_Details as Subject
from API.Contract_API import Contract

class Newterms(WidgetAbstract):
    """
    This class creates a user interface when a student decides to renew the contract with the same tutor but using new terms
    """
    def __init__(self,root2,firstusername,secondusername,lesson,description):
        self.root2 = root2
        self.root = Toplevel()
        self.root.title("New Terms Signing")
        self.root.geometry("800x800")
        self.root.configure(bg="snow")
        self.root.resizable(False,False)
        self.firstusername = firstusername
        self.secondusername = secondusername
        self.lesson = lesson
        self.description = description
        self.default = None
        self.duration = None
        self.frame_generator()


    def frame_generator(self):
        """
        Generates the frame
        """
        self.firstPartyName = User_Details(self.firstusername).get_fullName()
        self.secondPartyName = User_Details(self.secondusername).get_fullName()

        self.__label_generator()


    def __label_generator(self):
        """
        Generates the labels
        """
        labels = ["RENEW NEW TERMS","First Party","Second Party","Lesson","Description","Time_Day","Sessions","Rate","Contract Duration"]
        details = [self.firstPartyName,self.secondPartyName,self.lesson,self.description]

        y = 100
        for i in labels:
            if i == "RENEW NEW TERMS":
                header = self.title(self.root)
                header.config(text="RENEW NEW TERMS", fg="black", bg="snow")
                header.place(x=400, y=50, anchor="center")
            else:
                label = self.label_maker(self.root)
                label.config(text=i)
                label.place(x=10, y=y)
                y += 50

        y = 100
        for i in range(len(labels) - 1):
            colons = self.colon_maker(self.root)
            colons.config(bg="snow")
            colons.place(x=250, y=y)
            y += 50

        y = 100

        for i in range(len(details)):
            label2 = self.label_maker(self.root)
            label2.config(text=details[i])
            label2.place(x=300, y=y)
            y += 50
        self.__entry_boxes()
        self.__button2()

    def __entry_boxes(self):
        """
        Generates the entry boxes
        """
        time_day = self.Entry_maker(self.root)
        self.time_day_var = StringVar()
        time_day.config(textvariable=self.time_day_var)
        time_day.place(x=300,y=315)

        session = self.Entry_maker(self.root)
        self.session_var = StringVar()
        session.config(textvariable=self.session_var)
        session.place(x=300,y=365)

        rate = self.Entry_maker(self.root)
        self.rate_var = StringVar()
        rate.config(textvariable=self.rate_var)
        rate.place(x=300, y=405)

        def time_day_input(*args):
            self.time_day_var.get()

        def sessions_input(*args):
            self.session_var.get()

        def rate_input(*args):
            self.rate_var.get()

        self.time_day_var.trace('w',time_day_input)
        self.session_var.trace('w',sessions_input)
        self.rate_var.trace('w',rate_input)

    def __button2(self):
        """
        Generates the options menu and the contract sign button
        """
        contract_change = StringVar()
        decision = ["Yes. I would like to change","No. 6 months would suffice"]
        contract_change.set("Default Contract Length is 6 Months. Change?")
        contract_change_options = OptionMenu(self.root, contract_change, *decision)
        contract_change_options.config(width=45,bd=0,bg="snow")
        contract_change_options.place(x=300,y= 455)

        choices = ["3", "6", "12", "24", "Custom"]
        duration_change = StringVar()
        duration_change.set("Select your duration:")
        duration_change_option = OptionMenu(self.root,duration_change,*choices)
        duration_change_option.config(width=45,bd=0,bg="snow",state="disabled")
        duration_change_option.place(x=300,y=480)

        sign_button = self.button_maker(self.root)
        sign_button.config(text="SIGN",state="disabled")
        sign_button.place(x=300, y=555, width=200, height=50)

        def selection(*args):
            if duration_change.get() == "Custom":
                duration = simpledialog.askinteger("Duration","Enter Duration in Months: ")
                if duration:
                    self.duration = duration
                    self.button_destroyed = True
                    sign_button.config(state="active",command=lambda :[(self.__sign_contract2()),self.__messageBox2(),self.root.destroy(),self.root2.deiconify()])
                    duration_change_option.config(state="disabled")
                    contract_change_options.config(state="disabled")
            else:
                self.duration = int(duration_change.get())
                self.button_destroyed = True
                sign_button.config(state="active",command=lambda : [(self.__sign_contract2()),self.__messageBox2(),self.root.destroy(),self.root2.deiconify()])


        def my_show(*args):
            if "Yes" in contract_change.get():
                duration_change_option.config(state="active")
                self.default = False
                sign_button.config(state="disabled")
            else:
                duration_change_option.config(state="disabled")
                self.default = True
                self.button_destroyed = True
                sign_button.config(state="active",command=lambda:[(self.__sign_contract2()),self.__messageBox2(),self.root.destroy(),self.root2.deiconify()])


        contract_change.trace('w',my_show)
        duration_change.trace('w',selection)

    def __sign_contract2(self):
        """
        Creates the contract instead of signing it as the tutor is the second person to sign the contract.
        """
        firstPartyID = User_Details(self.firstusername).get_userid()
        secondPartyID = User_Details(self.secondusername).get_userid()
        self.subjectID = Subject(self.lesson,self.description).get_subject_id()
        if self.default:
            month = 6
        else:
            month = self.duration
        Contract().post(firstPartyID, secondPartyID, self.subjectID, "Renewed Contract", self.session_var.get(), self.rate_var.get(),
                        self.time_day_var.get(), month)
    def __messageBox2(self):
        messagebox.showinfo("Congratulations","You Have Signed The Contract")

