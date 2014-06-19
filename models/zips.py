from mongoengine import *

class Zips(Document):
    city = StringField(required=True)
    loc = ListField(FloatField())
    pop = IntField(required=True)
    state = StringField(required=True)
    zipcode = IntField(required=True)

