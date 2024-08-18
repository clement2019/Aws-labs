import json
import boto3

def iamaction():
    print('connecting to Iam')
    iam=boto3.resource('iam')
    group=iam.Group('Devgroup').users.all()
    #create list of users
    print('list of users')
    names=[i.name for i in group]
    return names



def start_program(event, context):
    print('iam started')
    iamaction()
    
