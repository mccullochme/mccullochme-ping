from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import requests
from requests.auth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/ping', methods=['GET'])
def ping():
    url = 'https://mccullochme-pong.herokuapp.com/'
    request = requests.get(url, auth=HTTPDigestAuth('vcu', 'rams'))
    #make request
    #return JSON payload with time request took
    return '<h1> hello </h1>'

if __name__ == "__main__":
    app.run(debug=True)



