from datetime import datetime
import os
import re
import shutil

heaviest_file = "^Copy heaviest (.+) file$"
latest_file = "^Copy latest (.+) file$"
named_file = "^Copy the (.+) file named with (.+)$"

class FilesHandler:
    def __init__(self, task_list):
        self._src = task_list[0]
        self._destination = "destination/" + task_list[1]
        self._description = task_list[2]

    def handle(self):
        self.extract_description_type()

    def extract_description_type(self):

        is_heaviest = re.search(heaviest_file, self._description)
        if is_heaviest:
            self.copy_heaviest(is_heaviest.group(1))
            print(is_heaviest.group(1))

        is_latest = re.search(latest_file, self._description)
        if is_latest:
            self.copy_latest(is_latest.group(1))
            print(is_latest.group(1))

        is_named = re.search(named_file, self._description)
        if is_named:
            self.copy_named(is_named.group(1), is_named.group(2))
            print(is_named.group(1) + ' ' + is_named.group(2))

        else:
            print("No match")

    def copy_heaviest(self, file_type):
        heaviest = 0
        file = ''
        for f in os.listdir(self._src):
            file_name, file_extension = os.path.splitext(f)
            if file_extension == file_type:
                size = os.path.getsize(file_name)
                if int(size) > heaviest:
                    heaviest = int(size)
                    file = f
        os.mkdir(self._destination)
        shutil.copyfile(self._src + '/' + file, self._destination)

    def copy_latest(self, file_type):
        latest = ''
        file = ''
        for f in os.listdir(self._src):
            file_name, file_extension = os.path.splitext(f)
            if file_extension == file_type:
                date_stamp = os.path.getmtime(self._src + '/' + f)
                date = datetime.fromtimestamp(date_stamp)
                if latest == '' or date.date() > latest:
                    latest = date.date()
                    file = f
                    print("yes")
        os.mkdir(self._destination)
        shutil.copyfile(self._src + '/' + file, self._destination)

    def copy_named(self, file_type, substring):
        file = ''
        for f in os.listdir(self._src):
            file_name, file_extension = os.path.splitext(f)
            if file_extension == file_type:
                if substring in file_name:
                    file = f
                    break
        os.mkdir(self._destination)
        shutil.copyfile(self._src + '/' + file, self._destination)

    def copy_file(self):
        try:
            self.create_dir()
            shutil.copyfile("source/dcm_static_and_templates/javascript.js", "destination/pm_internal/javascript.js")

        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        # If destination is a directory.
        except IsADirectoryError:
            print("Destination is a directory.")

        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")

        # For other errors
        except Exception as e:
            print("Error occurred while copying file.")

    def create_dir(self):
        if not os.path.isdir(self._destination):
            os.mkdir("destination/pm_internal")
        pass
