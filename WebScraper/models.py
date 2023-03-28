from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from . import constants

# Connect to the server
connectUri = f'mongodb+srv://{constants.MONGODB_USERNAME}:{constants.MONGODB_PASSWORD}@cluster0.yex3ra0.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(host=connectUri, server_api=ServerApi("1"))

# Test connection
client.admin.command('ping')
print("Successfully connected to MongoDB")

# Define collections
db = client.itsc4155_team15

facultyMembers = db.facultyMembers

# Define some functions

# For each profile, upsert that profile into the database
def updateByName(profileList):
    for profile in profileList:
        # Replace the faculty member in the database with the new profile
        facultyMembers.replace_one({'Title': profile['Title'], },
                                   {'Title': profile['Title'], 'Content': str(profile['Content'])},
                                   upsert=True)
