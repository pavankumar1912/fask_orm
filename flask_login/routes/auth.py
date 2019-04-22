from flask import Request,jsonify,request
import json
from flask_restful import Resource
from modles import *
import hashlib
from uuid import uuid4
from flask_sqlalchemy import sqlalchemy

class AddUser(Resource):
    def get(self):
        data = Users.query.all()
        cols = ['name','useremail','role_id']
        result = [{col: getattr(d, col) for col in cols} for d in data]
        return jsonify(result=result)
    def post(self):
        data = request.json
        cols = ['name','useremail','role_id']
        # verify = db.session.query(Users).filter(Users.useremail == data['email'])
        # result = [{col: getattr(d, col) for col in cols} for d in verify]
        # info = Users(name = data['name'], useremail = data['email'],password = data['password'], role_id = data['role_id'])
        # db.session.add(info)
        # db.session.commit()
        try:
            password = data['password']
            salt = uuid4().hex
            cipher = hashlib.sha256((password+salt).encode('utf-8')).hexdigest()
            pass_db = salt+cipher
            info = Users(name = data['name'], useremail = data['email'],password = pass_db, role_id = data['role_id'])
            db.session.add(info)
            db.session.commit()
            return 'sucess'
        except sqlalchemy.exc.IntegrityError:
            return 'user aleady exists'



class Userlogin(Resource):
    def post(self):
        data = request.json
        #cols = ['name','useremail','password', 'role_id']
        #result = db.session.query(Users).filter(Users.useremail == data['email'])
        #print(result)
        result = Users.query.filter_by(useremail = data['email']).first()
        #print(result.password[0:32])
        # result = [{col: getattr(d, col) for col in cols} for d in result]
        if result == None:
             return 'invalid user'
        else:
            frent_password = data['password']
            password = result.password
            salt = password[0:32]
            cipher_db = password[32:]
            cipher_front = hashlib.sha256((frent_password + salt).encode('utf-8')).hexdigest()
            if cipher_front == cipher_db:
                status = 'sucessfully logedin'
                return jsonify({"status":status,"result": {'name':result.name}})
            else:
                return 'bad password'

       # return 'result'

class DeleteUser(Resource):
    def delete(self):
        data = request.json
        Users.query.filter_by(useremail = data['email']).delete()
        print(data['email'])
        db.session.commit()
        return 'sucefully deleted'


class UpdateUser(Resource):
    def put(self):
        data = request.json
        Users.query.filter_by(useremail = data['email']).updata({})
