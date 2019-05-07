import json
import boto3

region = os.environ['region']
instances = os.environ['instances'].split()

def start(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    #ec2.start_instances(InstanceIds=instances)
    body = {
        "message": "Started your instances "+str(instances),
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response