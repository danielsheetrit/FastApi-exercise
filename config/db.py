import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
conn = MongoClient(mongo_uri)
