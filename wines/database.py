import pymongo
from django.conf import settings
from pymongo import MongoClient

# client = MongoClient(settings.MONGO_URI, settings.MONGO_PORT)
# client = MongoClient('mongodb://localhost:27017/')
print ("adasdasdsad")
print (settings.MONGO_URI)
client = MongoClient(settings.MONGO_URI)
dbs = client.csvproject
