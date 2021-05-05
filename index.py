'''

Flask app engine for Anime Board project.

'''

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

'''

ROUTES

TODO on all routes:
    - Check if user is logged in. (Authentication check) Send bool with render_template so
        login/logout buttons show correctly.
    
'''

#Root route
@app.route('/')
def index():
    return render_template('index.html')

#Image page route
@app.route('/img/<img_id>')
def imgpage(img_id):
    #Get all info about img
    #NOTE: change the route depending on how the API works -Emma
    #Get all comments about img
    #Send img info and comment info with render_template
    return render_template('imgpage.html')

#Comment page route
#TODO: This shouldn't run unless user is logged-in, redirect to login page instead.
@app.route('/img/<img_id>/comment')
def comment():
    return render_template('newPost.html')
    

#Random image board route
@app.route('/random')
def random():
    #Use random number generator to get... however many. let's say 12 or 15 images.
    #Send images with render_template
    return render_template('random.html')

@app.route('/new/post')
def createPost():
    return render_template('newPost.html')

#Login route
@app.route('/login')
def login():
    return render_template('login.html')

#Logout route
@app.route('/logout')
def logout():
    #Reset login information (Unauthenticate)
    return render_template('index.html')

'''

FUNCTIONS

'''


if __name__ == "__main__":
    app.run(debug=False)
