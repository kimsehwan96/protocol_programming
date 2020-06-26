import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder),
        "headers" : {
            'Access-Control-Allow-Headers': 'Content-Type,Origin,Accep,\
                X-Requested-With,Content-Type,Access-Control-Request-Method,\
                    Access-Control-Request-Headers,Authorization',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
        }
    }

    return response