from datetime import datetime, time
from flask import Flask, render_template, make_response, Response, request, redirect, flash
import csv
import json
from bson import json_util, ObjectId
from io import StringIO
import re

from WebScraper.webscraper import main as scrape
from Model import model
from Schedule import scheduler


app = Flask(__name__)
app.debug = True
app.secret_key = "password"
app.url_map.strict_slashes = False


@app.get('/')
def index():
    job = scheduler.get_job()
    next_scrape = scheduler.get_next_fire_time_delta()

    if None in (job, next_scrape):
        flash('No job in database', 'error')
        return render_template('index.html')
    else:
        # Stringify months and days
        month_str = job['months'][0].capitalize() if job['months'] != [] else None
        for month in job['months'][1:]:
            month_str += ', ' + month.capitalize()
        day_str = str(job['days'][0]) if job['days'] != [] else None
        for day in job['days'][1:]:
            day_str += ', ' + str(day)
        
        job_times = {
            'months': month_str,
            'days': day_str
        }
        
        print(job_times)
        
        next_scrape_times = {
            'months': next_scrape.months,
            'days': next_scrape.days,
            'hours': next_scrape.hours,
            'minutes': next_scrape.minutes
        }

        return render_template('index.html', job=job_times, next_scrape=next_scrape_times)


@app.get('/schedule')
def schedule():
    current_schedule = scheduler.get_job()

    if current_schedule is not None:
        months = current_schedule['months']
        days = current_schedule['days']

        exec_time = current_schedule['exec_time']
        exec_time_iso = exec_time.isoformat(
            'minutes') if isinstance(exec_time, time) else None

        start_date = current_schedule['start_date']
        start_date_iso = start_date.date().isoformat(
        ) if isinstance(start_date, datetime) else None

        return render_template('schedule.html', months=months, days=days, exec_time=exec_time_iso, start_date=start_date_iso)
    else:
        return render_template('schedule.html')


@app.get('/manual-entry')
def manual_entry():
    # repeated here instead of making a global so that it will update each
    # time it's needed
    return render_template('manual-entry.html')


@app.get('/search-profiles')
def profile_search():
    name = request.args.get('name')
    _id = request.args.get('_id')
    if _id is None or _id == "":
        profile = None
    else:
        profile = model.faculty_members.find_one({
            '_id': ObjectId(_id),
            # case insensitive search
            'name': {'$regex': re.escape(name), '$options': 'i'}})
        if profile is None:
            flash(f'Faculty member "{name}" not found', 'error')

    return render_template('profile.html', profile=profile)


@app.get('/faculty-profiles')
def get_profiles():
    # need to use the bson json_util to properly convert bson to valid json
    return json.loads(json_util.dumps(model.faculty_members.find({}, {'_id': 1, 'name': 1, 'email': 1})))


@app.delete('/delete/<_id>')
def delete_faculty_member(_id):
    model.faculty_members.delete_one({'_id': ObjectId(_id)})
    return Response(status=204)


@app.get('/help')
def help():
    return render_template('help.html')


@app.get('/csvdownload')
def csv_download():
    # Make a bunch of objects
    faculty_members = model.csv_dump()

    # This is needed because CSV needs to think it's outputting to a file
    csvString = StringIO()

    # Initialize a CSV writer
    writer = csv.writer(csvString, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['site', 'type', 'action', 'title', 'excerpt', 'content', 'date', 'author', 'slug',
                    'status', 'menu-order', 'password', 'categories', 'tags', 'taxonomy-{name}', 'meta-{name}'])

    # Fill the CSV
    for faculty_member in faculty_members:
        writer.writerow([faculty_member.url, 'post', 'update',
                        faculty_member.name, None, faculty_member.rawHtml])

    # Send a response
    filename = 'example'
    response = make_response(csvString.getvalue())
    response.mimetype = 'text/csv'
    response.headers['Content-Disposition'] = f'attachment; filename={filename}.csv'
    return response

    # return send_file('static/example.csv',
    #     mimetype='text/csv',
    #     download_name='example.csv',
    #     as_attachment=True)


# Temp:
@app.post('/manual-entry')
def update():
    _id = request.form.get('_id')
    db_filter = {'_id': ObjectId(_id)}

    faculty_dict = {
        'name': request.form.get('new_name'),
        'department': request.form.get('department'),
        'rawHtml': request.form.get('profile'),
        'tel': request.form.get('number'),
        'email': request.form.get('email'),
        'address': request.form.get('location'),
        'url': request.form.get('url')
    }

    for field, value in faculty_dict.items():
        if value is not None:
            model.faculty_members.update_one(
                db_filter, {'$set': {field: value if value != '' else None}})

    return redirect(f'search-profiles?name={faculty_dict["name"]}&_id={_id}')

# Change schedule


@app.post('/schedule')
def update_schedule():
    form_data = request.form.to_dict(flat=False)

    # Try to get months and days
    try:
        months = form_data['months']
        days = form_data['days']
    except KeyError as err:
        if err.args:
            flash(f'You must select at least one {err.args[0][:-1]}', 'error')
        else:
            flash('One or more fields are not filled out correctly', 'error')
        return redirect('/schedule')

    # Try to get time and start_time, these can be blank, or nonexistent
    try:
        start_date = form_data['start_date'][0]
        if start_date == '':
            start_date = None
    except KeyError:
        start_date = None
    try:
        exec_time = form_data['exec_time'][0]
        if exec_time == '':
            exec_time = None
    except KeyError:
        exec_time = None

    # If time is not None, it should be valid
    if exec_time is not None:
        try:
            exec_time = time.fromisoformat(exec_time)
        except ValueError:
            flash('Invalid time input', 'error')
            return redirect('/schedule')

    print('months: ', months)
    print('days: ', days)
    print('exec_time: ', exec_time)
    print('start_date: ', start_date)

    job = scheduler.update_job(months, days, exec_time,  start_date)

    if job is not None:
        flash('Job successfully added', 'message')
    else:
        flash('Job not added', 'error')

    return redirect('/schedule')
