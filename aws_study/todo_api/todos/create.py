import json
import logging
import os
import time
import uuid

import boto3 # for aws service connect

dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Vaildation Failed")
        raise Exception("could not create todo item")

    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id' : str(uuid.uuid1()),
        'text' : data['text'],
        'checked' : False,
        'createdAt' : timestamp,
        'updatedAt' : timestamp
    }

    table.put_item(Item=item)

    response = {
        "statusCode" : 200,
        "body" : json.dumps(item)
    }

    return response