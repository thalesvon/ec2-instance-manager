import json
import boto3
import os

region = os.environ['region']
stack_params = os.environ['stack_params']


def start(event, context):
    stack_json = json.loads(stack_params)
    for param in stack_json['Params']:
        cf = boto3.client('cloudformation')
        cf.create_stack(StackName=param['name'],TemplateURL=param['template_url'],Capabilities=['CAPABILITY_IAM'],OnFailure='DELETE')

    
    body = {
        "message": "Stack created",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response

