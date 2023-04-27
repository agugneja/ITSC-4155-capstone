from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.triggers.cron import CronTrigger
from bson.objectid import ObjectId

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
def add_job(year=None, month=None, day=None, week=None, day_of_week=None,
            hour=None, minute=None, second=None, start_date=None,
            end_date=None, departments: list[str] = None):
    trigger = CronTrigger(year=year, month=month, day=day, week=week,
                          day_of_week=day_of_week, hour=hour, minute=minute,
                          second=second, start_date=start_date, end_date=end_date)

    scheduler.add_job(func=scrape, trigger=trigger, kwargs={
                      'departments_to_scrape': departments})


# Get all jobs this is just here to expose the scheduler function
get_jobs = scheduler.get_jobs


# Update a job
def update_job(id: ObjectId) -> bool:
    # TODO
    pass


# Delete a job
def delete_job(id: ObjectId) -> bool:
    # TODO
    pass
