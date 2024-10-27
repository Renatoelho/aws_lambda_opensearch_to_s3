
from os import getenv

import boto3
from botocore.client import Config
from opensearchpy import OpenSearch


class OpenSearchClient:
    def __init__(self):
        opensearch_host = getenv("OPENSEARCH_HOST", None)
        opensearch_port = int(getenv("OPENSEARCH_PORT", 9200))
        opensearch_url = (
            f"http://{getenv('OPENSEARCH_USER', None)}"
            f":{getenv('OPENSEARCH_PASSWD', None)}"
            f"@{opensearch_host}"
            f":{opensearch_port}/"
        )

        self.client = OpenSearch(
            [opensearch_url,],
            use_ssl=False,  
            verify_certs=False,
            ssl_show_warn=False
        )
    def search(self, index, query):
        return self.client.search(index=index, body=query)
    
    def index_document(self, index, doc, doc_id=None):
        return self.client.index(index=index, body=doc, id=doc_id)


class S3Client:
    def __init__(self):
        self.aws_endpoint = getenv("AWS_ENDPOINT", None)
        self.aws_bucket = getenv("AWS_BUCKET", None)
        self.aws_bucket_key = getenv("AWS_BUCKET_KEY", None)
        self.aws_access_key = getenv("AWS_ACCESS_KEY", None)
        self.aws_secret_key = getenv("AWS_SECRET_KEY", None)
        self.region_name = getenv("AWS_REGION_NAME", None)
    
        self._minio = boto3.client(
            "s3",
            endpoint_url=self.aws_endpoint,
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key,
            config=Config(signature_version="s3v4"),
            region_name=self.region_name
        )

        self._s3 = boto3.client(
            "s3",
            endpoint_url=self.aws_endpoint,
            #aws_access_key_id=self.aws_access_key,
            #aws_secret_access_key=self.aws_secret_key,
            config=Config(signature_version="s3v4"),
            region_name=self.region_name
        )

    def upload_file_s3(
            self,
            csv_data,
            object_store="MinIO"
    ):
        if object_store == "s3":
            _object_store = self._s3
        else:
            _object_store = self._minio

        _object_store.put_object(
            Bucket=self.aws_bucket,
            Key=self.aws_bucket_key,
            Body=csv_data
        )
