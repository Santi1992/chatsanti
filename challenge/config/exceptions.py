
class ValidationException(Exception):
    def __init__(self, originalError, myCustomError="", whatProcessAndMoreInformactionAboutTheError=""):
        self.originalError = originalError
        self.myCustomError = myCustomError
        self.whatProcessAndMoreInformactionAboutTheError = whatProcessAndMoreInformactionAboutTheError
        super().__init__(originalError)


class RepositoryException(Exception):
    def __init__(self, originalError, myCustomError="", whatProcessAndMoreInformactionAboutTheError=""):
        self.originalError = originalError
        self.myCustomError = myCustomError
        self.whatProcessAndMoreInformactionAboutTheError = whatProcessAndMoreInformactionAboutTheError
        super().__init__(originalError)
