
from connections.connections import S3Client

s3 = S3Client()

def load_data(csv_data: object) -> bool:
    try:
        s3.upload_file_s3(csv_data)
        return True
    except Exception as error:
        print(error)
        return False
