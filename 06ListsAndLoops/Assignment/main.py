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
            scoretotal = scoretotal + score
    
    if scorecount == 0:
        return None
    
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

def all_the_same(numbers) :
    first = numbers[0]
    for num in numbers :
        if num != first :
            return False
    return True
print("All the same")
print("5,5,5", all_the_same([5,5,5]))
print("5,4,5", all_the_same([5,4,5]))

def increasing(list) :
    greaternum = list[0]-1
    for number in list :
        if number > greaternum :
            greaternum = number
        else: return False
    return True

print("increasing")
print("1,2,4", increasing([1,2,4]))
print("4,6,2", increasing([4,6,2]))
print("0,1,4", increasing([0,1,4]))

def is_incrementing(list) : 
    nextnumber = list[0]+1
    for number in list :
        if number+1 == nextnumber :
            nextnumber = nextnumber+1
        else: return False
    return True

print("Is Incrementing")
print("1,2,3", is_incrementing([1,2,3]))
print("4,6,2", is_incrementing([4,6,2]))
print("0,1,4", is_incrementing([0,1,4]))


def has_adjacent_repeat(list) :
    specialnumb = list[1]
    for number in list :
        if number == specialnumb :
            return True
        else: specialnumb = number
    return False

print("Has Adjacent Repeat")
print("1,2,2", has_adjacent_repeat([1,2,2]))
print("1,2,3", has_adjacent_repeat([1,2,3]))
print("0,1,4", has_adjacent_repeat([0,1,4]))

def sum_with_skips(list) :
    ignoring = False
    total = 0
   
    for number in list :
        if ignoring == True and number == -1:
            ignoring = False
        elif number == -1:
            ignoring = True
        elif ignoring == False:
            total = total + number

    return total

print("1,2,-1,2,1,-1,1", sum_with_skips([1,2,-1,2,1,-1,1]))
print("1,1,-1,1,-1,1,4", sum_with_skips([1,1,-1,1,-1,1,4]))

        