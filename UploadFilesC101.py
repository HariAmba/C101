import dropbox,os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,accessToken):
        self.accesToken = accessToken

    def upload_file(self,file_from,file_to):
         dbx = dropbox.Dropbox(self.accessToken)
         for root,dirs,files in os.walk(file_from):
             for fileName in files:
                 local_path = os.path.join(root,fileName)
                 relative_path = os.path.relpath(local_path,file_from)
                 dropbox_path = os.path.join(file_to,relative_path)
                 with open(local_path,'rb') as f:
                     dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))

def main():
    accessToken = ''
    transferData = TransferData(accessToken)
    file_from = str(input('Enter the folder path to transfer: '))
    file_to = input('Enter the full path tp upload to dropbox: ')
    transferData.upload_file(file_from,file_to)
    print('The file has been moved!')

main()