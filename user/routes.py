from flask import Flask

# get the app variable from app.py so we can do @app.route
from app import app
# import the user class from models.py
from user.models import User


# The signup method that takes in data as a post request
@app.route('/user/signup', methods=['POST'])
def signup():
    # Instatiate and invoke
    return User().signup()


# The login method of user/models.py > User class
# Take in data as a post request
@app.route('/user/login', methods=['POST'])
def login():
    # Instatiate and invoke
    return User().login()

# The signout method of user/models.py > User class
@app.route('/user/signout')
def signout():
    # Instatiate and invoke
    return User().signout()
