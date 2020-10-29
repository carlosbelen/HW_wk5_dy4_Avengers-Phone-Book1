# first model that will go into database.  
# will use information from flask-sqlachemy Quickstart to get started
from avengers import app, db, login_manager

# Import all of the Werkzeug Security methods
from werkzeug.security import generate_password_hash, check_password_hash

#Import for DateTime Module (this comes from python)
from datetime import datetime

# Import for the Login Manager UserMixin
from flask_login import UserMixin

# The user class will have
# An id, username, email
# password, post

# Create the current user_manager using the user_loader function
# Which is decorator (used in this class to send info to the User Model)
# Specifically to the User's ID

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    # each of our usernames have to be unique and it cant be empty:
    username = db.Column(db.String(150), nullable = False, unique=True)
    phone = db.Column(db.String(15), nullable = False, unique=True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    # 'lazy' this is only loaded when "we need it" or reqquested
    post = db.relationship('Post', backref = 'author', lazy = True)

    def __init__(self,username,phone,email,password):
        self.username = username
        self.phone = phone
        self.email = email
        # this will start our encryption method:
        self.password = self.set_password(password)
    
    def set_password(self,password):
        """
            Grab the password that is passed into the method
            return the hashed verion of the passowrd
            which will be stored inside the database

        """
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    # The following is needed to see when things go into our database, or object gets created so we can than use it:
    def __repr__(self):
        return f'{self.username} has been created with the following email: {self.email}'

# Creation of the Post Model
# The Post model will have: id, title, content, date_created, user_id

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,title,content,user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'The title of the post is {self.title} \n and the content is {self.content}'