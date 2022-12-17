import sys 
sys.path.append('code')
sys.path.append("models")
from db import db
from models.hospitalsModel import HospitalModel
from models.userModel import UserModel

class AreaModel(db.Model):
    __tablename__='areas'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    
    hospitals=db.relationship('HospitalModel',lazy='dynamic')
    users=db.relationship("UserModel",lazy='dynamic')
    
    def __init__(self,name):
        self.name=name
        
    @classmethod
    def find_by_name(self,name):
        return AreaModel.query.filter_by(name=name).first()
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def json(self):
        return{"id":self.id,"name":self.name,"hospitals":[hospital.json() for hospital in self.hospitals.all()],"users":[user.json()for user in self.users.all()]}
    
    