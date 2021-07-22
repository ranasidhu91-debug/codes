
from tkinter import *
from WidgetMakers import WidgetAbstract


class LoginUI(WidgetAbstract):
    """"
    "This class creates the UI that a user uses to login
    """
    def __init__(self, root):
        self.__root = root
        WidgetAbstract.root = self.__root
        self.__root.title("Online Tutoring System")
        self.__root.geometry("800x400")
        self.__root.resizable(False,False)
        self.__root.configure(bg="CadetBlue4")
        self.__loginFrame = Frame(self.__root,bg="snow")
        self.__loginFrame.place(x=5,y=5,width=790,height=390)
        self.__username = None
        self.__password = None
        self.login_button = None
        self.frame_generator()

    def frame_generator(self):
        """
        Generates the frame
        """
        title_maker = self.label_maker(self.__loginFrame)
        title_maker.config(text="Welcome to Online Tutoring System",font=("Times",35,"bold"))
        title_maker.pack()

        header = self.label_maker(self.__loginFrame)
        header.config(text="Login",font=("Times",25,"bold"))
        header.pack()

        username_label = self.label_maker(self.__loginFrame)
        username_label.config(text="Username",fg="grey")
        username_label.pack()

        self.__username = self.Entry_maker(self.__loginFrame)
        # self.__username.place(x=140, y=55,width=150)
        self.__username.pack()


        password_label = self.label_maker(self.__loginFrame)
        password_label.config(text="Password",fg="grey")
        # password_label.place(x=10,y=95)
        password_label.pack()

        self.__password = self.Entry_maker(self.__loginFrame)
        # self.__password.place(x=140, y=100,width=150)
        # self.__password.config()
        self.__password.pack()


        self.login_button = self.button_maker(self.__loginFrame)
        self.login_button.config(text="Login")
        # self.login_button.place(x=130, y=170)
        self.login_button.pack()


    def username_getter(self):
        """
        returns the username
        """
        return self.__username.get()

    def password_getter(self):
        """
        returns the password
        """
        return self.__password.get()

    # def root_getter(self):
    #     return self.__root

    def hide_frame(self):
        """
        hides the frame
        """
        return self.__loginFrame.place_forget()
