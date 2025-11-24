from pymongo import MongoClient 
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="app/.env")

mongo_uri = os.getenv("MONGO_URI")
database_name = os.getenv("DATABASE_NAME")


if not mongo_uri or not database_name:
    raise ValueError("Faltan variables de MONGO_URI o DATABASE_NAME en el archivo .env")

client = MongoClient(mongo_uri)
db = client[database_name]




