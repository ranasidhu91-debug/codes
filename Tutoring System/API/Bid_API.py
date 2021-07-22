from datetime import datetime, timedelta

import requests

import API.Abstract_API_methods as API
from API.api_key import api_key
from API.root_url import root_url

bid_url = root_url + "/bid"


class Bid(API.Abstracts):
    """
    This class inherits from API.Abstracts and creates concrete methods that contains the Bid related API requests.
    """

    def get(self):
        """
        This method gets all the bids in the system and returns them
        """
        response = requests.get(
            url=bid_url,
            headers={'Authorization': api_key}
        )
        json_data = response.json()
        return json_data

    def post(self, initiator_id, subject_id, bid_info):
        """
        This method posts a new bid into the system
        """
        response = requests.post(
            url=bid_url,
            headers={'Authorization': api_key},
            json={
                "type": "open",
                "initiatorId": initiator_id,
                "dateCreated": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
                "subjectId": subject_id,
                "additionalInfo": {
                    "bidInfo": bid_info,
                    "tutorBidOffers": [],
                    "bidAvailability": True,
                    "bidSubscribers": []
                }
            }
        )
        return response.json()

    def get_by_id(self, args1):
        """
        This method allows a bid to be obtained using an ID
        """
        response = requests.get(
            url=bid_url + "/" + args1,
            headers={'Authorization': api_key},
        )
        json_data = response.json()
        return json_data

    def patch_tutor_offers(self, tutor_bid_offer, single_bid_item):
        """"
        This method patches the BID by adding in the offers made by the tutors
        """
        bid_info = single_bid_item['additionalInfo']['bidInfo']
        bid_subscribers = single_bid_item['additionalInfo']['bidSubscribers']
        all_bid_offers = single_bid_item['additionalInfo']['tutorBidOffers']
        all_bid_offers.append(tutor_bid_offer)

        response = requests.patch(
            url=bid_url + "/" + single_bid_item['id'],
            headers={'Authorization': api_key},
            json={
                "additionalInfo": {
                    "bidInfo": bid_info,
                    "tutorBidOffers": all_bid_offers,
                    "bidAvailability": True,
                    "bidSubscribers": bid_subscribers
                }
            }
        )
        response.json()

    def delete_bid(self, id):
        """
        This method deletes a bid
        """
        response = requests.delete(
            url=bid_url + "/" + id,
            headers={'Authorization': api_key},
        )
        return response.status_code

    def bid_closedown(self, bid_id):
        """
        This method closes a bid
        """
        response = requests.post(
            url=bid_url + "/" + bid_id + "/close-down",
            headers={'Authorization': api_key},
            json={
                # changed the bid closing time to 2 minutes instead of 30 minutes for testing purposes
                "dateClosedDown": (datetime.now() + timedelta(minutes=100)).strftime('%Y-%m-%dT%H:%M:%S.%f')
            }
        )

    def patch_bid_availability(self, single_bid_item):
        """
        This method changes the availability of the bid
        """
        bid_info = single_bid_item['additionalInfo']['bidInfo']
        bid_subscribers = single_bid_item['additionalInfo']['bidSubscribers']
        all_bid_offers = single_bid_item['additionalInfo']['tutorBidOffers']

        response = requests.patch(
            url=bid_url + "/" + single_bid_item['id'],
            headers={'Authorization': api_key},
            json={
                "additionalInfo": {
                    "bidInfo": bid_info,
                    "tutorBidOffers": all_bid_offers,
                    "bidAvailability": False,
                    "bidSubscribers": bid_subscribers
                }
            }
        )
        response.json()

    def patch_bid_subscriber(self, single_bid_item, subscriber_username):
        """
        controls the subscription of the bid by the tutor
        :param single_bid_item: The bid that is currently being modified
        :return:response data
        """
        bid_info = single_bid_item['additionalInfo']['bidInfo']
        bid_availability = single_bid_item['additionalInfo']['bidAvailability']
        bid_subscribers = single_bid_item['additionalInfo']['bidSubscribers']
        bid_subscribers.append(subscriber_username)
        all_bid_offers = single_bid_item['additionalInfo']['tutorBidOffers']

        response = requests.patch(
            url=bid_url + "/" + single_bid_item['id'],
            headers={'Authorization': api_key},
            json={
                "additionalInfo": {
                    "bidInfo": bid_info,
                    "tutorBidOffers": all_bid_offers,
                    "bidAvailability": bid_availability,
                    "bidSubscribers": bid_subscribers
                }
            }
        )
        response.json()

    def get_bid_messages(self, bid):
        """
        This method returns the messages from a bid
        """
        bid_id = bid['id']
        response = requests.get(
            url=bid_url + "/" + bid_id,
            headers={'Authorization': api_key},
            params={'fields': 'messages'}
        )
        return response.json()
