import json
import os
import boto3

s3_client=boto3.client("s3")

#create the buckename

def lambda_handler(event,contents):
    mybucketname = s3_client.bucket('demo-test')
    for my_bucket_object in mybucketname.objects.all(): 
        print(my_bucket_object)
        
        
