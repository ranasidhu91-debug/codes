from API import Bid_API
from API import Subject_API
from Details import user_details,subject_details
from Model.Bid import close_bid


class new_bid:
    """
    This class allows new bids to be created and posted into the system.
    """
    def __init__(self,required_lesson, lesson_description, time_day, sessions_per_week,isOthers,rate,main_root = None):
        """
        This constructor creates the instance variables that would contain the details of the bids
        """
        self.__required_lesson = required_lesson
        self.__lesson_description = lesson_description
        self.__time_day = time_day
        self.__sessions_per_week = sessions_per_week
        self.__rate = rate
        self.__isOthers = isOthers
        self.main_root = main_root

    def create_bid(self):
        """
        This method creates a json-accepted format to be posted into the system using RESTAPI.
        """
        bid_info = {
            "requiredLesson": self.__required_lesson,
            "lessonDescription": self.__lesson_description,
            "timeDay": self.__time_day,
            "sessionsPerWeek": self.__sessions_per_week,
            "lessonRate": self.__rate
        }

        return bid_info

    def others(self):
        return self.__isOthers
        # if self.__isOthers:
        #     """
        #     If the subject was not in the system previously, this if statement creates a new subject and posts it into the system
        #     """
        #     Subject_API.Subject_API().post(self.__required_lesson,self.__lesson_description)
        # student_bid = Bid_API.Bid()
        # user_id = user_details.User_Details(username).get_userid()
        # # this code posts the bid into the system using the restAPI
        # bid_item = student_bid.post(user_id,subject_details.Subject_Details(self.__required_lesson,self.__lesson_description).get_subject_id(),bid_info)
        # close_bid.CloseBid(bid_item).bid_close()