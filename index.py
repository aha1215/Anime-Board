'''

Flask app engine for Anime Board project.

'''

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, url_for, redirect, flash, \
session, abort
from flask_bootstrap import Bootstrap
from PIL import Image
import random, requests, json
from pprint import pprint

app = Flask(__name__)
bootstrap = Bootstrap(app)

'''

ROUTES

TODO on all routes:
    - Check if user is logged in. (Authentication check) Send bool with render_template so
        login/logout buttons show correctly.
    
'''


""" read from a SQLite database and return data """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'configure strong secret key here'
# the name of the database
db_name = 'users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)
# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class User(db.Model):
    __tablename__ = 'users'
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    birthdate = db.Column(db.Integer)

    def __repr__(self):
        return '' % self.username


#Root route
@app.route('/')
def index():
    return render_template('index.html')

#Search Results route
@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['keywords']
        payload = {
            'q': search_term
        }
        endpoint = 'https://api.jikan.moe/v3/search/anime'

        r = requests.get(endpoint, params=payload)
        data = r.json()
        
        my_list = []

        '''
        for i in range(len(data)):
            my_list.append(data['results'][i]['image_url']) #List of images matching search_term
        '''
        my_list = data['results']

        return render_template('search_results.html', images=my_list, keywords=search_term)
    
    return render_template('search_results.html')

#Image page route
@app.route('/img/<img_id>')
def imgpage(img_id):
    #Get all info about img
    #NOTE: change the route depending on how the API works -Emma
    #Get all comments about img
    #Send img info and comment info with render_template
    return render_template('imgpage.html')

#Comment page route: 
#TODO: This shouldn't run unless user is logged-in, redirect to login page instead.
@app.route('/img/<img_id>/comment')
def comment():
    return render_template('comments.html')
    

#Random image board route
@app.route('/random')
def random():
    #Use random number generator to get... however many. let's say 12 or 15 images.
    #Send images with render_template
    return render_template('random.html')

#New post POST route
#Referenced https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data
@app.route('/new/post', methods=['GET','POST'])
def create_post_post():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        #Store user id + postId + postTitle,
        return render_template('new_post.html', info=description, title=title)
    else:
        return render_template('new_post.html')



@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if not (username and password):
            flash("Username or Password cannot be empty.")
            return redirect(url_for('login'))
        else:
            username = username.strip()
            password = password.strip()

        user = User.query.filter_by(username=username).first()

        if user and (user.password == password):
            session[username] = True
            return redirect(url_for("user_home", username=username))
        else:
            flash("Invalid username or password.")

    return render_template("login.html")

@app.route("/user/<username>/")
def user_home(username):
    """
    Home page for validated users.
    """
    if not session.get(username):
        abort(401)
  
    return render_template("user_home.html", username=username)

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
