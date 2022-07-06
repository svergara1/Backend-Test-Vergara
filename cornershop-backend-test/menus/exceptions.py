from django.utils.translation import ugettext


class MenuDoesNotExistException(Exception):
    def __init__(self, error_code, status_code=400, error_message=None):
        self.error_code = error_code
        self.status_code = status_code
        self.error_message = error_message or ugettext(error_code)
        super(MenuDoesNotExistException, self).__init__(error_code, error_message)

    @property
    def body(self):
        return {"error": self.error_code, "user_error_msg": self.error_message}


class MenuOptionDoesNotExistException(Exception):
    def __init__(self, error_code, status_code=400, error_message=None):
        self.error_code = error_code
        self.status_code = status_code
        self.error_message = error_message or ugettext(error_code)
        super(MenuOptionDoesNotExistException, self).__init__(error_code, error_message)

    @property
    def body(self):
        return {"error": self.error_code, "user_error_msg": self.error_message}
