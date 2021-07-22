from tkinter import messagebox
from API import User_api
import time


class checkCredentials:
    def correct_credentials(self, username, password):
        """
        This method checks if the username and password have been inserted and if they have been, verifies the credentials by calling User_api to determine
        if the credentials are correct. If the credentials are correct, then the Main screen of the program opens. If not, it notifies the user that
        wrong credentials have been inserted.
        """
        if username is False or password is False:
            messagebox.showerror("Error","Please insert all details")
        else:
            verified = User_api.User().post_login(username, password)
            return verified
