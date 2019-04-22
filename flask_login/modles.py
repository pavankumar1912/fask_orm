import os

from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "mysql://root:root@localhost/req"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "Users"
    name = db.Column(db.String(50), primary_key=True)
    useremail = db.Column(db.String(100))
    password = db.Column(db.String(150))
    role_id = db.Column(db.Integer)

