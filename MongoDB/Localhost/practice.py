import pprint
import os
import pymongo

MONGODB_URL = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(MONGODB_URL)

print(client.list_database_names())