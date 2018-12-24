import boto3
import os
from base64 import b64decode

def kms_decrypt(secret, arn):
    client = boto3.client('kms')
    context = {"PARAMETER_ARN": arn} if arn else None
    resp = client.decrypt(CiphertextBlob=b64decode(secret), EncryptionContext=context)
    return resp['Plaintext']

def handler(event, context):
    print(kms_decrypt(os.environ['ENCRYPTED_SECRETKEY'], os.environ.get('SECRETKEY_ARN')))
    return "OK"