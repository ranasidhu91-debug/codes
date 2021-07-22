from Model.Bid import new_bid
from API import Subject_API,Bid_API
from Details import user_details,subject_details


class studentBidCreation:
    def __init__(self,username,required_lesson, lesson_description, time_day, sessions_per_week,isOthers,rate):
        self.bid = new_bid.new_bid(required_lesson, lesson_description, time_day, sessions_per_week,isOthers,rate)
        self.subject_new = Subject_API.Subject_API()
        self.submitting_bid = Bid_API.Bid()
        self.user = user_details.User_Details(username)
        if self.bid.others():
            self.subject_new.post(required_lesson,lesson_description)
        self.subject_details = subject_details.Subject_Details(required_lesson,lesson_description)

    def createBid(self):
        bid_info = self.bid.create_bid()
        subject_id = self.subject_details.get_subject_id()
        user_id = self.user.get_userid()
        bid_item = self.submitting_bid.post(user_id,subject_id,bid_info)
        self.submitting_bid.bid_closedown(bid_item["id"])
