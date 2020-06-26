import os

import boto3
dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # delete the todo from the database
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "headers" : {
            'Access-Control-Allow-Headers': 'Content-Type,Origin,Accep,\
                X-Requested-With,Content-Type,Access-Control-Request-Method,\
                    Access-Control-Request-Headers,Authorization',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE'
        }
    }

    return response