import boto3

access_key_ID = 'AKIAVFIGTUJDIWWJPGMA'		
Secret_key = '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'

region = 'eu-west-1'

bucket_name = 'payminutelekan'

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