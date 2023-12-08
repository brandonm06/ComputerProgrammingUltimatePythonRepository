def is_alliteration(wrd1,wrd2) :
    firstletter = wrd1[0]
    if wrd2[0] == firstletter :
        return True
    return False
print("Is Alliteration")
print("Hey, Hi -->", is_alliteration("Hey","Hi"))
print("Yes, No -->", is_alliteration("Yes","No"))

def count_vowels(word):
    vowelcount = 0
    for letters in word:
        if letters in "aeiou" :
            vowelcount = vowelcount + 1
    return vowelcount
print("Count Vowels")
print("lol -->", count_vowels("lol"))
print("alphabet -->", count_vowels("alphabet"))

def count_numbers(string) :
    numbercount = 0
    for variables in string :
        if variables in "1234567890" :
            numbercount = numbercount + 1
    return numbercount

print("Count Numbers")
print("sdf9843ujjs4 -->", count_numbers("sdf9843ujjs4"))
print("jy4398u03m2 -->", count_numbers("jy4398u03m2"))
print("32io54980ej -->", count_numbers("32io54980ej"))

def count_target_letters(word, letter) :
    lettercount = 0
    for letters in word :
        if letters in letter :
            lettercount = lettercount + 1
    return lettercount

print("Count Chosen Letter")
print("mississippi, p -->", count_target_letters("mississippi","p"))
print("alabama, a -->", count_target_letters("alabama","a"))

def in_alphabetical_order(word) :
    if len(word) == 0:
        return True
    
    firstletter = word[0]
    for letters in word :
        if letters > firstletter:
            firstletter = letters
        elif firstletter > letters:
            return False
    return True

print("Is in alphabetical order")
print("abcdef -->", in_alphabetical_order("abcdef"))
print("acegh -->", in_alphabetical_order("acegh"))
print("opale -->", in_alphabetical_order("opale"))

def alternate_case(word) : 
    result = ""
    uppercase = True
    for letter in word :
        if uppercase == True:
            result = result + letter.upper()
            uppercase = False
        elif uppercase == False :
            uppercase = True
            result = result + letter
    return result

print("Alternate Case")
print("hello -->", alternate_case("hello"))
print("brandon -->", alternate_case("brandon"))

def remove_vowels(word) : 
    result = ""
    for letter in word :
        if letter not in "aeiou" :
            result = result + letter
    return result

print("Remove Vowels")
print("mississippi -->", remove_vowels("mississippi"))
print("alabama -->", remove_vowels("alabama"))

def to_camel_case(phrase) :
    result = ""
    firstletter = False
    for letter in phrase :
        if firstletter == True :
            result = result + letter.upper()
            firstletter = False
        elif letter == " " :
            pass
            firstletter = True
        elif firstletter == False :
            result = result + letter
    return result
print("To Camel Case")
print("hi my name is brandon -->", to_camel_case("hi my name is brandon"))

def to_snake_case(phrase) :
    result = ""
    for letter in phrase:
        if letter == " " :
            result = result + "_"
        else: result = result + letter
    return result
print("To Snake Case")
print("hi my name is brandon -->", to_snake_case("hi my name is brandon"))

def without_duplicates(list) :
    previousnumber = list[0]-1
    result = []
    for number in list :
        if number == previousnumber :
            pass
            previousnumber = number
        else: 
            previousnumber = number
            result.append(number)
    return result

print("Without Duplicates")
print("1,1,2,4,4 -->", without_duplicates([1,1,2,4,4]))

def filter_valid_act_scores(list):
    valid = []
    for number in list :
        if number > 0 and number < 37 :
            valid.append(number)
        else: pass
    return valid

print("Filter Valid ACT Scores")
print("32,45,12,95,52 -->", filter_valid_act_scores([32,45,12,95,52]))


            
        
