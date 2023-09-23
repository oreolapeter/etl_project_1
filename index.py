import psycopg2

import pandas as pd

from sqlalchemy import create_engine

import boto3

from utils.helper import create_bucket

from configparser import ConfigParser

from utils.constants import db_tables



config = ConfigParser()

config.read('.env')

region = config['AWS']['region']

access_key_ID = config['AWS']['access_key_ID']		

Secret_key = config['AWS']['Secret_key']

bucket_name = config['AWS']['bucket_name']


host = config['DB_CRED']['host']
username = config['DB_CRED']['username']
password = config['DB_CRED']['password']
database = config['DB_CRED']['database']

# step 1: create a bucket using boto3

create_bucket()

# step 2: extract from Database to datalake

conn = create_engine('postgresql+psycopg2://{username}:{password}@{host}:5432/{database}')



s3_path ='s3://{}/{}.csv'



for table in db_tables:
    query = f'SELECT * FROM {table}'
    df = pd.read_sql_query(query, conn)


    df.to_csv(
        s3_path.format(bucket_name,table)
        , index=False
        ,storage_options={
            'key': access_key_ID
            , 'secret': Secret_key
        }
    )




