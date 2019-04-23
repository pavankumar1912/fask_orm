import os

from flask import Flask



app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "mysql://root:root@localhost/sample"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)
migrate = Migrate(app,db)


class Users(db.Model):
    
    name = db.Column(db.String(50), primary_key=True)
    useremail = db.Column(db.String(100))
    password = db.Column(db.String(150))
    role_id = db.Column(db.Integer)
   
  
