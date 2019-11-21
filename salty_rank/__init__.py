from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Set application configuration key values
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///HRTopDown.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Instantiate database
db = SQLAlchemy(app)

from salty_rank import routes
