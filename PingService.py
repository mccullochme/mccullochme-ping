from flask import Flask, render_template
import requests
from requests.auth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=[GET, POST])
def index():
    return render_template("index.html")

@app.route('/ping', methods=[GET])
def ping():
    #create url
    #make request
    #return JSON payload with time request took
    return '<h1> hello <h1>'