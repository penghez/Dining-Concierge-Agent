import http.client
import urllib.parse
import base64
import json
import boto3
import decimal
import csv
from datetime import datetime as dt
    
def main():

    API_KEY = 'bUwim9s5gGcura_xgkycXp48YpqBGTd51DbHiKK2Ylks4EJUlXkrvW6ptZb_d6V_GmHeyAKO-3Ma7tYM1aFVhPIBbariUnKlTgAjdCwtH_nTaP_tJxXgvsUML9aCXHYx'
    headers = {'Authorization': 'Bearer %s' % API_KEY,}
    # client = boto3.client('dynamodb')
    dynamodb = boto3.resource('dynamodb')
    table= dynamodb.Table('yelp-restaurants')

    file = open("file1.csv", "a")
    writer = csv.writer(file)
    cuisine_list = ['Indian', 'American', 'Chinese', 'Thai','Mexican', 'Italian', 'Spanish', 'Turkish', 'Korean', 'Continental','Vietnamese', 'Irish', 'Greek', 'French', 'Japanese']

    writer.writerow(['BusinessID', 'Cuisine', 'Rating', 'NumberOfReviews'])
    conn = http.client.HTTPSConnection("api.yelp.com")
    for i in range (15):
        cuisine_type = cuisine_list[i]
        for j in range(0,500,20):

            params = {'limit':20, 'offset':j+1, 'location':'Manhattan', 'term':cuisine_type}
            param_string = urllib.parse.urlencode(params)
            url = "/v3/businesses/search?" + param_string
            conn.request("GET",url, headers = headers)
            response = conn.getresponse()
            data = response.read()
            data = json.loads(data.decode("utf-8"))
        
            restaurant_list = data["businesses"]
            
            for rest in restaurant_list:
                RestaurantID = rest['id']
                RestaurantName = rest['name']
                Rating = decimal.Decimal(str(rest['rating']))
                NumberOfReviews = rest['review_count']
                address = "\'{}\'".format(str(rest['location']['display_address'][0]))
                # print (address)
                Zipcode=str(rest['location']['zip_code'])
                coordinates_latitude = decimal.Decimal(str(rest['coordinates']['latitude']))
                coordinates_longitude = decimal.Decimal(str(rest['coordinates']['longitude']))
                cat_list = []
                for cat in rest['categories']:
                    cat_list.append(cat['title'])
                timestamp = str(dt.now())
                dynamo_data = {"BusinessID" : RestaurantID, "Name" : RestaurantName, "cuisine" : cat_list,\
                    "Rating" : Rating,"num_reviews" : NumberOfReviews,"address" : address, "Zip Code" : Zipcode,\
                    "latitude" : coordinates_latitude, "longitude" : coordinates_longitude, "timestamp" : timestamp}
                dynamo_data_actual = {key : value for key, value in dynamo_data.items() if value}

                response=table.put_item(Item = dynamo_data_actual)

                writer.writerow([RestaurantID, cat_list, Rating, NumberOfReviews])
    
    conn.close()
    file.close()


if __name__ == "__main__":
    main()