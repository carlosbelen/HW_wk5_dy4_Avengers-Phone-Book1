from flask import Flask

# import the Config Object
from config import Config

#import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

#import the Migrate Object
from flask_migrate import Migrate

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

from avengers import routes, models