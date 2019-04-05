import csv
import json

file = open("./prediction.csv", "r")
reader = csv.reader(file)

rows_in_only1 = []
for line in reader:
    if line[4] == "1":
        rows_in_only1.append(line)
file.close()





file = open("only1.csv", "w", newline='')
writer = csv.writer(file)
writer.writerow(['BusinessID','NumberOfReviews','Rating','Cuisine','Recommended'])
for row in rows_in_only1:
    writer.writerow(row)

file.close()
