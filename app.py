from flask import Flask, render_template, session, redirect
from functools import wraps

# import username and password in file "config.py"
import config

# import mongodb
import pymongo

app = Flask(__name__)
# Flask requires a secret key for sessions, this can be anything
# I have stored mine in the config.py file
app.secret_key = config.secret_key

# Connect the database. This is the URI from mongodb.com > clusters > connect > connect your application
client = pymongo.MongoClient(f'mongodb+srv://{config.db_username}:{config.db_password}@cluster0.fzgne.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = client.user_login_system

# Decorators
# We don't want to be able to access /dashboard unless an account has been made
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if('logged_in' in session):
            # Allowed through (continue to def dashboard)
            return f(*args, **kwargs)
        else:
            # Must make an account
            return redirect('/')

    return wrap

# import routes.py
# note this must be below app declaration or it will cause a circular import
from user import routes


# The home directory
@app.route('/')
def home():
    return render_template('home.html')

# The dashboard directory
@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')
