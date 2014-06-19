python-dataanalysis
===================

python-dataanalysis is collected code snippets that are the outcome of a corpoate Python study group exercises.
#Motivation?
These little software snippets solve a number of common data problems and demonstrate how to use several key libraries.
#What is built so far?
Sessions:

1. ZipCode-Distance: Distance MongoDB zipcodes driven geographical distance calculator from a city/town.

##ZipCode-Distance
###Mongo ORM
This is a basic implementation of MongoEngine's ORM features where we converted zipcodes into Zips object.

###GeoDistance Algorithm
We used distance algorithm from geopy with declared points from lat/long information from Zipcodes dataset.

###What libraries are we using?
        
* [Mongoengine] (http://mongoengine.org/)  
* [Geopy](https://code.google.com/p/geopy/) 

###Additional Resources
You can find zipcodes json file from [mongo site](http://docs.mongodb.org/manual/tutorial/aggregation-zip-code-data-set/):
 
###Notes
Zipcodes json file contains _id entries as zipcodes, however those types of entries are not treated well with mongoengine... replace _id with zipcode as a field, let Mongo create 
its own objectIds as a work around.