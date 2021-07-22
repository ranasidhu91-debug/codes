from .all_messages import AllMessages
from Details.user_details import User_Details

class StudentMessagesView(AllMessages):
    def is_first_party(self, message):
        return self.current_user == self.bid['initiator']

    def is_second_party(self, message):
        return self.second_party == User_Details(self.tutor_offer['offeredBy']).get_user_in_system()