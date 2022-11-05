import pycristoforo as pyc
import numpy
import shapely
from countrygroups import EUROPEAN_UNION
import random
def generate():
    lscorjson = []
    coordls =[]
    numofpoints = 1#int(input("How many points would you like"))

    for i in range(numofpoints):
        curcountry = random.choice(EUROPEAN_UNION)
        country = pyc.get_shape(curcountry)
        points = pyc.geoloc_generation(country, 1, curcountry)
        cur = points[0]
        coord = cur['geometry']['coordinates']
        coord=[coord[1],coord[0]]
        lscorjson.append(coord)
    return lscorjson

#print(lscorjson)#fuck yeah

#time to print these coordinates on a map
