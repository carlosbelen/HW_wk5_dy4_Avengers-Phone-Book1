# Import the app variable from the init
from avengers import app

# Import specific packages from flask
from flask import render_template,request

#Import Our Form(s)
from avengers.forms import UserInfoForm

# Default Home Route
# routes are the traffic cop telling people where to go
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/test')
# def testRoute():
#     names = ['Robert','David', 'Bill', 'Jessy']
#     return render_template('test.html',list_names = names)

@app.route('/register', methods = ['GET', 'POST'])
# GET information then 
# POST send Information
def regisger():
    # Init our Form - INSTANTIATING HERE
    form = UserInfoForm()
    
    #now sending form information instead of just text (i.e. names)
    if request.method == 'POST' and form.validate():
        #Get Information from the form
        username = form.username
        phone = form.phone
        email = form.email.data
        password = form.password.data
        # print the data to the server that comes form the form 
        print(username,phone,email,password)

    return render_template('register.html', user_form = form)