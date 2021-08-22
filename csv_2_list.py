import csv

results = []
whole = '/home/shantanu/Downloads/noeven123.csv'
# with open('/home/shantanu/imp python/newcsv/4.csv', newline='') as inputfile:
with open(whole, newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row[0])