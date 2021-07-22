from API import Subject_API

class Subject_Details:
    def __init__(self,lesson,description):
        self.__lesson_description = Subject_API.Subject_API().get_individual_subject(lesson,description)

    def get_subject_id(self):
        return self.__lesson_description["id"]

    def get_subject_name(self):
        return self.__lesson_description["name"]

    def get_subject_description(self):
        return self.__lesson_description["description"]
