import json
import boto3
import os

region = os.environ['region']
rds_clusters = os.environ['rds'].split()
stack_params = os.environ['stack_params']


def start(event, context):
    stack_json = json.loads(stack_params)
    for param in stack_json['Params']:
        cf = boto3.client('cloudformation')
        cf.create_stack(StackName=param['name'],TemplateURL=param['template_url'],Capabilities=['CAPABILITY_IAM'],OnFailure='DELETE')

    rds = boto3.client('rds')
    for cluster in rds_clusters:
        rds.start_db_cluster(DBClusterIdentifier=cluster)

    body = {
        "message": "QA and DEV environment started",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response

