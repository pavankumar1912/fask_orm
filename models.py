# Create models here
from app import db

class User_role(db.Model):
    role_id = db.Column(db.Integer,nullable=False,primary_key=True,unique= True)
    role_name = db.Column(db.String(100), nullable=True)
    employes = db.relationship('Employee',backref = 'user_role', lazy = 'dynamic')
    def __repr__(self):
        return (self.role_name)


class Employee(db.Model):
    employeeId = db.Column(db.Integer, primary_key=True)
    employeeName = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False, unique=True)
    joiningDate = db.Column(db.String,nullable = False)
    password = db.Column(db.String(100),nullable= False)
    role_id = db.Column(db.Integer,db.ForeignKey('user_role.role_id'))
    gender = db.Column(db.String(100),nullable= False)
    
    def __repr__(self):
        return self.employeeName



    

    