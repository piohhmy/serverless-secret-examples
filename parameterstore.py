import boto3
import os
import logging


def parameter_store_decrypt(key):
    client = boto3.client('ssm')
    resp = client.get_parameter(
        Name=key,
        WithDecryption=True
    )
    return resp['Parameter']['Value']

def handler(event, context):
    print(parameter_store_decrypt(os.environ['SSM_PATH_TO_SECRETKEY']))
    return "OK"

