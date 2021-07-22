from abc import abstractmethod, ABC
from tkinter import *

class WidgetAbstract:
    username = None
    root = None
    """
    This is abstract class that houses all the widget creation and the username of a student as all the UIs would be inheriting this class
    """
    @abstractmethod
    def frame_generator(self):
        pass

    def title(self,frame):
        title = Label(frame,font=("Times",35,"bold"),bg="CadetBlue4",fg="white")
        return title

    def label_maker(self,frame):
        label = Label(frame,font=("Times",8,"bold"),bg="snow")
        return label

    def Entry_maker(self,frame):
        entry = Entry(frame,width=45)
        return entry

    def button_maker(self,frame):
        button = Button(frame,font=("Times", 10),bg="snow")
        return button

    # fix this
    def colon_maker(self,frame):
        return Label(frame, text=":", font=("Times", 20, "bold"), bg="white")






