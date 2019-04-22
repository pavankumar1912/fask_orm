from flask import Flask
from flask_restful import Api
from modles import *
from routes.auth import *


api = Api(app)

api.add_resource(AddUser, '/user', endpoint = 'AddUser')
api.add_resource(Userlogin,'/userlogin', endpoint = 'Userlogin')
api.add_resource(DeleteUser,'/delete', endpoint = 'DeleteUser')
if __name__ == "__main__":
    app.run()