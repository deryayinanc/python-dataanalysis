from mongoengine import *
from models.zips import Zips
from geopy import distance
from geopy import Point

connect('scratch', host='mongodb://142.133.150.180/scratch')

# zipins = Zips(zipcode=999999, city="testlocation", loc=[1.0,1.0],pop=12345, state="ZZ").save()

locationList = []
location = {}
distanceList = []

for zip in Zips.objects:
    locationList.append(zip)

for location1 in locationList:
    if location1.city=="BEVERLY HILLS" :
        point1 = Point(location1.loc[0], location1.loc[1])
        for location2 in locationList:
            if location1 != location2 and location2.city !="BEVERLY HILLS":
                point2 = Point(location2.loc[0], location2.loc[1])
                if(distance.distance(point1, point2) < 5):
                    distanceList.append(location2)

for location in distanceList:
    print (location.city, location.zipcode)
