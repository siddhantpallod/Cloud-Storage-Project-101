import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(fileFrom):
            for fileName in files:
                localPath = os.path.join(root, fileName)

                relativePath = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)

                with open(localPath, 'rb') as f:
                    dbx.filesUpload(f.read(), dropboxPath, mode = WriteMode('overwrite'))

def main():
    access_token = 'RZSCy2zyE_YAAAAAAAAAAf6OvC8czkqOFLqZ4N7miDA7lEFC7RGK4DLCShnX5sFo'
    transferData = TransferData(access_token)


    fileFrom = str(input("Enter The Folder Path To Transfer: "))
    fileTo = str(input("Enter The Path To Upload To Dropbox: "))

    transferData.uploadFile(fileFrom,fileTo)
    print("File Has Been Moved!!")

main()