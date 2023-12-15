import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/gradebook_data.csv", "r")
data = []
reader = csv.reader(f) 
for row in reader:
    data.append(row)

    

def totalgradesawarded() :
    Acount = 0
    Bcount = 0
    Ccount = 0
    Dcount = 0
    Fcount = 0
    for row in data :
        percent = int(row[2])
        if percent > 89 :
            Acount = Acount + 1
        elif percent > 79 :
            Bcount = Bcount + 1
        elif percent > 69 :
            Ccount = Ccount +1 
        elif percent > 59 :
            Dcount =Dcount +1
        elif percent > 0 :
            Fcount = Fcount +1
    print("A:", Acount,"B:", Bcount,"C:", Ccount,"D:", Dcount,"F:", Fcount)


def averagegrades(): 
    gradetotal = 0
    gradecount = 0
    for row in data :
        grade = int(row[1])
        score = int(row[2])
        if grade == 9 :
            gradecount = gradecount + 1
            gradetotal = gradetotal + score
    print("Freshman Average:", gradetotal/gradecount)
    gradetotal = 0
    gradecount = 0
    for row in data :
        grade = int(row[1])
        score = int(row[2])
        if grade == 10 :
            gradecount = gradecount + 1
            gradetotal = gradetotal + score
    print("Sophomore Average:", gradetotal/gradecount)
    gradetotal = 0
    gradecount = 0
    for row in data :
        grade = int(row[1])
        score = int(row[2])
        if grade == 11 :
            gradecount = gradecount + 1
            gradetotal = gradetotal + score
    print("Junior Average:", gradetotal/gradecount)
    gradetotal = 0
    gradecount = 0
    for row in data :
        grade = int(row[1])
        score = int(row[2])
        if grade == 12 :
            gradecount = gradecount + 1
            gradetotal = gradetotal + score
    print("Senior Average:", gradetotal/gradecount)


def failingseniors() :
    namelist = []
    for row in data :
        grade = int(row[1])
        score = int(row[2])
        name = (row[0])
        if grade == 12 and score < 60 :
            namelist.append(name)
    print(namelist)

failingseniors()
