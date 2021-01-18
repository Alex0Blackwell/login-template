from flask import Flask, render_template

# import username and password in file "config.py"
import config

# import mongodb
import pymongo

app = Flask(__name__)

# Connect the database. This is the URI from mongodb.com > clusters > connect > connect your application
client = pymongo.MongoClient(f'mongodb+srv://{config.db_username}:{config.db_password}@cluster0.fzgne.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = client.user_login_system

# import routes.py
# note this must be below app declaration or it will cause a circular import
from user import routes


# The home directory
@app.route('/')
def home():
    return render_template('home.html')

# The dashboard directory
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
