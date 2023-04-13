from flask import Flask, render_template, url_for, send_file

from WebScraper.webScraper import main as scrape
# Passed from app.py
# def get_functions(get_scrape):
#     global scrape 
#     scrape = get_scrape

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/schedule')
def schedule():
    return render_template('schedule.html')

@app.get('/manual-entry')
def manual_entry():
    return render_template('manual-entry.html')

@app.get('/help')
def help():
    return render_template('help.html')
@app.get('/csvdownload')
def csv():
    return send_file('static/example.csv',
        mimetype='text/csv',
        download_name='example.csv',
        as_attachment=True)
# Temp:
@app.post('/manual-entry')
def manual_update():
    scrape()
