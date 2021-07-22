from API.Competency_API import Competency
from tkinter import *
from WidgetMakers import WidgetAbstract
from Details.user_details import User_Details
from API.Contract_API import Contract
from Details.subject_details import Subject_Details
from tkinter import simpledialog
from tkinter import messagebox

class DifferentTutSameTermsUI(WidgetAbstract):
    """
    This UI is created when the student decides to sign a contract with a different tutor using the same terms as the current contract.
    """
    def __init__(self,root2,firstpartyusername,lesson,description,session,time_day,rate):
        self.root2 = root2
        self.root = Toplevel()
        self.root.title("Different Tutor")
        self.root.geometry("800x800")
        self.root.configure(bg="snow")
        self.root.resizable(False,False)
        self.first = firstpartyusername
        self.lesson = lesson
        self.description = description
        self.session = session
        self.time_day = time_day
        self.rate = rate
        self.duration = None
        self.default = None
        self.frame_generator()

    def frame_generator(self):
        self.firstPartyName = User_Details(self.first).get_fullName()

        self.__label_generator()

    def __label_generator(self):
        labels = ["NEW TUTOR", "First Party", "Second Party", "Lesson", "Description", "Time_Day", "Sessions",
                  "Rate", "Contract Duration"]
        details = [self.firstPartyName,self.lesson,self.description,self.time_day,self.session,self.rate,self.duration]

        y = 100
        for i in labels:
            if i == "NEW TUTOR":
                header = self.title(self.root)
                header.config(text="NEW TUTOR", fg="black", bg="snow")
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
            if i == 0:

                label2 = self.label_maker(self.root)
                label2.config(text=details[i])
                label2.place(x=300, y=y)
                y += 100
            else:
                label2 = self.label_maker(self.root)
                label2.config(text=details[i])
                label2.place(x=300, y=y)
                y+= 50
        self.options()

    def competent(self):
        """
        This method selects the tutors that are at least two levels higher in competency from the student.
        """
        all = Competency().get()
        all_usernames = []
        username_ids = []
        level = 0
        for i in range(len(all)):
            level = all[i]['level']
            id = all[i]['id']
            owner = all[i]['owner']
            all_usernames.append(owner['userName'])
            first_name = owner['givenName']
            second_name = owner['familyName']
            tutor = owner['isTutor']
            if tutor:
                username_ids.append((id, owner['userName'], first_name, second_name, level))
        tutors_greater = []
        if self.first not in all_usernames:
            level = 0
        else:
            for i in range(len(username_ids)):
                if self.first == username_ids[i][1]:
                    level = username_ids[i][4]
                    break
        for i in range(len(username_ids)):
            if username_ids[i][4] >= level + 2:
                tutors_greater.append(username_ids[i])
        names_of_tutors = []
        usernames = []
        for i in range(len(tutors_greater)):
            fullname = tutors_greater[i][2] + " " + tutors_greater[i][3]
            usernames.append(tutors_greater[i][1])
            names_of_tutors.append(fullname)
        return usernames

    def options(self):
        self.tutor_options = StringVar()
        tutors = self.competent()
        self.tutor_options.set("These tutors have a higher level competency")
        tutor_optionsMenu = OptionMenu(self.root,self.tutor_options,*tutors)
        tutor_optionsMenu.config(width=45, bd=0, bg="snow")
        tutor_optionsMenu.place(x=300,y=150)

        contract_change = StringVar()
        decision = ["Yes. I would like to change","No. 6 months would suffice"]
        contract_change.set("Default Contract Length is 6 Months. Change?")
        contract_change_options = OptionMenu(self.root, contract_change, *decision)
        contract_change_options.config(width=45,bd=0,bg="snow")
        contract_change_options.place(x=300,y= 460)


        choices = ["3", "6", "12", "24", "Custom"]
        duration_change = StringVar()
        duration_change.set("Select your duration:")
        duration_change_option = OptionMenu(self.root, duration_change, *choices)
        duration_change_option.config(width=45, bd=0, bg="snow", state="disabled")
        duration_change_option.place(x=300, y=485)

        sign_button = self.button_maker(self.root)
        sign_button.config(text="SIGN", state="disabled")
        sign_button.place(x=300, y=600, width=200, height=50)

        def selection(*args):
            if duration_change.get() == "Custom":
                duration = simpledialog.askinteger("Duration", "Enter Duration in Months: ")
                if duration:
                    self.duration = duration
                    self.button_destroyed = True
                    sign_button.config(state="active",
                                                  command=lambda: [self.contract_signed(),
                                                                   duration_change_option.config(state="disabled"),
                                                                   contract_change_options.config(state="disabled"),self.root.destroy(),self.root2.deiconify()])
                    duration_change_option.config(state="disabled")
                    contract_change_options.config(state="disabled")
            else:
                self.duration = int(duration_change.get())
                self.button_destroyed = True
                sign_button.config(state="active",
                                              command=lambda: [self.contract_signed(),
                                                                   duration_change_option.config(state="disabled"),
                                                                   contract_change_options.config(state="disabled"),self.root.destroy(),self.root2.deiconify()])

        def my_show(*args):
            if "Yes" in contract_change.get():
                duration_change_option.config(state="active")
                self.default = False
                sign_button.config(state="disabled")
            else:
                duration_change_option.config(state="disabled")
                self.default = True
                self.button_destroyed = True
                sign_button.config(state="active",
                                              command=lambda: [self.contract_signed(), self.message(),
                                                                   duration_change_option.config(state="disabled"),
                                                                   contract_change_options.config(state="disabled"),self.root.destroy(),self.root2.deiconify()])

        contract_change.trace('w', my_show)
        duration_change.trace('w', selection)

        def my_show2(*args):
            self.tutor_options.get()

        self.tutor_options.trace('w',my_show2)
    def message(self):
        messagebox.showinfo('Signed','Contract Signed')

    def contract_signed(self):
        if self.default:
            month = 6
        else:
            month = self.duration
            firstuserID = User_Details(self.first).get_userid()


        Contract().post(User_Details(self.first).get_userid(),User_Details(self.tutor_options.get()).get_userid(),Subject_Details(self.lesson,self.description).get_subject_id(),"Reused Contract",self.session,self.rate,self.time_day,month)
