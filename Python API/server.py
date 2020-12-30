import flask
from flask import request, jsonify, render_template


app = flask.Flask(__name__)
app.config["DEBUG"] = False

# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

products = {"Apple": 5, "Pear": 5, "Hand bag": 20, "Shoe":10, "Toothbrush": 5, "iphone": 100, "ipad": 70, "laptop": 200}
accounts = {}
credits = {}

EXISTING_CUSTOMER = '-1'
WRONG_CREDENTIAL = '-2'
SUCCESS = '0'
NO_PRODUCT_FOUND = '-3'

# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route("/")
def index():
    return render_template("index.html", suggestions = credits)

@app.route("/secret")
def index_info():
    return render_template("index.html", suggestions = accounts)

@app.route('/register', methods=['POST'])
def new_user():
    if accounts.get(request.form['username']) is None:
        accounts[request.form['username']] = request.form['password']
        credits[request.form['username']] = 0
        return SUCCESS
    return EXISTING_CUSTOMER

@app.route('/login', methods=['POST'])
def login():
    if accounts.get(request.form['username']) is None or accounts.get(request.form['username']) != request.form['password']:
        return WRONG_CREDENTIAL
    return SUCCESS

@app.route('/add_credit', methods=['POST'])
def add_credit():
    balance = credits.get(request.form['cookie'])
    balance += int(request.form['amount'])
    credits[request.form['cookie']] = balance
    return "Credit added, your balance is: " + str(balance)

@app.route('/profile', methods=['POST'])
def view_profile():
    return "You are signed in as " + request.form['cookie'] + " with credit balance of " + str(credits.get(request.form['cookie']))

@app.route('/buy', methods=['POST'])
def buy_product():
    if products.get(request.form['product']) is None:
        return "ERROR: Product not found"
    if products.get(request.form['product']) > credits.get(request.form['cookie']):
        return "ERROR: Insufficient funds"
    balance = credits.get(request.form['cookie'])
    balance -= products.get(request.form['product'])
    credits[request.form['cookie']] = balance
    return "Item purchased, your balance is: " + str(balance)

@app.route('/list', methods=['GET'])
def list_all_products():
    output = ''
    for element in products.keys():
        output += element + " : " + str(products.get(element)) + "\n"
    return output

app.run(host = '0.0.0.0')
