import os
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import flask_httpauth
from flask_httpauth import HTTPDigestAuth


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

auth = HTTPDigestAuth()

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/ping', methods=['GET'])
@auth.login_required()
def ping():
    url = 'https://mccullochme-pong.herokuapp.com/pong'
    request = requests.get(url, auth=HTTPDigestAuth('vcu', 'rams'))
    reply = request.jsonify()
    return '<h1> sent a request</h1>'

if __name__ == "__main__":
    app.run(debug=True)



