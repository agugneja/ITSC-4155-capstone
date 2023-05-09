from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.triggers.cron import CronTrigger
from apscheduler.job import Job
from apscheduler.jobstores.base import JobLookupError
from typing import Union
import re
from datetime import datetime, time
from zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta

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

ZONE_INFO = ZoneInfo('America/New_York')

def update_job(months: Union[int, str, list[Union[int, str]], None],
               days: Union[int, str, list[Union[int, str]], None],
               exec_time: Union[time, None] = None,
               start_date: Union[str, datetime, None] = None) -> Job:
    """Add/update the scraping schedule

    ### Args:
        months: a list of months, a single month, or a comma-seperated list of months. Can be either a number [1-12] or the first three letters of the month.
        days: a list of days, a single day, or a comma-seperated list of days.
        exec_time: The time to execute. If None, execute at 00:00:00. If not None, 60 seconds of jitter are applied to the job
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

    if exec_time is not None:
        hour = exec_time.hour
        minute = exec_time.minute
        jitter = 0
    else:
        hour = None
        minute = None
        jitter = 60

    # Create the jobs
    trigger = CronTrigger(month=monthstr, day=daystr, hour=hour,
                          minute=minute, start_date=start_date, jitter=jitter)

    # Try to just update the existing job
    try:
        return scheduler.reschedule_job(job_id='0', trigger=trigger)
    except JobLookupError:
        return scheduler.add_job(func=scrape, kwargs={'department_profiles': True, 'contact_info': False}, trigger=trigger, id='0')


def get_job() -> Union[dict, None]:
    """Get the job. There should only be one in the database at a time.

    ### Returns:
        dict: A dictionary containing:
        - `months: list[str]`
        - `days: list[int]`
        - `exec_time: (time | None)`
        - `start_date: datetime`
        - `next_fire_time: datetime`

        None: if there is no job
    """
    FIELD_NAMES = CronTrigger.FIELD_NAMES

    # Get the job
    if (job := scheduler.get_job('0')) is not None:
        trigger = job.trigger
        fields = dict(zip(FIELD_NAMES, trigger.fields))

        # Get days and months
        try:
            months = [str(x) for x in fields['month'].expressions]
        except TypeError:
            months = []
        try:
            days = [x.first for x in fields['day'].expressions]
        except (TypeError, AttributeError):
            days = []

        # Get time as a time object
        try:
            if not fields['hour'].is_default:
                exec_time = time(
                    hour=fields['hour'].expressions[0].first, minute=fields['minute'].expressions[0].first)
            else:
                exec_time = None
        except (TypeError, AttributeError):
            exec_time = None

        # Extract the actual expression
        job_attrs = {'months': months,
                     'days': days,
                     'start_date': trigger.start_date,
                     'exec_time': exec_time,
                     'next_fire_time': trigger.get_next_fire_time(None, datetime.now(ZONE_INFO))}
        return job_attrs
    else:
        return None

def get_next_fire_time_delta() -> Union[relativedelta, None]:
    """Get the next fire time for the job.

    Returns:
        datetime: Returns the next time the scheduler will fire if job['0'] exists.
        None: Returns None otherwise
    """
    
    now = datetime.now(ZONE_INFO)
    
    try:
        next_fire_time = scheduler.get_job('0').trigger.get_next_fire_time(previous_fire_time=None, now=now)
        return relativedelta(next_fire_time, now)
    except AttributeError as err:
        if err.args == ("'NoneType' object has no attribute 'trigger'",):
            # This just means that job['0'] does not exist
            return None
        else:
            # Rethrow any other errors
            raise err
