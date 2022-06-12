import os
import shutil


class FileAction:
    """ A class to handle file description

      Parameters:
      argument1 (str): file type - the extension of the file
      argument2 (list): task list - relevant data to execute task

    """

    def __init__(self, file_type, task_list):
        self._file_type = file_type
        self._file_to_copy_from = ''
        self._src = task_list[0]  # src folder
        self._destination = "destination/" + task_list[1]  # destination folder
        self._description = task_list[2]  # task description

    def find_matching_file(self):
        """
        function to look for all files with the given extension
        :return:
        """
        for f in os.listdir(self._src):
            file_name, file_extension = os.path.splitext(f)
            if file_extension == self._file_type:
                self.find_file(f)
        self.copy_file()  # copies the file matching the description

    def create_dest_folder(self):
        """
        verifying and creating a destination folder with the specific route
        :return:
        """
        cur_folder = ''
        for folder in self._destination.split('/'):
            cur_folder += folder
            if not os.path.isdir(cur_folder):  # create that path if it doesn't exist
                os.mkdir(cur_folder)
            cur_folder += '/'

    def find_file(self, f):
        """
        find a specific file according to the task description
        :param f: a file to review
        :return:
        """
        pass

    def copy_file(self):
        """
        once the wanted file was found, we create a destination folder for it and copy the source file to there
        :return:
        """
        try:
            self.create_dest_folder()
            shutil.copyfile(self._src + '/' + self._file_to_copy_from,
                            self._destination + '/' + self._file_to_copy_from)
            # shutil.copyfile("source/dcm_static_and_templates/javascript.js", "destination/pm_internal/javascript.js")

        except shutil.SameFileError:
            print("Source and destination represents the same file")

        # If destination is a directory.
        except IsADirectoryError:
            print("Destination is a directory.")

        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")

        # For other errors
        except Exception as e:
            print("Error occurred while copying file.")
