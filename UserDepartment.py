from UserInput import UserInput


class UserDepartment(UserInput):
    def __init__(self, user_input):
        super().__init__(user_input)
        self._type = 'DEPARTMENT'

    def check_inp_type(self):
        if len(self._user_input) == 1:
            if self._user_input[0].isalpha():
                self._user_input = self._user_input[0].upper()
                return True
        return False
