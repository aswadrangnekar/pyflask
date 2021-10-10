import os

from flask import render_template
from flask import Flask

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    team = {'name': os.getenv('TEAM_NAME') or 'white'}
    
    return render_template('index.html', team=team)
