from datetime import datetime
import os

from FileAction import FileAction


class NamedFile(FileAction):
    def __init__(self, file_type, task_list, substring):
        super().__init__(file_type, task_list)
        self._substring = substring
        self.latest_date = ''
        # self._src_latest_date = self.find_src_latest_date()

    def find_file(self, f):
        if self._substring in f:
            self._file_to_copy_from = f
