import os
import json
from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import requests
from requests.auth import HTTPDigestAuth as sampleAuth


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
auth = HTTPDigestAuth()

users = {
    "vcu": "rams"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/ping', methods=['GET'])
@auth.login_required()
def ping():
    url = 'https://mccullochme-pong.herokuapp.com/pong'
    request = requests.get(url, auth=sampleAuth('vcu', 'rams'))
    time = request.elapsed.total_seconds()
    t = jsonify(pingpong_t=(time))
    return t.json, 201


if __name__ == "__main__":
    app.run(debug=True)



