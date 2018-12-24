import boto3
import os

def handler(event, context):
    print("Processing secret: {}".format(os.environ['SECRETKEY']))
    return "OK"
