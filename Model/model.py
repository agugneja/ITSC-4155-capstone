from dataclasses import dataclass, asdict
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from . import constants

# Connect to the server
connect_URI = f'mongodb+srv://{constants.MONGODB_USERNAME}:{constants.MONGODB_PASSWORD}@cluster0.yex3ra0.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(host=connect_URI, server_api=ServerApi("1"))

# Test connection
client.admin.command('ping')
print("Successfully connected to MongoDB")


# Make the FacultyProfile dataclass
@dataclass
class FacultyProfile():
    name: str
    rawHtml: str = None
    tel: str = None
    email: str = None
    url: str = None


# Define collections
db = client.itsc4155_team15
faculty_members = db.facultyMembers


# Define some functions

# For each profile, upsert that profile into the database
def update_by_name(profiles: list[FacultyProfile]):

    for profile in profiles:
        # Replace the faculty member in the database with the new profile
        faculty_members.replace_one(
            {'name': profile.name}, asdict(profile), upsert=True)


# Dump entire database for the CSV
# This is just to make sure only necessary data is gathered
def csv_dump() -> list[FacultyProfile]:
    cursor = faculty_members.find(
        projection={'url': True, 'name': True, 'rawHtml': True})

    return [FacultyProfile(faculty_member.get('name'),
                           faculty_member.get('rawHtml'),
                           url=faculty_member.get('url'))
            for faculty_member in faculty_members.find(projection={'name': True, 'rawHtml': True, 'url': True})]