from UserInput import UserInput
import requests
from Logger import logger

url = "https://dct-tasks-db.herokuapp.com/tasks"
incorrect_inp_msg = "Missing ID, try again: try({}/3): "
incorrect_id_msg = "Task ID doesn't exist, try again: try({}/3): "


class UserId(UserInput):
    """ A class to manage validating a User task id input

      Parameters:
      argument1 (list): user input

    """

    def __init__(self, user_input):
        super().__init__(user_input)
        self._type = 'ID'
        self._task_details = []  # saves relevant data to execute task

    def validate(self):
        """
        function to validate the user input
        :return: if the input is indeed valid
        """
        is_first_success = self.first_step()

        if is_first_success:
            self._input_tries = 0
            if self.second_step():
                logger.info("valid {}: {}".format(self._type, self._user_input[0]))
                return True, self._task_details
            return False, self._task_details
        else:
            print("All tries failed. Program exits")
            logger.info("All tries failed. Program exits")
            exit()

    def first_step(self):
        """
        function to do the type of input validation
        :return:
        """

        while self._input_tries < 3:

            is_id_valid = self.check_inp_type()

            if is_id_valid:
                return True
            else:

                self.take_new_input(incorrect_inp_msg)
        return False

    def second_step(self):
        """
        function to hold all the input validations
        :return:
        """
        response = requests.get(url)
        while self._input_tries <= 3:
            if self.check_inp_type() and self.find_task_in_json(response):
                return True
            else:
                self.take_new_input(incorrect_id_msg)

        return False

    def find_task_in_json(self, response):
        """
        function to do the fetching and verifying whether the task id exits in REST API
        :return:
        """
        for task in response.json():
            if task["id"] == int(self._user_input[0]):
                if task["status"] == "open":
                    self._task_details = [task["source"], task["destination"], task["description"]]
                    return True
                print("Closed task. Program exits")
                logger.info("Closed task. Program exits")
                exit()
        logger.info("task id doesn't exist in tasks API")

        return False

    def check_inp_type(self):
        """
        function to check the specific characteristics of an input according to its flag
        :return: if input is valid
        """
        if len(self._user_input) == 1 and str(self._user_input[0]).isdigit():
            return True
        return False

    def take_new_input(self, msg):
        """
        function to take a new input from user in case of an invalid one
        :return: if input is valid
        """

        if self._input_tries == 3:
            print("Maxed number of tries. Program exits")
            logger.info("Maxed number of tries. Program exits")
            exit()
        self._input_tries += 1
        if self._user_input is None:

            self._user_input = ['x']

        logger.info("received an invalid input")
        self._user_input = [str(input(msg.format(self._input_tries)))]
        logger.info("new {} from user".format(self._type))

    def __str__(self):
        return str(self._user_input)
