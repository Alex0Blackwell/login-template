from flask import Flask

# get the app variable from app.py so we can do @app.route
from app import app
# import the user class from models.py
from user.models import User


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()
