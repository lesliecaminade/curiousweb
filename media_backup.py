from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import upload_folder

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

src_folder_name = 'media'
dst_folder_name = 'media'
parent_folder_name = 'certconlinereview'

def main():
    upload_folder.main(src_folder_name, dst_folder_name, parent_folder_name)


if __name__ == '__main__':
    main()
