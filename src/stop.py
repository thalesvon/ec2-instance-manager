import json
import boto3
import os

region = os.environ['region']
rds_clusters = os.environ['rds'].split()
stack_name = os.environ['stack_name']

def stop(event, context):
    cf = boto3.client('cloudformation')
    cf.delete_stack(StackName=stack_name)

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