from API.Messages_API import MessageAPI


class Messages:
    def __init__(self, bid, first_party, second_party):
        self.bid = bid
        self.first_party = first_party
        self.second_party = second_party

    def new_message(self, message_content):
        bid_id = self.bid['id']
        poster_id = self.first_party['id']
        MessageAPI().post(bid_id, poster_id, message_content, self.first_party, self.second_party)
