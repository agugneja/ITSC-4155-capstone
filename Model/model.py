from dataclasses import dataclass, asdict
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from . import constants


# Constants
DB_NAME = 'itsc4155_team15'
COLLECTION_NAME = 'facultyMembers'

# Connect to the server
connect_URI = f'mongodb+srv://{constants.MONGODB_USERNAME}:{constants.MONGODB_PASSWORD}@cluster0.yex3ra0.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(host=connect_URI, server_api=ServerApi("1"))

# Test connection
client.admin.command('ping')
print("Successfully connected to MongoDB")


# Define collections
db = client[DB_NAME]
faculty_members = db[COLLECTION_NAME]


# Make the FacultyProfile dataclass
@dataclass
class FacultyProfile():
    name: str
    department: str
    rawHtml: str = None
    tel: str = None
    email: str = None
    url: str = None

    # Explicit type cast to exclude casting None to str
    def __setattr__(self, __name: str, __value) -> None:
        if __value is not None:
            try:
                __value = str(__value)
            except ValueError as e:
                print("Error while casting: " + e)
        elif __name == 'name':
            raise TypeError("name is required")
        super().__setattr__(__name, __value)


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
