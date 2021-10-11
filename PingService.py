import os
import json
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
import requests
from requests.auth import HTTPDigestAuth


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/ping', methods=['GET'])
def ping():
    url = 'https://mccullochme-pong.herokuapp.com/pong'
    request = requests.get(url, auth=HTTPDigestAuth('vcu', 'rams'))
    time = request.elapsed.total_seconds()
    return render_template("timeReturn.html", time=time)


if __name__ == "__main__":
    app.run(debug=True)



