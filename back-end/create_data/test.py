import boto3


def main():

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('yelp-restaurants')
    print (table.creation_date_time)
    response = table.get_item(
        Key = {
            'BusinessID': 'IhSVn0TaX8xXb3wcQ-fgcA'
        })
    item = response['Item']
    print(item)

if __name__ == "__main__":
    main()