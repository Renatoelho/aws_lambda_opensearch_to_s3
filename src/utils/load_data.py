
from connections.connections import S3Client

s3 = S3Client()

def load_data(csv_data: object) -> bool:
    s3.upload_file_s3(csv_data) #MinIO
    #s3.upload_file_s3(csv_data, engine=False) #S3
