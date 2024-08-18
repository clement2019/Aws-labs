import json
import boto3

def lamda_handler(event,context):
    client=boto3.client('ses')
    subject="test subject from lamda"
    body="test body from lamda"
    message=("Subject": ("Data": subject), "Body": ("Html": ,("Data": body)))
    response=client.send_email(source="",Destination=)
            
            
 Mesage =meassge
    
