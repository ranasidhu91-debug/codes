from tkinter import messagebox

from Model.Credential_Checker import checkCredentials
from LoginUserInterface import LoginUI
from tkinter import *
from Details.user_details import User_Details
from View.Dashboard import Dashboard
from WidgetMakers import WidgetAbstract
from Controller.tutor_view_controller import TutorViewController
from Controller.student_view_controller import StudentViewController


class LoginController:
    def __init__(self, login: checkCredentials, welcome_ui: LoginUI):
        """
        controls the login of the user
        :param login: an instance of the login model that checks the user with the server
        :param welcome_ui: an instance of the login view which determines which generates the UI for the login
        """
        self.welcome_ui = welcome_ui
        self.login = login
        self.welcome_ui.login_button.config(command=lambda: [self.user_login()])
        self.__active_contract = None

    def user_login(self):
        """
        calls the login model to check the credentials of the user in the system
        """
        username = self.welcome_ui.username_getter()
        password = self.welcome_ui.password_getter()
        verified = self.login.correct_credentials(username, password)
        self.__active_contract = self.get_active_contracts()
        if verified == 200:
            WidgetAbstract.username = username
            WidgetAbstract.root = root
            self.open_dashboard(username)
        else:
            messagebox.showerror(title="Error", message="The credentials you entered are incorrect")

    def contract_nos(self):
        # ACTIVE CONTRACTS. NOT ALL CONTRACTS
        if len(self.__active_contract) > 5:
            messagebox.showinfo("Contracts","Maximum number of contracts allowed is 5")

    def get_active_contracts(self):
        return User_Details(WidgetAbstract.username).active()



    def open_dashboard(self, username):
        """
        This method creates the main screen of the program after the user details have been verified.
        """
        name = User_Details(self.welcome_ui.username_getter()).get_givenName() + " " + User_Details(self.welcome_ui.username_getter()).get_familyName()
        # Dashboard(WidgetAbstract.root, name, len(self.get_active_contracts()))
        current_user = User_Details(username)
        if current_user.isTutor():
            TutorViewController(Dashboard(name, len(self.get_active_contracts())))
        elif current_user.isStudent():
            StudentViewController(Dashboard(name, len(self.get_active_contracts())))
        self.welcome_ui.hide_frame()
        WidgetAbstract.root.withdraw()


if __name__ == '__main__':
    root = Tk()
    LoginController(checkCredentials(), LoginUI(root))
    root.mainloop()