import os
import shutil


class FileAction:
    def __init__(self, file_type, task_list):
        self._file_type = file_type  # file extension
        self._file_to_copy_from = ''
        self._src = task_list[0]
        self._destination = "destination/" + task_list[1]
        self._description = task_list[2]

    def find_matching_file(self):
        print("in find_matching_file")
        for f in os.listdir(self._src):
            print("f in dir= " + f)
            file_name, file_extension = os.path.splitext(f)
            print("filename= " + file_name + " extension= " + file_extension)
            if file_extension == self._file_type:
                self.find_file(f)
        self.copy_file()

    def create_dest_folder(self):
        cur_folder = ''
        for folder in self._destination.split('/'):
            cur_folder += folder
            if not os.path.isdir(cur_folder):
                os.mkdir(cur_folder)
            cur_folder += '/'

    def find_file(self, f):
        pass

    def copy_file(self):
        try:
            print("bef create folder")
            self.create_dest_folder()
            print("after create folder")
            print("src= " + self._src + '/' + self._file_to_copy_from)
            print("dest= " + self._destination + '/' + self._file_to_copy_from)
            shutil.copyfile(self._src + '/' + self._file_to_copy_from,
                            self._destination + '/' + self._file_to_copy_from)
            # shutil.copyfile("source/dcm_static_and_templates/javascript.js", "destination/pm_internal/javascript.js")

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
