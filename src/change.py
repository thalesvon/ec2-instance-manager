import json
import boto3
import os
import urllib.request
import json

region = os.environ['region']
instances = os.environ['instances'].split()
start_event = os.environ['start_event']
stop_event = os.environ['stop_event']
slack_token = os.environ['slack_token']
channel = os.environ['channel']

def change(event, context):
        
    try:
        data = json.loads(event['body'])
        data = data['action']
    except:
        data = 'invalid json'

    if data == 'enable':
        cw_events = boto3.client('events',region_name=region)
        start_event_rule = cw_events.describe_rule(Name=start_event)
        stop_event_rule = cw_events.describe_rule(Name=stop_event)
        if start_event_rule['State'] == 'ENABLED' and stop_event_rule['State'] == 'ENABLED':
            msg = "Scheduled Jobs are already enabled, no changes were made"
        else:
            cw_events.enable_rule(Name=start_event)
            cw_events.enable_rule(Name=stop_event)
            msg = "Scheduled Jobs have been enabled"
            req = urllib.request.Request('https://slack.com/api/chat.postMessage?token='+slack_token+'&channel='+channel+'&text=Scheduled%20Jobs%20have%20been%20enabled&as_user=true&pretty=1')
            resp = urllib.request.urlopen(req)

        body = {
            "message": msg,
            "input": data
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        
        return response
    
    elif data == 'disable':
        cw_events = boto3.client('events',region_name=region)
        start_event_rule = cw_events.describe_rule(Name=start_event)
        stop_event_rule = cw_events.describe_rule(Name=stop_event)
        if start_event_rule['State'] == 'DISABLED' and stop_event_rule['State'] == 'DISABLED':
            msg = "Scheduled Jobs are already disabled, no changes were made"
        else:
            cw_events.disable_rule(Name=start_event)
            cw_events.disable_rule(Name=stop_event)
            msg = "Scheduled Jobs have been disabled"
            req = urllib.request.Request('https://slack.com/api/chat.postMessage?token='+slack_token+'&channel='+channel+'&text=Scheduled%20Jobs%20have%20been%20disabled&as_user=true&pretty=1')
            resp = urllib.request.urlopen(req)

        body = {
            "message": msg,
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