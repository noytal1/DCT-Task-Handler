from datetime import datetime
import os

from FileAction import FileAction


class LatestFile(FileAction):
    def __init__(self, file_type, task_list):
        super().__init__(file_type, task_list)
        self.latest_date = ''
        # self._src_latest_date = self.find_src_latest_date()

    def find_file(self, f):
        date_stamp = os.path.getmtime(self._src + '/' + f)
        date = datetime.fromtimestamp(date_stamp)
        print("f + date = " + f + ' ' + str(date))

        if self.latest_date == '' or date.date() > self.latest_date:
            self.latest_date = date.date()
            self._file_to_copy_from = f
