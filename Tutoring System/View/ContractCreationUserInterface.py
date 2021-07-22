from tkinter import *
from tkinter import messagebox,simpledialog
from WidgetMakers import WidgetAbstract
from Details.user_details import User_Details
from Details.subject_details import Subject_Details as Subject
from API.Contract_API import Contract


class ContractCreationUI(WidgetAbstract):
    """"
    This class would create the UI to sign the contract
    """
    def __init__(self,root2,firstPartyUsername, secondPartyUsername,sessions,rate,time_day,subject_lesson,subject_description,bidID=None,renew=None):
        self.root2 = root2 # dashboard
        self.root = Toplevel()
        self.root.title("Contract Signing")
        self.root.geometry("800x600")
        self.root.configure(bg="snow")
        self.root.resizable(False,False)
        self.firstPartyUsername = firstPartyUsername
        self.secondPartyUsername = secondPartyUsername
        self.lesson = subject_lesson
        self.description = subject_description
        self.sessions = sessions
        self.rate = rate
        self.time_day = time_day
        self.bidID = bidID
        self.default = False
        self.duration = None
        self.button_destroyed = False
        self.renew=renew
        self.frame_generator()


    def frame_generator(self):
        self.firstPartyName = User_Details(self.firstPartyUsername).get_fullName()
        self.secondPartyName = User_Details(self.secondPartyUsername).get_fullName()
        self.__label_generator()



    def __label_generator(self):
        contract_description = [self.firstPartyName, self.secondPartyName, self.lesson, self.description, self.rate,
                                self.bidID]
        if not self.renew:
            labels = ["CONTRACT SIGNING","First Party","Second Party","Lesson","Description","Rate","Bid ID","Contract Duration"]

            y = 100
            for i in labels:
                if i == "CONTRACT SIGNING":
                    header = self.title(self.root)
                    header.config(text="CONTRACT SIGNING",fg="black",bg="snow")
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

            for i in contract_description:
                label2 = self.label_maker(self.root)
                label2.config(text=i)
                label2.place(x=300,y=y)
                y+= 50
            self.__buttons()
        else:
            labels = ["CONTRACT RENEWAL", "First Party", "Second Party", "Lesson", "Description", "Rate",
                      "Contract Duration"]

            y = 100
            for i in labels:
                if i == "CONTRACT RENEWAL":
                    header = self.title(self.root)
                    header.config(text="CONTRACT RENEWAL",fg="black",bg="snow")
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
            for i in contract_description:
                label2 = self.label_maker(self.root)
                label2.config(text=i)
                label2.place(x=300,y=y)
                y+= 50
            self.__button2()


    def __button2(self):
        contract_change = StringVar()
        decision = ["Yes. I would like to change","No. 6 months would suffice"]
        contract_change.set("Default Contract Length is 6 Months. Change?")
        contract_change_options = OptionMenu(self.root, contract_change, *decision)
        contract_change_options.config(width=45,bd=0,bg="snow")
        contract_change_options.place(x=300,y= 360)

        choices = ["3", "6", "12", "24", "Custom"]
        duration_change = StringVar()
        duration_change.set("Select your duration:")
        duration_change_option = OptionMenu(self.root,duration_change,*choices)
        duration_change_option.config(width=45,bd=0,bg="snow",state="disabled")
        duration_change_option.place(x=300,y=385)

        sign_button = self.button_maker(self.root)
        sign_button.config(text="SIGN",state="disabled")
        sign_button.place(x=300, y=500, width=200, height=50)

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

    def __buttons(self):
        contract_change = StringVar()
        decision = ["Yes. I would like to change","No. 6 months would suffice"]
        contract_change.set("Default Contract Length is 6 Months. Change?")
        contract_change_options = OptionMenu(self.root, contract_change, *decision)
        contract_change_options.config(width=45,bd=0,bg="snow")
        contract_change_options.place(x=300,y= 405)

        choices = ["3", "6", "12", "24", "Custom"]
        duration_change = StringVar()
        duration_change.set("Select your duration:")
        duration_change_option = OptionMenu(self.root,duration_change,*choices)
        duration_change_option.config(width=45,bd=0,bg="snow",state="disabled")
        duration_change_option.place(x=300,y=430)

        create_contract_button = self.button_maker(self.root)
        create_contract_button.config(text="CREATE CONTRACT",state="disabled")
        create_contract_button.place(x=300, y=500, width=200, height=50)

        def selection(*args):
            if duration_change.get() == "Custom":
                duration = simpledialog.askinteger("Duration","Enter Duration in Months: ")
                if duration:
                    self.duration = duration
                    self.button_destroyed = True
                    create_contract_button.config(state="active",command=lambda :[(self.__create_contract()),self.__messageBox1(),duration_change_option.config(state="disabled"),contract_change_options.config(state="disabled"),self.__sign_button(),create_contract_button.destroy()])
                    duration_change_option.config(state="disabled")
                    contract_change_options.config(state="disabled")
            else:
                self.duration = int(duration_change.get())
                self.button_destroyed = True
                create_contract_button.config(state="active",command=lambda : [(self.__create_contract()),self.__messageBox1(),duration_change_option.config(state="disabled"),contract_change_options.config(state="disabled"),self.__sign_button(),create_contract_button.destroy()])


        def my_show(*args):
            if "Yes" in contract_change.get():
                duration_change_option.config(state="active")
                self.default = False
                create_contract_button.config(state="disabled")
            else:
                duration_change_option.config(state="disabled")
                self.default = True
                self.button_destroyed = True
                create_contract_button.config(state="active",command=lambda:[(self.__create_contract()),self.__messageBox1(),duration_change_option.config(state="disabled"),contract_change_options.config(state="disabled"),self.__sign_button(),create_contract_button.destroy()])


        contract_change.trace('w',my_show)
        duration_change.trace('w',selection)


    def __sign_contract2(self):
        firstPartyID = User_Details(self.firstPartyUsername).get_userid()
        secondPartyID = User_Details(self.secondPartyUsername).get_userid()
        self.subjectID = Subject(self.lesson,self.description).get_subject_id()
        if self.default:
            month = 6
        else:
            month = self.duration
        WidgetAbstract.student_signed = True
        Contract().post(firstPartyID, secondPartyID, self.subjectID, self.bidID, self.sessions, self.rate,
                        self.time_day, month)

    def __create_contract(self):
        firstPartyID = User_Details(self.firstPartyUsername).get_userid()
        secondPartyID = User_Details(self.secondPartyUsername).get_userid()
        self.subjectID = Subject(self.lesson,self.description).get_subject_id()
        if self.default:
            month = 6
        else:
            month = self.duration
        Contract().post(firstPartyID,secondPartyID,self.subjectID,self.bidID,self.sessions,self.rate,self.time_day,month)



    def __sign_button(self):
        if self.button_destroyed:
            sign_button = self.button_maker(self.root)
            sign_button.config(text="SIGN",command=lambda :[self.__sign_contract(),self.__messageBox2(),self.root.destroy()])
            sign_button.place(x=300, y=500, width=200, height=50)

    def __sign_contract(self):
        id = Contract().get_single_contract_id(self.firstPartyUsername,self.secondPartyUsername,self.subjectID)
        Contract().signed(id)

    def __messageBox1(self):
        messagebox.showinfo("Success","You Have Created The Contract")

    def __messageBox2(self):
        messagebox.showinfo("Congratulations","You Have Signed The Contract")