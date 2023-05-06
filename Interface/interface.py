from datetime import datetime
from flask import Flask, render_template, url_for, send_file, make_response, Response, request, redirect, flash, session
import csv
import json
from bson import json_util, ObjectId
from io import StringIO
import re

from WebScraper.webscraper import main as scrape
from Model import model
from dataclasses import dataclass, asdict
from Schedule import scheduler
from WebScraper import webscraper
from flask_sock import Sock
import asyncio
from threading import Thread
from WebScraper.liststream import liststream
from datetime import timezone
from zoneinfo import ZoneInfo
import tzlocal
app = Flask(__name__)
# app.debug = True
app.secret_key = "password"
app.url_map.strict_slashes = False

sock = Sock(app)

@app.get('/')
def index():
    # current_schedule = scheduler.get_job()
    last_updated = None
    if webscraper.last_updated is not None:
        last_updated = webscraper.last_updated.astimezone(tzlocal.get_localzone())
        last_updated = last_updated.strftime('%b %w, %Y at %I:%M %p %Z')
    return render_template('index.html', scraper_running=webscraper.is_running, last_updated=last_updated)

@app.post('/')
def run_scraper():
    task = Thread(target=webscraper._main)
    task.start()
    return redirect('/')

@sock.route('/scraper_output')
def scraper_output(ws):
    liststream.reset_index()
    while webscraper.is_running:
        if liststream.index < len(liststream) - 1:
            ws.send(liststream.readline())
            
    # if webscraper stops running close connection
    ws.send('Web scraper finished! Redirecting...')
    ws.close()
        

@app.get('/last_updated')
def get_last_updated_time():
    return json.dumps(webscraper.last_updated.isoformat())

@app.get('/schedule')
def schedule():
    current_schedule = scheduler.get_job()

    months = current_schedule['months']
    days = current_schedule['days']
    start_date_iso = current_schedule['start_date'].date().isoformat() if type(current_schedule['start_date']) == datetime else None
    # next_fire_time is not important for this page

    return render_template('schedule.html', months=months, days=days, start_date=start_date_iso)


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
    months = form_data.get('months')
    days = form_data.get('days')
    start_date = form_data['start_date'][0]
    # Handle start_date not existing
    if  start_date == '':
        start_date = None
    
    print(form_data)

    job = scheduler.add_job(months, days, start_date)

    if job is not None:
        flash('Job successfully added', 'message')
    else:
        flash('Job not added', 'error')

    return redirect('/schedule')
