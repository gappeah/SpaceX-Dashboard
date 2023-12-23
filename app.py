from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def fetch_spacex_launches():
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return[]  
    
def category(Launches):
    success = list(filter(Launches, lambda x: x['launch success'] and not x ["upcoming"]))
    failed = list(filter(Launches, lambda x: not x['launch failed'] and not x ["upcoming"]))
    upcoming = list(filter(Launches, lambda x: x ["upcoming"]))
    

    
launches = fetch_spacex_launches()






if __name__ == '__main__':
    app.run(debug=True)