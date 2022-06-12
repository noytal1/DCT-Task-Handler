from UserInput import UserInput


class UserName(UserInput):
    """ A class to manage validating the User name, inherits from UserInput class

           Parameters:
          argument1 (list): user input

      """

    def __init__(self, user_input):
        super().__init__(user_input)
        self._type = 'NAME'

    def check_inp_type(self):
        """
           function to check the specific characteristics of an input according to its flag
           :return: if input is valid
        """
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
