import requests

import API.Abstract_API_methods as API
from API.api_key import api_key
from API.root_url import root_url

subject_url = root_url + "/subject"

class Subject_API(API.Abstracts):
    """
    This class inherits from API.Abstracts and implements concrete classes to interact with RESTAPI using requests
    """
    def get(self):
        """
        This method gets all the subjects in the system
        """
        response = requests.get(
            url= subject_url,
            headers={'Authorization': api_key}
        )
        json_data = response.json()
        return json_data

    def post(self,name,description):
        """
        This method creates a new subject
        """
        response = requests.post(
            url=subject_url,
            headers = {'Authorization': api_key},
            data={
                'name':name,
                'description':description
            }
        )
        return response.status_code

    def get_by_id(self, id):
        """
        This method gets a subject by id
        """
        response = requests.get(
            url=subject_url + "/" + id,
            headers={'Authorization': api_key},
        )
        json_data = response.json()
        return json_data

    def get_individual_subject(self,lesson,description):
        """
        This subject gets the subject based on the name of the subject and the description of it
        """
        subjects = self.get()
        for i in subjects:
            if i["name"] == lesson and i["description"] == description:
                return i

    def get_all_subjects(self):
        """
        This method returns all the subjects in the system in a list form
        """
        subject_list = []
        subjects = self.get()
        for i in subjects:
            names = []
            names.append(i["name"])
            names.append(i["description"])
            subject_list.append(names)
        return subject_list

    def delete_subjects(self,lists):
        """
        This method deletes a subject from the system
        """
        responses = []
        for i in lists:
            response = requests.delete(
                url=subject_url + "/" + i,
                headers={'Authorization': api_key}
            )
            responses.append(response.status_code)
        return responses