from API.Competency_API import Competency

class CompetencyDetails:
    def __init__(self,id):
        self.__details = Contract_API.Contract().get_by_id(id)