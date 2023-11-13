from stemmer_madura import stemmer as stemmerMadura
import csv

with open('tests/test__prefix.csv', 'r') as f:
  csv_reader = csv.reader(f, delimiter=';')
  for row in csv_reader:
    print(row[0] + ' -> ' + stemmerMadura(row[0]))




