from ast import Lambda
import csv
from email import header 


data = []

with open("archive_dataset.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)

headers = data[0]

planet_data = data[1:]


for data_point in planet_data:
    
    #converting planet lines in lowercase
    data_point[2] = data_point[2].lower()


#sorting planet data in alphabetical order

planet_data.sort(key=lambda planet_data: planet_data[2])

with open("archive_dataset_sorted.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)


with open("archive_dataset_sorted.csv") as input, open("archive_dataset_sorted1.csv", "w", newline="" ) as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)  

