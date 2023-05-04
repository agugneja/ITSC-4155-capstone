from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.triggers.cron import CronTrigger
from apscheduler.job import Job
from typing import Union
import re
from datetime import datetime
from zoneinfo import ZoneInfo

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
scheduler.start()


def add_job(months: Union[int, str, list[Union[int, str]], None],
            days: Union[int, str, list[Union[int, str]], None],
            start_date: Union[str, datetime, None] = None) -> Job:
    """Add/update the scraping schedule

    ### Args:
        months: a list of months, a single month, or a comma-seperated list of months. Can be either a number [1-12] or the first three letters of the month.
        days: a list of days, a single day, or a comma-seperated list of days.
        start_date: earliest possible date/time to trigger on (inclusive). Can be a str formatted in ISO 8601 or a datetime

    ### Raises:
        ValueError: If ranges are used or if CronTrigger raises ValueError.

    ### Returns:
        Job: The Job that was added
    """

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

    # Avoid ranges and other weird things.
    # These are supported by CronTrigger, but don't want to deal with them.
    if isinstance(monthstr, str) and re.search('/|-|th|last', monthstr):
        raise ValueError('That kind of expression is not supported:', monthstr)
    if isinstance(daystr, str) and re.search('/|-|th|last', daystr):
        raise ValueError('That kind of expression is not supported:', daystr)

    # Create the jobs
    trigger = CronTrigger(month=monthstr, day=daystr,
                          start_date=start_date, jitter=60)
    return scheduler.add_job(func=scrape, trigger=trigger)


def get_job() -> dict:
    """Get the job. There should only be one in the database at a time.

    ### Returns:
        dict: A dictionary containing:
        - `months: list[str]`
        - `days: list[int]`
        - `start_date: datetime`
        - `next_fire_time: datetime`
    """
    FIELD_NAMES = CronTrigger.FIELD_NAMES

    # Because of the way cron works, I will assume there is only one job
    trigger = scheduler.get_jobs()[0].trigger
    fields = dict(zip(FIELD_NAMES, trigger.fields))
    months = fields['month'].expressions
    days = fields['day'].expressions

    # Extract the actual expression
    job_attrs = {'months': [str(x) for x in months],
                 'days': [x.first for x in days],
                 'start_date': trigger.start_date,
                 'next_fire_time': trigger.get_next_fire_time(None, datetime.now(ZoneInfo('America/New_York')))}
    return job_attrs
