from datetime import datetime
import os
from FileAction import FileAction
from Logger import logger


class LatestFile(FileAction):
    """ A class to handle file description of type "latest file". Inherits from FileAction

      Parameters:
      argument1 (str): file type - the extension of the file
      argument2 (list): task list - relevant data to execute task

    """

    def __init__(self, file_type, task_list):
        super().__init__(file_type, task_list)
        self.latest_date = ''  # the latest date found, foe comparison purposes

    def find_file(self, f):
        """
        find a specific file according to the task description
        :param f: a file to review
        :return:
        """
        date_stamp = os.path.getmtime(self._src + '/' + f)
        date = datetime.fromtimestamp(date_stamp)

        # compare the given date to the one we already found
        if self.latest_date == '' or date.date() > self.latest_date:
            self.latest_date = date.date()
            self._file_to_copy_from = f
            logger.info("updated latest file to: {}".format(f))

