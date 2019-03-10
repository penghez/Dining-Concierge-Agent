import json
import boto3


def lambda_handler(event, context):
    msg = {}

    client = boto3.client('lex-runtime')
    params = event['queryStringParameters']
    print(event)
    bot_response = client.post_text(
        botName='DiningBot',
        botAlias='$LATEST',
        userId='DiningBot',
        inputText=params['query']
    )

    msg["botresp"] = bot_response["message"]
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Access-Control-Allow-Headers,Origin,X-Requested-With,Authorization,Content-Type,Accept,Z-Key',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(msg)
    }
