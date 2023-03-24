from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/manual-entry')
def manualEntry():
    return render_template('manual-entry.html')

@app.route('/help')
def help():
    return render_template('help.html')
