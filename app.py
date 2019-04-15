import os
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "inventory.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
api = Api(app)
db = SQLAlchemy(app)
#from flask_sqlalchemy import SQLAlchemy

@app.route('/')
#@login_required
def hello():
	return '<h1>Welcome to Inventory Application</h1>'

if __name__ == '__main__':

    app.run()
