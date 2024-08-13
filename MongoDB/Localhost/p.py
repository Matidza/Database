import os
import pprint
from pymongo import MongoClient

MONGODB_URL = 'mongodb://localhost:27017/'
client = MongoClient(MONGODB_URL)
dbs = client.School
collect = dbs.list_collection_names()
print(collect)



import os
import pprint
from pymongo import MongoClient

MONGODB_URL = 'mongodb://localhost:27017/'
client = MongoClient(MONGODB_URL)
db = client.learn
database = db.list_database_names()
print(cdatabase)