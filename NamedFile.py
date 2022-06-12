from datetime import datetime
import os

from FileAction import FileAction


class NamedFile(FileAction):
    """ A class to handle file description of type "name with file". Inherits from FileAction

      Parameters:
      argument1 (str): file type - the extension of the file
      argument2 (list): task list - relevant data to execute task
      argument3 (ste): substring - a file name substring to use

    """

    def __init__(self, file_type, task_list, substring):
        super().__init__(file_type, task_list)
        self._substring = substring  # a file name substring to use

    def find_file(self, f):
        """
        find a specific file according to the task description
        :param f: a file to review
        :return:
        """
        if self._substring in f:
            self._file_to_copy_from = f
