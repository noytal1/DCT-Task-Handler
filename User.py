from UserDepartment import UserDepartment
from UserId import UserId
from UserName import UserName
from FilesHandler import FilesHandler


class User:
    def __init__(self, name, task_id, dept):
        self._name = name
        self._task_id = task_id
        self._dept = dept

    def create_user(self):
        user_name = UserName(self._name)
        if user_name.validate():
            user_id = UserId(self._task_id)
            is_id_valid, task_list = user_id.validate()
            if is_id_valid:
                user_dept = UserDepartment(self._dept, task_list)
                if user_dept.validate():
                    file_handler = FilesHandler(task_list)
                    file_handler.handle()
            else:
                exit()

