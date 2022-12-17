import sys
sys.path.append('code')
from db import db

class UserModel(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(50))
    blood_type=db.Column(db.String(5))
    user_type=db.Column(db.String(20))
    area=db.Column(db.String(80),db.ForeignKey('areas.name'))
    db.relationship('AreaModel')
    
    def __init__(self,username,password,blood_type,user_type,area):
        self.username=username
        self.password=password
        self.blood_type=blood_type
        self.user_type=user_type
        self.area=area
        
        
    @classmethod
    def find_by_username(self,username):
        return UserModel.query.filter_by(username=username).first()
       
    
    @classmethod
    def find_by_id(self,user_id):
        return UserModel.query.filter_by(id=user_id).first()
        
    
    def json(self):
        return {"user id":self.id,"username":self.username,"password":self.password,"blood type":self.blood_type,"user type":self.user_type,"area":self.area}
    
    def insert(self):
        db.session.add(self)
        db.session.commit()