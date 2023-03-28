from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import constants

# Connect to the server
connectUri = f'mongodb+srv://{constants.MONGODB_USERNAME}:{constants.MONGODB_PASSWORD}@cluster0.yex3ra0.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(host=connectUri, server_api=ServerApi("1"))

# Test connection
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB")
except Exception as e:
    print(e)

# Define collections
db = client.itsc4155_team15

facultyMembers = db.facultyMembers
urls = db.urls
