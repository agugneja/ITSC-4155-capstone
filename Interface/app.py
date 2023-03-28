from flask import Flask, render_template, url_for

# Passed from app.py
def getFunctions(getScrape):
    global scrape 
    scrape = getScrape

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

# Temp:
@app.post('/manual-entry')
def manual_update():
    scrape()
