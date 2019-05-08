import json
import boto3
import os

region = os.environ['region']
instances = os.environ['instances'].split()
start_event = os.environ['start_event']
stop_event = os.environ['stop_event']

def change(event, context):
    
    try:
        data = event['action']
    except:
        data = 'invalid json'

    if data == 'enable':
        cw_events = boto3.client('events',region_name=region)
        event_rule = cw_events.describe_rule(Name=start_event)
        if event_rule['State'] == 'ENABLED':
            pass
        else:
            cw_events.enable_rule(Name=start_event)

        body = {
            "message": "your instances will be started",
            "input": data
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        
        return response
    
    elif data == 'disable':
        cw_events = boto3.client('events',region_name=region)
        event_rule = cw_events.describe_rule(Name=stop_event)
        if event_rule['State'] == 'DISABLED':
            pass
        else:
            cw_events.disable_rule(Name=stop_event)

        body = {
            "message": "your instances will be stopped",
            "input": data
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        
        return response

    else:
        body = {
            "message": "Bad Request",
            "input": data
        }
        response = {
            "statusCode": 400,
            "body": json.dumps(body)
        }
        
        return response
