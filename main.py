import csv

with open('sample.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile);   

    for row in reader:
        print(row['NAME'], row['TMAX'], row['TMIN'])