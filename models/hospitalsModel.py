import sys
sys.path.append('code')
from db import db

class HospitalModel(db.Model):
    __tablename__="Hospitals"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    
    area=db.Column(db.String(100),db.ForeignKey('areas.name'))
    db.relationship('AreaModel')
    
    def __init__(self,name,area):
        self.name=name
        self.area=area
        
    @classmethod
    def find_by_name(self,name):
        return HospitalModel.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_area(self,area):
        hospitals_list=[]
        hospitals=HospitalModel.query.filter_by(area=area)
        for hospital in hospitals:
            hospitals_list.append(hospital.json())
        return {"hospitals":hospitals_list}
        
    def json(self):
        return {"hospital id":self.id,"hospital name":self.name,"area":self.area}
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod    
    def get_all_hospitals(self):
        return HospitalModel.query.all()