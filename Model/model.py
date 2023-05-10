from dataclasses import dataclass, asdict
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import tzlocal
from bson.codec_options import CodecOptions
from typing import Optional

# Make sure constants.py exists
try:
    from . import constants
except ImportError as err:
    raise SystemExit('You must have constants.py in the Model folder. This file is not included in the GitHub repository because it contains an API key')


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
misc = db['misc'].with_options(codec_options=CodecOptions(
    tz_aware=True, tzinfo=tzlocal.get_localzone()))


# Make the FacultyProfile dataclass
@dataclass
class FacultyProfile():
    name: str
    department: str = None
    rawHtml: str = None
    tel: str = None
    email: str = None
    address: str = None
    url: str = None
    scholar_url: str = None

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

def update_by_name(profiles: list[FacultyProfile]):
    # For each profile, upsert that profile into the database
    for profile in profiles:
        # Replace the faculty member in the database with the new profile
        faculty_members.replace_one(
            {'name': profile.name}, asdict(profile), upsert=True)


def update_last_update_time(datetime: datetime):
    misc.replace_one({'last_updated': {'$exists': True}}, {
                     'last_updated': datetime}, upsert=True)


def get_last_update_time() -> Optional[datetime]:
    """Returns last update time as a datetime object converted to local timezone"""
    if response := misc.find_one({'last_updated': {'$exists': True}}):
        return response['last_updated']
    return None


# Dump entire database for the CSV
# This is just to make sure only necessary data is gathered
def csv_dump(projection: list[str] = ['name']) -> list[FacultyProfile]:
    """Dumps the database as a list of FacultyProfile objects. Uses a projection to save on bandwidth.

    ### Args:
        projection (list[str], optional): A list of fields to get. 'name' is added if not present. Defaults to ['name'].

    ### Returns:
        list[FacultyProfile]: A list of FacultyProfile objects that have elements from projection
    """    
    if 'name' not in projection:
        projection.append('name')
    
    projection_dict = {field: True for field in projection}
    projection_dict['_id'] = False
    cursor = faculty_members.find(projection=projection_dict)
    
    # At this stage cursor is an Iterable[dict]
    return [FacultyProfile(**faculty_member) for faculty_member in cursor]
