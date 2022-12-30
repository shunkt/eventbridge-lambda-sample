import os
import json
import boto3
from dateutil.tz import gettz


def lambda_handler(event, context):

    TOPIC = os.getenv("SNS_TOPIC")
    if not TOPIC:
        raise Exception("SNS_TOPIC env. var. is not found")

    sns = boto3.client('sns')

    sns_params = {
        'TopicArn': TOPIC,
        'Message': "OK",
        'Subject': 'EventBridge Lambda Example'
    }

    response = sns.publish(**sns_params)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
