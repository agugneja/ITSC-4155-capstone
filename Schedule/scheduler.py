from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.triggers.cron import CronTrigger
from bson.objectid import ObjectId
from typing import Union

# Get the database info from the model, and the scraper function from webscraper
from Model.model import DB_NAME, client
from WebScraper.webscraper import main as scrape


# Initialize the scheduler
jobstores = {
    'default': MongoDBJobStore(database=DB_NAME, client=client)
}
executors = {
    # I think making max_workers = 1 still allows multiple threads
    'default': ProcessPoolExecutor(max_workers=1)
}
job_defaults = {
    'coalesce': True,
    'max_instances': 1
}

scheduler = BackgroundScheduler(
    jobstores=jobstores, executors=executors, job_defaults=job_defaults)


# Add a job
def add_job(months: Union[str, list[str], None],
            days: Union[int, str, list[Union[int, str]], None]):

    ALLOWED_MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug',
                      'sep', 'oct', 'nov', 'dec']

    # Convert months and days to lists if they weren't already
    if not isinstance(months, list):
        months = [month.strip() for month in months.split(',')]

    if isinstance(days, int):
        days = [days]
    elif not isinstance(days, list):
        # This can raise a ValueError if days is not
        days = [int(day) for day in days.split(',')]

    # Validate month and day
    for month in months:
        if month.lower() not in ALLOWED_MONTHS:
            raise ValueError('The month must be a valid month')
    for day in days:
        if not (1 <= day <= 31):
            raise ValueError('Day must be between 1 and 31')
    
    # Convert to strings
    monthstr = months[0]
    for month in months[1:]:
        monthstr += ',' + month
    
    daystr = str(days[0])
    for day in days[1:]:
        daystr += ',' + str(day)

    # Create the jobs
    trigger = CronTrigger(month=monthstr, day=daystr, jitter=60)
    scheduler.add_job(func=scrape, trigger=trigger)


# Get all jobs
def get_job():
    # TODO
    pass


# Update a job
def update_job(id: ObjectId) -> bool:
    # TODO
    pass


# Delete a job
def delete_job(id: ObjectId) -> bool:
    # TODO
    pass
