import csv
from socket import create_server

dataset1 = []
dataset2 = []

with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
    
with open("archive_dataset_sorted1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

headers1 = dataset1[0]
planet_data1 = dataset1[1:]

headers2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = headers1 + headers2

planetsdata = []

for index, datarow in enumerate(planet_data1):
    planetsdata.append(planet_data1[index] + planet_data2[index])

with open("merged_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetsdata)
    