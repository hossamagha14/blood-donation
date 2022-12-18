import sys
sys.path.append("models")
sys.path.append("resource")
from db import app,db
from flask_restful import Api
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from resources.user import User
from resources.hospitals import Hospitals 
from resources.area import Area
from resources.allHospitals import AllHospitals

app.secret_key='jose'
api=Api(app)

@app.before_first_request
def create_tabele():
    db.create_all()

jwt=JWT(app,authenticate,identity)

api.add_resource(User,'/user')
api.add_resource(Hospitals,'/hospitals')
api.add_resource(Area,'/areas')
api.add_resource(AllHospitals,'/all hospitals')


app.run(port=5000)
    