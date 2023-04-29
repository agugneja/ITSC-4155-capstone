from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.triggers.cron import CronTrigger
from bson.objectid import ObjectId
from typing import Union
import re

# Get the database info from the model, and the scraper function from webscraper
from Model.model import DB_NAME, client
from WebScraper.webscraper import main as scrape


# Initialize the scheduler
jobstores = {
    'default': MongoDBJobStore(database=DB_NAME, collection='jobs', client=client),
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
def add_job(months: Union[int, str, list[Union[int, str]], None],
            days: Union[int, str, list[Union[int, str]], None]):

    # Convert to strings if list
    if isinstance(months, list):
        monthstr = str(months[0])
        for month in months[1:]:
            monthstr += ',' + str(month)
    else:
        monthstr = months

    if isinstance(days, list):
        daystr = str(days[0])
        for day in days[1:]:
            daystr += ',' + str(day)
    else:
        daystr = days

    # Avoid ranges and onter weird things.
    # These are supported by CronTrigger, but don't want to deal with them.
    if isinstance(monthstr, str) and re.search('/|-|th|last', monthstr):
        raise ValueError('That kind of expression is not supported:', monthstr)
    if isinstance(daystr, str) and re.search('/|-|th|last', daystr):
        raise ValueError('That kind of expression is not supported:', daystr)

    # Create the jobs
    trigger = CronTrigger(month=monthstr, day=daystr, jitter=60)
    return scheduler.add_job(func=scrape, trigger=trigger)


# Because of the way cron works, I will assume there is only one job
# Get all jobs
def get_job() -> dict:
    trigger = scheduler.get_jobs()[0].trigger
    months = trigger.fields[1]
    days = trigger.fields[2]

    # Extract the actual expression
    months = [str(x) for x in months]
    days = [str(x) for x in days]

    return {'months': months, 'days': days}


# Update a job
def update_job():
    # TODO
    pass


# Delete a job
def delete_job():
    # TODO
    pass
