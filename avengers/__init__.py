from flask import Flask

# import the Config Object
from config import Config

#import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

#import the Migrate Object
from flask_migrate import Migrate

# Import for the Flask Login Module - rom ONLINE Documentation
from flask_login import LoginManager

app = Flask(__name__) 
# name is = avengers. So anything that happens inside of that foloder 
# is now linked to this file.
# package based and module based

app.config.from_object(Config)
# the above completes the Config cycle for our Flask App
# And Give access to our Database (When we have one)
# Along with our Secret key
 
# Init our database (db) - information will now be passed to db
db = SQLAlchemy(app)

# Init the migrator - then its migrated
migrate = Migrate(app,db)

# Login Config - Init for the LoginManager
# varies a little from online documentation because Joel opted to condense it and include 'app' in the ()
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Specify what page to load for Non-Authenticated users

from avengers import routes, models