import os
from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "inventory.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
api = Api(app)
db = SQLAlchemy(app)


import models
from models import *


@app.route('/')
#@login_required
def hello():
    a = User_role.query.all()
    print(a)
    return '<h1>Welcome to Inventory Application</h1>'
@app.route("/user", methods=["GET"])
def get_user():
    print('2nd call')
    all_users = User_role.query.all()
    print(all_users)
    #result = users_schema.dump(all_users)
    return "Hello World"

@app.route("/user", methods=["POST"])
def add_user():
    print("post call")
    rid = request.json['username']
    rname = request.json['email']
    
    new_user = User_role(role_id =rid,role_name=rname)

    db.session.add(new_user)
    db.session.commit()

    return "post call success"


if __name__ == '__main__':

    app.run()
