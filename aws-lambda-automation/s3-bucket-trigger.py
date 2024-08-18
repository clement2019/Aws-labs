import json
import os
import boto3

s3_client=boto3.client("s3")

#create the buckename

def lambda_handler(event,contents):
    bucketname = event['Records'][0]['s3']['bucket']['name']
    s3_filename = event['Records'][0]['s3']['object']['key']
    response=s3_client.get_object(Bucket= bucketname ,key= s3_filename)
    print(response)
    data=response['Body'].read()
    print(data)
    #split the data into new lines
