import csv
import os

# allow files to be read from the current location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()

print(words[1])