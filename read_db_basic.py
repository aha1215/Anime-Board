""" read from a SQLite database and return data """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# the name of the database; add path if necessary
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

#routes

@app.route('/login')
def login_page():
    try:
        users = User.query
        user_text = '<ul>'
        for user in users:
            user_text += '<li>' + user.username + ', ' + user.password + ', '  + '</li>'
        user_text += '</ul>'
        return user_text
    except Exception as e:
        # holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)