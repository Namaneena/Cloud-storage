import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BHLDKyTQa8WfXSelLsAcZwfGe-_ZfhPicU8CNLzdHQrIMkEQdsurSPD9JdSYpyvO20lexJSi5ZhKW3S6eQAa3jCTTxQJJA7fJjyZsG4X7Rte0o3s_KxXikx52pPGc3__s9ATD3Gco6qC'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer")
    file_to = input("Enter the full path to upload to Dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been Moved")
    
main()