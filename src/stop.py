import json
import boto3
import os

region = os.environ['region']
stack_params = os.environ['stack_params']


def stop(event, context):
    stack_json = json.loads(stack_params)
    for param in stack_json['Params']:
        cf = boto3.client('cloudformation')
        cf.delete_stack(StackName=param['name'])

    body = {
        "message": "Stack Deleted",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response