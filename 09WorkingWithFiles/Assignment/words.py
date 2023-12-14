import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()



def mostvowels():
    vowelcount = 0
    mostvowelcount = 0
    mostvowels = "word"
    for word in words :
        vowelcount = 0
        for letter in word :
            if letter in "aeiou" :
                vowelcount = vowelcount + 1
        if vowelcount > mostvowelcount :
            mostvowelcount = vowelcount
            mostvowels = word
            vowelcount = 0
    return mostvowels
    


def averagewordlength() :
    wordscounttotal = 0
    wordslengthtotal = 0
    for word in words :
        wordscounttotal = wordscounttotal + 1
        for letter in word :
            wordslengthtotal = wordslengthtotal + 1
    return wordslengthtotal/wordscounttotal

print (averagewordlength())
