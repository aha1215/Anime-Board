<h1>Anime Image Board</h1>

<strong>Description:</strong> A board where users can discuss their favorite anime.

<strong>Team Members:</strong> Andrew Brown, Emma Larson, Scott Coonis, Alfredo Hernandez

<strong>Class:</strong> CST 205 Multimedia Design and Programming

<strong>Date:</strong> 5/17/2021

<strong>GitHub Repo Link:</strong> https://github.com/ahernandez1215/anime_board.git

-------------------------
<h2>How to Run</h2>
Install flask sqlalchemy module while your virtual environment is running: python -m pip install flask-sqlalchemy

For Windows: Start a virtual environment using power shell and change directory to anime_board directory.
Run the following....

$env:FLASK_APP = "index.py"

$env:FLASK_DEBUG = "1"

flask run

Then open your browser and go to http://127.0.0.1:5000/

-------------------------

Future Work:

- A character section that allows users to search by character

- A custom homepage for logged-in users

- More features for logged-in users in general like 'favorites' and 'view post history'
