import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

data = []

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/delete', methods=['GET'])
def delete_record():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/find', methods=['GET'])
def find_record():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/add', methods=['GET'])
def add_record():
    return "<h1>THIS IS A TEST</h1>"

@app.route('/status', methods=['GET'])
def get_record_status():
    print(request.args, 'this is the data')
    print(request)
    return str(data)

app.run()