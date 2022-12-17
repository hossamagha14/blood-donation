import sys
sys.path.append("models")
from models.hospitalsModel import HospitalModel
from flask_restful import Resource,reqparse

class Hospitals(Resource):
    get_parser=reqparse.RequestParser()
    get_parser.add_argument("name",type=str,required=True,help='please enter the hospital name')
    
    parser=reqparse.RequestParser()
    parser.add_argument("name",type=str,required=True,help='please enter the hospital name')
    parser.add_argument("area",type=str,required=True,help='please enter the hospital area')
    
    def get(self):
        data=Hospitals.get_parser.parse_args()
        hospital=HospitalModel.find_by_name(data['name'])
        if hospital:
            return hospital.json()
        else:
            return{"message":"hospital not found"}
            
    def post(self):
        data=Hospitals.parser.parse_args()
        hospital=HospitalModel.find_by_name(data['name'])
        if hospital:
            return{"message":"hospital with this name already exists"}
        else:
            hospital=HospitalModel(data['name'],data['area'])
            hospital.insert()
            return hospital.json()