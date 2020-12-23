import sys
import csv

input_csv = sys.argv[1]
rel_set = []

with open(input_csv) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rel = row[1]
        rel_set.append(rel)

rel_set = set(rel_set)
print(rel_set)