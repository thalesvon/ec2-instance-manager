import json
import boto3
import os

region = os.environ['region']
rds_clusters = os.environ['rds'].split()
stack_params = os.environ['stack_params']


def stop(event, context):
    stack_json = json.loads(stack_params)
    for param in stack_json['Params']:
        cf = boto3.client('cloudformation')
        cf.delete_stack(StackName=param['name'])

    rds = boto3.client('rds')
    for cluster in rds_clusters:
        rds.stop_db_cluster(DBClusterIdentifier=cluster)

    body = {
        "message": "QA and DEV environment stopped",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response