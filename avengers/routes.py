# Import the app variable from the init
from avengers import app, db

# Import specific packages from flask
from flask import render_template,request,redirect,url_for

#Import Our Form(s)
from avengers.forms import UserInfoForm, LoginForm

# Import of our Model(s) for the Database
from avengers.models import User,Post, check_password_hash 

# Import for Flask Login funcitons - login_recheck_password_hashquired
#  login_user, current_user, logout_user
from flask_login import login_required,login_user,current_user,logout_user

# Default Home Route
# routes are the traffic cop telling people where to go
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods = ['GET', 'POST'])
# GET information then 
# POST send Information
def register():
    # Init our Form - INSTANTIATING HERE
    form = UserInfoForm()
    
    #now sending form information instead of just text (i.e. names)
    if request.method == 'POST' and form.validate():
        #Get Information from the form
        username = form.username.data
        phone = form.phone
        email = form.email.data
        password = form.password.data
        # print the data to the server that comes form the form 
        print(username,email,password)

        # Creation/Init of our User Class (aka Model)  -- INSTANTIATING HERE
        user = User(username,email,password)

        # Open a connection to the database
        db.session.add(user)

        # Commit all data to the database
        db.session.commit()

    return render_template('register.html', user_form = form)
     
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        # Saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        #check the password of the newly found user
        #and validate the password against the hash value
        #inside of the database
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            # TODO Redirected user
            return redirect(url_for('home'))
        else:
            # TODO Redirect User to login route
            return redirect(url_for('login'))
    return render_template('login.html', login_form = form)