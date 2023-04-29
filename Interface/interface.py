from flask import Flask, render_template, url_for, send_file, make_response, Response, request, redirect, flash, session
import csv, json
from bson import json_util, ObjectId
from io import StringIO
import re

from WebScraper.webscraper import main as scrape
from Model import model
# Passed from app.py
# def get_functions(get_scrape):
#     global scrape
#     scrape = get_scrape

app = Flask(__name__)
app.debug = True
app.secret_key = "password"
app.url_map.strict_slashes = False

@app.get('/')
def index():
    faculty_members = [faculty['name'] for faculty in model.faculty_members.find()]
    return render_template('index.html', faculty_members=faculty_members)

@app.get('/schedule')
def schedule():
    return render_template('schedule.html')


@app.get('/manual-entry') 
def manual_entry():
    # repeated here instead of making a global so that it will update each 
    # time it's needed
    faculty_members = [faculty['name'] for faculty in model.faculty_members.find()]
    return render_template('manual-entry.html', faculty_members=faculty_members)

@app.get('/search-profiles')

def profile_search():
    faculty_names = [faculty['name'] for faculty in model.faculty_members.find()]
    faculty_emails = [faculty['email'] if faculty['email'] else '' for faculty in model.faculty_members.find()]
    name = request.args.get('name')
    _id = request.args.get('_id')
    if _id is None or _id == "":
        profile = None
    else:
        # case insensitive search
        profile = model.faculty_members.find_one({'_id':ObjectId(_id)})
        # profile = model.faculty_members.find_one({'name':{ '$regex': re.escape(query), '$options': 'i'}})
        if profile is None:
            flash(f'Faculty member "{name}" not found')

    return render_template('profile.html', profile=profile, faculty_names=faculty_names, faculty_emails=faculty_emails)
    

@app.get('/faculty-profiles')
def get_profiles():
    # need to use the bson json_util to properly convert bson to valid json
    return json.loads(json_util.dumps(model.faculty_members.find({},{'_id':1, 'name':1, 'email':1})))

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
def manual_update():
    scrape()
