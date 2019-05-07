import json
import boto3
import os

region = os.environ['region']
instances = os.environ['instances'].split()

def stop(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    #ec2.stop_instances(InstanceIds=instances)
    body = {
        "message": "Stopped your instances "+str(instances),
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response