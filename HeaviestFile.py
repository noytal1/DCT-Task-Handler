import os

from FileAction import FileAction


class HeaviestFile(FileAction):
    """ A class to handle file description of type "heaviest file". Inherits from FileAction

      Parameters:
      argument1 (str): file type - the extension of the file
      argument2 (list): task list - relevant data to execute task

    """

    def __init__(self, file_type, task_list):
        super().__init__(file_type, task_list)
        self.heaviest_size = 0  # the heaviest file size found, foe comparison purposes

    def find_file(self, f):
        """
        find a specific file according to the task description
        :param f: a file to review
        :return:
        """
        size = os.path.getsize(self._src + '/' + f)  # compare the given file size to the one we already found
        if int(size) > self.heaviest_size:
            self.heaviest_size = int(size)
            self._file_to_copy_from = f
