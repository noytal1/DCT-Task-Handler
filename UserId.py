from UserInput import UserInput
import requests

url = "https://dct-tasks-db.herokuapp.com/tasks"
incorrect_inp_msg = "Incorrect input, try again: try({}/3): "
incorrect_id_msg = "Task ID doesn't exist, try again: try({}/3): "

class UserId(UserInput):
    def __init__(self, user_input):
        super().__init__(user_input)
        self._type = 'ID'
        self._task_details = []

    def validate(self):
        is_first_success = self.first_step()
        if is_first_success:
            self._input_tries = 0
            if self.second_step():
                return True, self._task_details
            return False, self._task_details
        else:
            print("All tries failed. Program exits")
            exit()

    def first_step(self):
        while self._input_tries < 3:
            is_id_valid = self.check_inp_type()
            if is_id_valid:
                return True
            else:
                self.take_new_input(incorrect_inp_msg)
        return False

    def second_step(self):
        response = requests.get(url)
        while self._input_tries <= 3:
            if self.check_inp_type() and self.find_task_in_json(response):
                return True
            else:
                self.take_new_input(incorrect_id_msg)
        return False

    def find_task_in_json(self, response):
        for task in response.json():
            if task["id"] == int(self._user_input[0]):
                if task["status"] == "open":
                    self._task_details = [task["source"], task["destination"], task["description"]]
                    print(self._task_details)
                    return True
                print("Closed task. Program exits")
                exit()
        return False

    def check_inp_type(self):

        if len(self._user_input) == 1 and str(self._user_input[0]).isdigit():
            return True
        return False

    def take_new_input(self, msg):
        if self._input_tries == 3:
            print("Maxed number of tries. Program exits")
            exit()
        self._input_tries += 1
        self._user_input[0] = str(input(msg.format(self._input_tries)))

    def __str__(self):
        return str(self._user_input)
