def count_failing_grades(grades):
    gcount = 0
    for grade in grades:
        if grade < 60 :
            gcount = gcount + 1
    
    return gcount

print("Count Failing Grades")
print("59,70,89,42 -->", count_failing_grades([59,70,89,42]))
print("32,48,90,52,74 -->", count_failing_grades([32,48,90,52,74]))

def count_act_scores(scores) :
    validscore = 0
    for score in scores :
        if score > 0 and score < 37 :
            validscore = validscore + 1

    return validscore

print("Count Valid ACT Scores")
print("32,48,21,4,36 -->", count_act_scores([32,48,21,4,36]))

def number_sum(list) : 
    sum = 0
    for number in list :
        sum = sum + number
    
    return sum

print("Number Sum")
print("10 + 4 + 6 + 20 =", number_sum([10,4,6,20]))

def average_act_score(scores) :
    scorecount = 0
    scoretotal = 0
    for score in scores :
        if score > 0 and score < 37 :
            scorecount = scorecount + 1
            scoretotal = 0 + score

    return scoretotal / scorecount

print("Average ACT Score")
print("32,48,21,4,36 -->", average_act_score([32,48,21,4,36]))

def all_true(list) :
    for true_false in list:
        if  true_false == False :
            return False
    return True

print("All True")
print("True,True,True -->", all_true([True, True, True]))
print("True,True,False -->", all_true([True, True, False]))

def any_true(list) : 
    for true_false in list:
        if true_false == True :
            return True
    return False

print("Any True")
print("True,False,False -->", any_true([True, False, False]))
print("True,True,False -->", any_true([True, True, False]))
print("False,False,False -->", any_true([False, False, False]))

def mostly_true(list) : 
    truecount = 0
    falsecount = 0
    for true_false in list :
        if true_false == True :
            truecount = truecount +1
        elif true_false == False :
            falsecount = falsecount + 1
    if truecount > falsecount :
        return True
    return False

print("Mostly True")
print("True,False,False -->", mostly_true([True, False, False]))
print("True,True,False -->", mostly_true([True, True, False]))
print("False,False,False -->", mostly_true([False, False, False]))
print("True,True,False -->", mostly_true([True, True, False]))

def has_vowel(letters) :
    for letter in letters :
        if letter in ["a","e","i","o","u"] : 
            return True
    return False

print("has_vowel")
print("a,h,j,e,h,s", has_vowel(["a","h","j","e","h","s"]))
print("l,m,n,p", has_vowel(["l","m","n","p"]))