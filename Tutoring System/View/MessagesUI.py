import tkinter as tk

from Details.user_details import User_Details
from Model.Messages.all_messages import AllMessages
from Model.Messages.message import Messages
from Model.Messages.student_messages_view import StudentMessagesView
from Model.Messages.tutor_messages_view import TutorMessagesView


class MessagesUI:
    def __init__(self, bid, username, tutor_offer):
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.title("Messages")
        self.current_user = username
        self.current_user = User_Details(username).get_user_in_system()
        self.bid = bid
        self.tutor_offer = tutor_offer
        self.first_party = self.current_user
        self.second_party = self.second_party()
        messages_content = tk.Entry(self.root,width=45)
        messages_content.place(x=50, y=50)
        tk.Button(self.root, text="Comment",command=lambda:{Messages(self.bid, self.first_party, self.second_party).new_message(messages_content.get()), self.display_all_messages()}, width=24,height="2").place(x=400, y=40)
        self.display_all_messages()
        self.root.mainloop()

    def display_all_messages(self):
        if self.current_user['isTutor']:
            TutorMessagesView(self.first_party, self.second_party, self.root, self.bid, self.current_user, self.tutor_offer).display_all_messages()
        elif self.current_user['isStudent']:
            StudentMessagesView(self.first_party, self.second_party, self.root, self.bid, self.current_user,self.tutor_offer).display_all_messages()
        # AllMessages(self.first_party, self.second_party, self.root, self.bid, self.current_user, self.tutor_offer).display_all_messages()

    def second_party(self):
        if self.current_user['isStudent']:
            return User_Details(self.tutor_offer['offeredBy']).get_user_in_system()
        elif self.current_user['isTutor']:
            return self.bid['initiator']

