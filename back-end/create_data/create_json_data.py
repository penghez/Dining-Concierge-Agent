import csv
import json


with open('predict.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	rownum = 0

	strrow1 = { "index" : { "_index": "elasticdomain", "_type" : "restaurant" } }

	for row in reader:

		colnum = 0
		for col in row:
			if colnum == 0:
				BusinessID = col
			elif colnum	== 1:
				cuisine = col
			colnum += 1


		strrow2 = { "RestaurantID": BusinessID,
					"Cuisine": cuisine}

		rownum += 1

		with open('data.json', 'a') as outfile:
			json.dump(strrow1, outfile)
			outfile.write('\n')
			json.dump(strrow2, outfile)
			outfile.write('\n')
			outfile.close()

	csvfile.close()

	print (rownum)