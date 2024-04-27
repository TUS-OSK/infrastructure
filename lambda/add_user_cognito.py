import boto3
import os
import json

def lambda_handler(event, context):
    try:
        cognito = boto3.client('cognito-idp')
        body = json.loads(event['body'])
        print(body)
        username = body['username']
        password = body['password']
        userPoolId = os.environ['userPoolId']
        response = cognito.admin_create_user(
            UserPoolId = userPoolId,
            Username = username,
            TemporaryPassword = password,
        )
        print(response)
        return {
            'statusCode': 200,
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 400,
        }
