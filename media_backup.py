from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import random
import string

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

def replace_or_upload(source_filename, dest_filename):
    file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
    print(file_list)

    exists = False
    for file in file_list:
        if file['title'] == dest_filename:
            file.Delete()

    f = drive.CreateFile()
    f['title'] = dest_filename
    f.SetContentFile(source_filename)
    f.Upload()

    print(f"""{dest_filename} upload success.""")

def upload(source_filename, dest_filename):
    file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
    print(file_list)

    exists = False
    for file in file_list:
        if file['title'] == dest_filename:
            file['title'] = file['title'] + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

    f = drive.CreateFile()
    f['title'] = dest_filename
    f.SetContentFile(source_filename)
    f.Upload()

    print(f"""{dest_filename} upload success.""")

def main():
    replace_or_upload('media.zip', 'certconlinereview-media.zip')
    upload('data.json', 'certconlinereview-data.json')

if __name__ == '__main__':
    main()
