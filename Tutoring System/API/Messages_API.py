from datetime import datetime

import requests

import API.Abstract_API_methods as API
from API.api_key import api_key
from API.root_url import root_url

messages_url = root_url + "/message"

class MessageAPI(API.Abstracts):
    """
    This class creates messages to be stored in particular bids between a student and tutor using the RESTAPI requests.
    """
    def post(self, bid_id, poster_id, message_content, first_party, second_party):
        response = requests.post(
            url=messages_url,
            headers = {'Authorization': api_key},
            json={
              "bidId": bid_id,
              "posterId": poster_id,
              "datePosted": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
              "content": message_content,
              "additionalInfo": {
                  "firstParty": first_party,
                  "secondParty": second_party
              }
            }
        )
        response.json()

