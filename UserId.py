from UserInput import UserInput


class UserId(UserInput):
    def __init__(self, user_input):
        super().__init__(user_input)
        self._type = 'ID'

    def check_inp_type(self):
        if len(self._user_input) == 1:
            if self._user_input[0].isdigit():
                self._user_input = self._user_input[0]
                return True
        return False
