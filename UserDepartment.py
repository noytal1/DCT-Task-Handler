from UserInput import UserInput
import json
import re


def is_substring(str1, str2):
    x = re.search(".+{}.+".format(str1), str2)
    if x:
        return True
    else:
        print("This user's department is not allowed to execute this task. Program exits")
        return False


class UserDepartment(UserInput):
    def __init__(self, user_input, task_list):
        super().__init__(user_input)
        self._type = 'DEPARTMENT'
        self._task_list = task_list

    def check_inp_type(self):
        if len(self._user_input) == 1:
            if self._user_input[0].isalpha():
                self._user_input = self._user_input[0].upper()
                print(self._user_input)
                return self.find_dept_in_all_depts()
        return False

    def find_dept_in_all_depts(self):
        try:
            with open("source/auth/permissions.json") as file:
                data = json.load(file)
                for dept in data:
                    if dept == self._user_input:
                        department_permissions = data[dept]
                        if self.is_task_desc_in_dept(department_permissions):
                            return True
                        else:
                            print("add msg here")
                            exit()
                return False

        except Exception as e:
            print(f"{e} occurred")
            return False

    def is_task_desc_in_dept(self, department_permissions):
        task_description = self._task_list[2]
        if department_permissions == 'null':
            return False

        elif type(department_permissions) == str:
            return is_substring(department_permissions[5:], task_description)
        elif type(department_permissions) == list:

            for perm in department_permissions:
                return is_substring(perm[5:], task_description)
        return False
