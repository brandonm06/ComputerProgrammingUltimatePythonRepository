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


def furthestcompass() :
   # fnorth = {"coordinate": 0, "name": ""}
    fnorth = [0, ""]
    fsouth = [cities[0]["latitude"], ""]
    feast = [cities[0]["longitude"], ""]
    fwest = [0, ""]
    for city in cities :
        if city["latitude"] > fnorth[0] :
            fnorth[0] = city["latitude"]
            fnorth[1] = city["city"]
    for city in cities :
        if city["latitude"] < fsouth[0] :
            fsouth[0] = city["latitude"]
            fsouth[1] = city["city"]
    for city in cities :
        if city["longitude"] > feast[0] :
            feast[0] = city["longitude"]
            feast[1] = city["city"]
    for city in cities :
        if city["longitude"] < fwest[0] :
            fwest[0] = city["longitude"]
            fwest[1] = city["city"]
    print ("Furthest North:", fnorth,"Furthest South:", fsouth, "Furthest East:", feast, "Furthest West:", fwest )


def fastestgrowshrink():
    fshrink = [0,""]
    fgrow = [0,""]
    for city in cities :
        if city["growth_from_2000_to_2013"] > fgrow[0] :
            fgrow[0] = city["growth_from_2000_to_2013"]
            fgrow[1] = city["city"]
    for city in cities :
        if city["growth_from_2000_to_2013"] < fshrink[0] :
            fshrink[0] = city["growth_from_2000_to_2013"]
            fshrink[1] = city["city"]
    print("Fastest growth:", fgrow, "Fastest shrink:", fshrink)
fastestgrowshrink()
