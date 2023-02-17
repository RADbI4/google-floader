from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import json
from base64 import b64decode
gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def upload_file(data):
    """

    :param file:
    :return:
    """
    content = json.loads(data)
    drive = GoogleDrive(gauth)

    with open(content.get('f_name'), 'wb') as binary_file:
        fdata = b64decode(content.get('f_data'))
        binary_file.write(fdata)
    my_file = drive.CreateFile({'title': content.get('f_name')})
    my_file.SetContentFile(content.get('f_name'))
    my_file.Upload()
    os.remove(content.get('f_name'))


if __name__ == '__main__':
    # upload_file(path='/home/radmir/Desktop/GIT_HUB/google_floader/src/files')
    pass