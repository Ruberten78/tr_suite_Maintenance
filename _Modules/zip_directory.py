# importing required modules
from zipfile import ZipFile
import os
import datetime


class ZIPFILE:

    def __init__(self):

        x = datetime.datetime.now()
        self.today = str(x.strftime('%d-%m-%Y'))

    def get_all_file_paths(self, directory):
        # initializing empty file paths list
        file_paths = []

        # crawling through directory and subdirectories
        for root, directories, files in os.walk(directory):
            for filename in files:
                # join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

                # returning all file paths
        return file_paths

    def main_directory(self, directory, name_zip_export):

        # name_zip_export = 'Report_Tariffe_Profili.zip'

        # calling function to get all file paths in the directory
        file_paths = self.get_all_file_paths(directory)

        # printing the list of all files to be zipped
        print('\nFollowing files will be zipped:')
        for file_name in file_paths:
            print(file_name)

            # writing files to a zipfile
        with ZipFile(name_zip_export, 'w') as zip:
            # writing each file one by one
            for file in file_paths:
                zip.write(file)

        print('All files zipped successfully!')

