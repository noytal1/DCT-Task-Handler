from UserInput import UserInput
import json
import re
from Logger import logger


def is_substring(str1, str2):
    """
    static function to check whether a string is a substring of a string
    :param str1: substring
    :param str2: main string
    :return:
    """
    x = re.search(".+{}.+".format(str1), str2)
    if x:
        return True
    return False


class UserDepartment(UserInput):
    """ A class to manage validating a User department input

      Parameters:
      argument1 (list): user input

    """

    def __init__(self, user_input, task_list):
        super().__init__(user_input)
        self._type = 'DEPARTMENT'
        self._task_list = task_list  # saves relevant data to execute task

    def check_inp_type(self):
        """
        function to check the specific characteristics of an input according to its flag
        :return: if input is valid
        """
        if len(self._user_input) == 1:
            if self._user_input[0].isalpha():
                self._user_input = self._user_input[0].upper()
                return self.find_dept_in_all_depts()
        return False

    def find_dept_in_all_depts(self):
        """
        function to load json file and find whether the given department is allowed to execute the task
        :return:
        """
        try:
            with open("source/auth/permissions.json") as file:
                data = json.load(file)
                for dept in data:
                    if dept.upper() == self._user_input:
                        department_permissions = data[dept]
                        if self.is_task_desc_in_dept(department_permissions):
                            logger.info("department {} can execute the task".format(self._user_input))
                            return True
                        else:
                            print("This user's department is not allowed to execute this task. Program exits")
                            logger.info("This user's department is not allowed to execute this task. Program exits")
                            exit()
                return False

        except Exception as e:
            print(f"{e} occurred")
            logger.info(f"{e} occurred")
            return False

    def is_task_desc_in_dept(self, department_permissions):
        """
        function to find whether the task description is in the departments permissions
        :param department_permissions: a list of the departments permissions
        :return:
        """
        task_description = self._task_list[2]
        if department_permissions == 'null':
            return False

        elif type(department_permissions) == str:
            return is_substring(department_permissions[5:], task_description)

        elif type(department_permissions) == list:
            is_allowed = False
            for perm in department_permissions:
                is_allowed = is_substring(perm[5:], task_description)
            if not is_allowed:
                return False
            return True
