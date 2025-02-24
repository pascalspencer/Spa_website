from pymongo import MongoClient


def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://spencerincdev:<db_password>@zodiac.k8rucbs.mongodb.net/?retryWrites=true&w=majority&appName=Zodiac"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['client_list']
  

dbname = get_database()
collection_name = dbname["client_details"]