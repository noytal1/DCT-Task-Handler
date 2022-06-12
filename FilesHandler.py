import re

from HeaviestFile import HeaviestFile
from LatestFile import LatestFile
from NamedFile import NamedFile

""" Regex for each possible file description """
heaviest_file = "^Copy heaviest (.+) file$"
latest_file = "^Copy latest (.+) file$"
named_file = "^Copy the (.+) file named with (.+)$"


class FilesHandler:
    """ A class to handle file copying - task description execution

      Parameters:
      argument1 (list): task list - relevant data to execute task

    """
    def __init__(self, task_list):
        self._task_list = task_list

    def handle(self):
        """
        function to check the specific task description type and handle it
        """
        is_heaviest = re.search(heaviest_file, self._task_list[2])
        if is_heaviest:
            heaviest = HeaviestFile("." + is_heaviest.group(1), self._task_list)
            return heaviest.find_matching_file()

        is_latest = re.search(latest_file, self._task_list[2])
        if is_latest:
            latest = LatestFile("." + is_latest.group(1), self._task_list)
            return latest.find_matching_file()

        is_named = re.search(named_file, self._task_list[2])
        if is_named:
            named = NamedFile("." + is_named.group(1), self._task_list, is_named.group(2))
            return named.find_matching_file()

        else:
            print("No match")
