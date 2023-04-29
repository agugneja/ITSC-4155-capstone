from flask import Flask, render_template, url_for, send_file, make_response, Response, request, redirect, flash
import csv, json
from io import StringIO
import re

from WebScraper.webscraper import main as scrape
from Model import model
from dataclasses import dataclass, asdict
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
    faculty_members = [faculty['name'] for faculty in model.faculty_members.find()]
    faculty_name = request.args.get('name')
    if faculty_name is None or faculty_name == "":
        profile = None
    else:
        # case insensitive search
        profile = model.faculty_members.find_one({'name':{ '$regex': re.escape(faculty_name), '$options': 'i'}})
        if profile is None:
            flash(f'Faculty member "{faculty_name}" not found')

    return render_template('profile.html', profile=profile, faculty_members=faculty_members)
    


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
# @app.post('/manual-entry')
# def manual_update():
#     scrape()

@app.post('/manual-entry')
def update():
    faculty_name = request.form.get('name')
    member = model.faculty_members.find_one({'name': faculty_name})
    filter = { '_id': member.get('_id')}

    if member is None or faculty_name == "" or filter is None:
        flash(f'Faculty Member {faculty_name} not found.')
    

    faculty_dict = {
        'name': request.form.get('name'),
        'department': request.form.get('department'),
        'rawHtml':request.form.get('profile'),
        'tel': request.form.get('number'),
        'email': request.form.get('email'),
        'location': request.form.get('location'),
        'url': request.form.get('url')
    }

    # faculty_dict['name'] = request.form.get('name')
    # faculty_dict['department'] = request.form.get('department')
    # faculty_dict['rawHtml'] = request.form.get('profile')
    # faculty_dict['tel'] = request.form.get('number')
    # faculty_dict['email'] = request.form.get('email')
    # faculty_dict['location'] = request.form.get('location')
    # faculty_dict['url'] =  request.form.get('url')

    for field, value in faculty_dict.items():
        if value is not None:
            model.faculty_members.update_one(filter, {'$set': {field: value}})
    
    return render_template('manual-entry.html')