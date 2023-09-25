import boto3

from configparser import ConfigParser

config = ConfigParser()

config.read('.env')

region = config['AWS']['region']

access_key_ID = config['AWS']['access_key_ID']		

Secret_key = config['AWS']['Secret_key']

bucket_name = config['AWS']['bucket_name']


access_key_ID = access_key_ID		
Secret_key = Secret_key

region = region

bucket_name = bucket_name

def create_bucket():
    
    client = boto3.client(
        's3',
        aws_access_key_id = access_key_ID,
        aws_secret_access_key = Secret_key

    )

    client.create_bucket(
        Bucket = bucket_name,
        CreateBucketConfiguration = {
            'LocationConstraint': region
        }
    )