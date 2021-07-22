from API import Bid_API

class tutor_bid:
    """
    A class that creates the bid that the tutor has offered
    """
    def __init__(self, time_day, sessions_per_week, rate):
        """
        This constructor creates the time_day, sessions_per_week and the rate the tutor has offered.
        """
        self.__time_day = time_day
        self.__sessions_per_week = sessions_per_week
        self.__rate = rate

    def time_day_getter(self):
        """
        This method returns the time_day instance variable
        """
        return self.__time_day

    def __sessions_per_week_getter(self):
        """
        This method returns the number of sessions in a week
        """
        return self.__sessions_per_week

    def __rate_getter(self):
        """
        This method returns the rate the tutor has offered.
        """
        return self.__rate

    def make_bid_offer(self, username, single_bid_item):
        """
        Creates the offer details in a json-accepted format and patches the Bid API
        """
        tutor_bid_offer = {
            "timeDay": self.time_day_getter(),
            "sessionsPerWeek": self.__sessions_per_week_getter(),
            "lessonRate": self.__rate_getter(),
            "offeredBy": username
        }

        Bid_API.Bid().patch_tutor_offers(tutor_bid_offer, single_bid_item)





