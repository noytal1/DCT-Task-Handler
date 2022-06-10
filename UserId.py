from UserInput import UserInput
import requests

url = "https://dct-tasks-db.herokuapp.com/tasks"

class UserId(UserInput):
    def __init__(self, user_input):
        super().__init__(user_input)
        self._type = 'ID'
        self._json_tries = 0
        # self._valid_task = False

    def check_inp_type(self):
        if len(self._user_input) == 1:
            if self._user_input[0].isdigit():
                self._user_input = self._user_input[0]
                return self.check_task_id()
        return False

    def check_task_id(self):
        response = requests.get(url)
        while self._json_tries <= 4:
            if self.find_task_in_json(response):
                return True
            self._json_tries += 1
            new_input = str(input("Task ID doesn't exist, try again: try({}/3): ".format(self._json_tries)))
            self._user_input = int(new_input)
        return False

    def find_task_in_json(self, response):
        for task in response.json():
            if task["id"] == int(self._user_input):
                if task["status"] == "open":
                    # self._valid_task = True
                    return True
                print("Closed task. Program exits")
                exit()
        return False

    def __str__(self):
        return str(self._user_input)
