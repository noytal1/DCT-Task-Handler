from UserInput import UserInput


class UserName(UserInput):
    def __init__(self, user_input):
        super().__init__(user_input)
        self._type = 'NAME'

    def check_inp_type(self):
        if type(self._user_input) == list and len(self._user_input) > 1:
            for word in self._user_input:
                if not word.isalpha():
                    return False
            return True
        return False

    def __str__(self):
        full_name = ''
        for word in self._user_input:
            full_name += word + ' '
        return full_name
