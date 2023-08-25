import os
import boto3
from io import BytesIO

class S3 ():

    def __init__(self) -> None:
        pass

    def save_into_s3(self, file_bytes, nameToS3):
        s3_client = boto3.client('s3', aws_access_key_id=os.getenv("AMZ_CLIENT"), aws_secret_access_key=os.getenv("AMZ_SECRET"), region_name='us-east-1')
        bucketName = "bucket"
        s3_client.upload_fileobj(BytesIO(file_bytes), bucketName, nameToS3)

    def get_document(self, fileName):
        s3_client = boto3.client('s3', aws_access_key_id=os.getenv("AMZ_CLIENT"), aws_secret_access_key=os.getenv("AMZ_SECRET"), region_name='us-east-1')
        bucketName = "bucket"
        response = s3_client.get_object(Bucket=bucketName, Key=fileName)
        file = response['Body']
        return file
