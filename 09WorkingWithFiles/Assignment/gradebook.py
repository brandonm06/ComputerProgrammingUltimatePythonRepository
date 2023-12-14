import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/gradebook_data.csv", "r")
data = []
reader = csv.reader(f) 
for row in reader:
    data.append(row)

print(data)

for row in data:
    

def totalgradesawarded() :
    Acount = 0
    Bcount = 0
    Ccount = 0
    Dcount = 0
    Fcount = 0