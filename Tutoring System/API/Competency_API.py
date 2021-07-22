from datetime import datetime, timedelta

import requests

import API.Abstract_API_methods as API
from API.api_key import api_key
from API.root_url import root_url

competency_url = root_url + "/competency"

class Competency(API.Abstracts):
    def get(self):
        response = requests.get(
            url=competency_url,
            headers={'Authorization': api_key}
        )
        json_data = response.json()
        return json_data




