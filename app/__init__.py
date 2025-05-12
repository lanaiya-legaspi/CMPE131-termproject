#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#create flask object
myapp_obj = Flask(__name__)

#locate local file path of repository
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLAlchemy required setup
myapp_obj.config.from_mapping(
	SECRET_KEY = 'you-will-never-guess',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
	SQLALCHEMY_TRACK_MODIFICATIONS = False
)

#create database object
db = SQLAlchemy(myapp_obj)

#imports for routing, db connections, and web forms
from app import routes, models, forms
