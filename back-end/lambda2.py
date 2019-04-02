import http.client
import json
import urllib
import boto3
import datetime
import time
from botocore.vendored import requests


def lambda_handler(event, context): 

    sqs=boto3.resource('sqs')
    queue=sqs.get_queue_by_name(QueueName='CC-HW2')

    for message in queue.receive_messages():

        body = json.loads(message.body)
        location = body['Location']
        foodtype  = body['FoodType']
        date = body['Date']
        time = body['Time']
        people = body['People']
        phone = body['Phone']
        message.delete()

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('yelp-resturants')

        # elastic search
        es_url = 'https://search-restaurants-l7a6popsqvxfdqctb4sebw2scu.us-east-1.es.amazonaws.com/elasticdomain/_search?q=' + foodtype
        response = requests.get(es_url)
        data = response.json()
        data_list = []
        for i in range(0, 3):
            data_list.append(data['hits']['hits'][i]['_source']['RestaurantID'])

        # dynamodb
        response = []
        for i in range (3) :
            response.append(table.get_item(Key = {'BusinessID': data_list[i]}))
        
        restaurant_name_list=[]
        restaurant_location_list=[]
        
        for item1 in response:
            print(item1["Item"]["address"])
            restaurant_location_list.append(item1["Item"]['address'])
            restaurant_name_list.append(item1["Item"]['Name'])
        
        result=[]

        for j in range(3):
            stringVariable = str(j+1)+ ". "+ restaurant_name_list[j] + "located at " + restaurant_location_list[j] + "."
            result.append(stringVariable)
        
        stringToOutput = ""
        for k in range(3):
            stringToOutput = stringToOutput + result[k] + " , "
        message = "Hello! Here are my "+ foodtype + " restaurant suggestions for " + people + " people, for " + date + " at " + time + " : \n"
        message = message + stringToOutput
        
        # SNS code
        client=boto3.client('sns')
        # client.subscribe(TopicArn = 'arn:aws:sns:us-east-1:028352437066:CC-HW2', Protocol='Email', Endpoint = mail)
        # client.publish(TopicArn = 'arn:aws:sns:us-east-1:028352437066:CC-HW2', Message = message)
        client.publish(PhoneNumber = phone, Message = message)
    return 0

    # curl -XPOST elasticsearch_domain_endpoint/_bulk --data-binary @bulk_movies.json -H 'Content-Type: application/json'
