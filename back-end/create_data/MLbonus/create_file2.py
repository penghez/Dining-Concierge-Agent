import csv
import json

file = open("file1.csv", "r")
reader = csv.reader(file)
count = 0
rows_in_file2_1 = []
rows_in_file2_2 = []
for line in reader:
    if count == 100:
        break
    if line[1][0:7] == "['Thai'" and float(line[2]) >= 3.0 and int(line[3]) >= 100:
        print(line)
        rows_in_file2_1.append(line)
        count = count + 1
    else:
        if reader.line_num == 1:
            continue
        rows_in_file2_2.append(line)


file.close()
rows_in_file2_2 = rows_in_file2_2[0:100]
print(len(rows_in_file2_1))
print(len(rows_in_file2_2))


file = open("file2.csv", "w", newline='')
writer = csv.writer(file)
writer.writerow(['BusinessID', 'Cuisine', 'Rating', 'NumberOfReviews', "Recommended"])
for row in rows_in_file2_1:
    row.append(1)
    writer.writerow(row)
for row in rows_in_file2_2:
    row.append(0)
    writer.writerow(row)
file.close()
