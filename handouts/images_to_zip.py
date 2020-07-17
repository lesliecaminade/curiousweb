# importing required modules
from zipfile import ZipFile
import random
import string
import os
import curiousweb

def get_all_file_paths(directory):

    # initializing empty file paths list
    # file_paths = []

    # # crawling through directory and subdirectories
    # for root, directories, files in os.walk(directory):
    #     for filename in files:
    #         # join the two strings in order to form the full filepath.
    #         filepath = os.path.join(root, filename)
    #         file_paths.append(filepath)

    file_paths = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # returning all file paths
    return file_paths

def main(input_path):
    # path to folder which needs to be zipped
    directory = input_path

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    # writing files to a zipfile
    save_path = os.path.join(curiousweb.settings.MEDIA_ROOT, 'temp_zip')
    random_zip_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '.zip'
    with ZipFile(os.path.join(save_path, random_zip_name),'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')
    return os.path.join(save_path, random_zip_name)
