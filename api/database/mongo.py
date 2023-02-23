from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

db = MongoClient(os.getenv("URL")).get_database("euro2020")

