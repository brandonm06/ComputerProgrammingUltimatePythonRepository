import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()



def kansascities() : 
    citylist = []
    for city in cities:
        if city["state"] == "Kansas" :
            citylist.append(city["city"])
    print(citylist)


def longestname() :
    longestcity = ""
    longestcitychars = 0
    for city in cities :
        if len(city["city"]) > longestcitychars :
            longestcity = city["city"]
            longestcitychars = len(city["city"])
    print(longestcity)
longestname()

def 

