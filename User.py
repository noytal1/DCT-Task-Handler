from UserDepartment import UserDepartment
from UserId import UserId
from UserName import UserName
from FilesHandler import FilesHandler
from Logger import logger


class User:
    """ A class to hold three elements, so when combined together, they
        represent a task execution

        Parameters:
        argument1 (list): name of user to execute task
        argument1 (list): id of the task
        argument1 (list): the user's department

   """

    def __init__(self, name, task_id, dept):
        self._name = name
        self._task_id = task_id
        self._dept = dept

    def create_user(self):
        """
        the main function that runs the process of creating a user
        with all given elements

        """
        user_name = UserName(self._name)  # creating a user name
        logger.info("Receiving NAME from user")

        if user_name.validate():
            user_id = UserId(self._task_id)  # creating a user task id
            logger.info("Receiving TASK ID from user")

            is_id_valid, task_list = user_id.validate()
            if is_id_valid:

                user_dept = UserDepartment(self._dept, task_list)  # creating a user department
                logger.info("Receiving DEPT from user")

                if user_dept.validate():
                    file_handler = FilesHandler(task_list)  # if al args are valid, execute task
                    file_handler.handle()
            else:
                logger.info("invalid arguments, program exits")
                exit()
