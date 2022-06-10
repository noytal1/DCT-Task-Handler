class UserInput:
    def __init__(self, user_input):
        self._user_input = '' if user_input is None else user_input
        self._is_valid = False
        self._num_of_tries = 0
        self._type = ''

    def validate(self):
        while not self._is_valid and self._num_of_tries <= 4:
            if not self.check_inp_type():
                self._num_of_tries += 1
                new_input = str(
                    input("Incorrect {} input, try again: try({}/3): ".format(self._type, self._num_of_tries))).split()
                self._user_input = new_input
            else:
                self._is_valid = True
        return self._is_valid

    def check_inp_type(self):  # if None
        pass

    def get_is_valid(self):
        return self._is_valid

    def __str__(self):
        return self._user_input
