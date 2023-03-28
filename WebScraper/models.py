from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from . import constants

# Connect to the server
connect_URI = f'mongodb+srv://{constants.MONGODB_USERNAME}:{constants.MONGODB_PASSWORD}@cluster0.yex3ra0.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(host=connect_URI, server_api=ServerApi("1"))

# Test connection
client.admin.command('ping')
print("Successfully connected to MongoDB")

# Define collections
db = client.itsc4155_team15

faculty_members = db.facultyMembers

# Define some functions

# For each profile, upsert that profile into the database
def update_by_name(profile_list):
    for profile in profile_list:
        # Replace the faculty member in the database with the new profile
        faculty_members.replace_one({'Title': profile['Title'], },
                                   {'Title': profile['Title'], 'Content': str(profile['Content'])},
                                   upsert=True)
