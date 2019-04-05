import csv
file = open("file2.csv", "r")
reader = csv.reader(file)
ids = []
for line in reader:
    if reader.line_num == 1:
        continue
    ids.append(line[0])


file.close()

rows_for_file3 = []
file = open("file1.csv", "r")
reader = csv.reader(file)
for line in reader:
    if line[0] not in ids:
        rows_for_file3.append(line)

file.close()
print(len(rows_for_file3))


file = open("file3.csv", "w", newline='')
writer = csv.writer(file)

for line in rows_for_file3:
    writer.writerow(line)

file.close()
