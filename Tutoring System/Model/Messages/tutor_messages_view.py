from .all_messages import AllMessages

class TutorMessagesView(AllMessages):
    def is_first_party(self, message):
        return self.current_user == message['additionalInfo']['firstParty']

    def is_second_party(self, message):
        return self.second_party == self.bid['initiator']