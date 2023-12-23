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
    success = list(filter(lambda x: x['launch success'] and not x ["upcoming"], launches))
    failed = list(filter(lambda x: not x['launch failed'] and not x ["upcoming"], launches))
    upcoming = list(filter(lambda x: x ["upcoming"], launches))

    return {'success': success, 'failed': failed, 'upcoming': upcoming}
    
launches = category(fetch_spacex_launches())
print(launches)





if __name__ == '__main__':
    app.run(debug=True)