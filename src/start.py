import json
import boto3
import os

region = os.environ['region']
instances = os.environ['instances'].split()
rds_clusters = os.environ['rds'].split()

def start(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)

    rds = boto3.client('rds')
    for cluster in rds_clusters:
        rds.start_db_cluster(DBClusterIdentifier=cluster)

    body = {
        "message": "Started your instances "+str(instances),
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response