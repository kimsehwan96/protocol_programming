import json
import os

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.scan()

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder),
        "headers" : {
            'Access-Control-Allow-Headers': 'Content-Type,Origin,Accep,\
                X-Requested-With,Content-Type,Access-Control-Request-Method,\
                    Access-Control-Request-Headers,Authorization',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
        }
    }

    return response
