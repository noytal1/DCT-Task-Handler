from Logger import logger


class UserInput:
    """ A class to manage validating a User input

              Parameters:
              argument1 (list): user input

         """

    def __init__(self, user_input):
        self._user_input = '' if user_input is None else user_input
        self._is_valid = False  # is the given input valid
        self._input_tries = 0  # number of input tries
        self._type = ''  # the flag name of the input

    def validate(self):
        """
        function to validate the user input
        :return: if the input is indeed valid
        """
        while not self._is_valid and self._input_tries <= 4:
            if not self.check_inp_type():
                self._input_tries += 1  # updating number of tries
                new_input = str(
                    input("Incorrect {} input, try again: try({}/3): ".format(self._type, self._input_tries))).split()
                logger.info("received an invalid input: {}, try({}/3)".format(self._user_input, self._input_tries))
                self._user_input = new_input  # trying a new given input
                logger.info("new {} from user: {}".format(self._type, new_input))

            else:
                self._is_valid = True
        logger.info("valid {}: {}".format(self._type, self._user_input))
        return self._is_valid

    def check_inp_type(self):
        """
        function to check the specific characteristics of an input according to its flag
        :return: if input is valid
        """
        pass

    def get_is_valid(self):
        return self._is_valid

    def __str__(self):
        return self._user_input
