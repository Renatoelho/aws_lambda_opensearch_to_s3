
from os import getenv

import boto3
from botocore.client import Config
from opensearchpy import OpenSearch


class OpenSearchClient:
    def __init__(self):
        environment = getenv("LOCAL_ENVIRONMENT", "None")
        opensearch_host = getenv("OPENSEARCH_HOST", None)
        opensearch_port = int(getenv("OPENSEARCH_PORT", 9200))
        if not environment == "None":
            opensearch_parameters = {
                "use_ssl": False,
                "verify_certs": False,
                "ssl_show_warn": False
            }
            opensearch_url = (
                f"http://{getenv('OPENSEARCH_USER', None)}"
                f":{getenv('OPENSEARCH_PASSWD', None)}"
                f"@{opensearch_host}"
                f":{opensearch_port}/"
            )
        else:
            opensearch_parameters = {
                "use_ssl": True,
            }
            opensearch_url = [
                {
                    "host": getenv('OPENSEARCH_USER', None),
                    "port": int(getenv("OPENSEARCH_PORT", 443))
                }
            ]

        self.__client = OpenSearch(
            [opensearch_url,],
            **opensearch_parameters
        )
    def search(self, index, query):
        return self.__client.search(index=index, body=query)
    
    def index_document(self, index, doc, doc_id=None):
        return self.__client.index(index=index, body=doc, id=doc_id)


class S3Client:
    def __init__(self):
        self.environment = getenv("LOCAL_ENVIRONMENT", "None")
        self.__aws_endpoint = getenv("AWS_ENDPOINT", None)
        self.__aws_bucket = getenv("AWS_BUCKET", None)
        self.__aws_bucket_key = getenv("AWS_BUCKET_KEY", None)
        self.__aws_access_key = getenv("AWS_ACCESS_KEY", None)
        self.__aws_secret_key = getenv("AWS_SECRET_KEY", None)
        self.__region_name = getenv("AWS_REGION_NAME", "sa-east-1")

        if not self.environment == "None":
            self.__s3 = boto3.client(
                "s3",
                endpoint_url=self.__aws_endpoint,
                aws_access_key_id=self.__aws_access_key,
                aws_secret_access_key=self.__aws_secret_key,
                config=Config(signature_version="s3v4"),
                region_name=self.__region_name
            )
        else:
            self.__s3 = boto3.client("s3")

    def upload_file_s3(self, csv_data):
        self.__s3.put_object(
            Bucket=self.__aws_bucket,
            Key=self.__aws_bucket_key,
            Body=csv_data
        )
