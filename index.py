import logging
import boto3
import json
from botocore.exceptions import ClientError

def upload_file(file_name, bucket, object_name=None):


    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def download_file(file_name, bucket, object_name=None):
    s3 = boto3.client('s3')
    with open(file_name, 'w') as f:
        s3.download_fileobj(bucket, object_name, f)


def handler(event, context):
    bucket = "awsbuckets3alexendava"
    file_name = "random.txt"

    if event["func"] == "put" :
        upload_file(file_name, bucket)
    else :
        download_file(file_name, bucket)
