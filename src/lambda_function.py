import os
from os import getenv

from utils.load_data import load_data
from utils.formats_data import formats_data


def lambda_handler(event=None, context=None):
    index_list = getenv("INDEX_LIST", "").split(",")
    csv_data = formats_data(index_list)
    load_data(csv_data)
    return {
        "statusCode": 200,
        "body": "File saved to Object Store successfully."
    }

if __name__ == "__main__":
    if not "AWS_PROFILE" in os.environ:
        raise Exception("AWS_PROFILE env missing")

    lambda_handler()
