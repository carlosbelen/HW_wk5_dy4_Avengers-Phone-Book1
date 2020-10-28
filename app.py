from avengers import app, routes 

 # '__name__' is this file 'app.py' is the main file (it's not being imported anywhere else), run this
if __name__ == '__main__':
    app.run(debug = True)