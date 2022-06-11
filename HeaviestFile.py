import os

from FileAction import FileAction


class HeaviestFile(FileAction):
    def __init__(self, file_type, task_list):
        super().__init__(file_type, task_list)
        self.heaviest_size = 0

    def find_file(self, f):
        print("f= " + f)

        size = os.path.getsize(self._src + '/' + f)
        print("size= " + str(size))
        if int(size) > self.heaviest_size:
            print("self.heaviest_size= " + str(self.heaviest_size))
            self.heaviest_size = int(size)
            self._file_to_copy_from = f
