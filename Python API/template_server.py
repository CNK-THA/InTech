import flask # import necessary libraries
from flask import request, jsonify, render_template

app = flask.Flask(__name__) # initialise the Flask library
app.config["DEBUG"] = True # This version is not our final yet

# These 3 dictionaries will simulate our database. In real implementation  MySQL or phpMyAdmin will be used.
products = {} # Products we have on offer
accounts = {} # dictionary mapping between username and password of the user
credits = {} # dictionary mapping between username and account's credit (money) of the user


@app.route('/register', methods=['POST'])
def new_user():
    pass # remove this!
    # Code for registering new users goes here

@app.route('/login', methods=['POST'])
def login():
    pass # remove this!
    # code for logging user in goes here


# Create a function (like the 2 above) for each of these options:

# code for adding credit to account goes here

# code for printing profile information (username and how many credits we have) goes here

# code for buying an item goes here

# code for listing out all products goes here

app.run() # run the program
