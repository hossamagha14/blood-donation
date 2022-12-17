import sys
sys.path.append('models')
from models.areaModel import AreaModel
from flask_restful import Resource,reqparse


class Area(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('name',type=str,required=True,help='please enter the are ayou are looking for')
    
    
    def get(self):
        data=Area.parser.parse_args()
        area=AreaModel.find_by_name(data['name'])
        if area:
            return area.json()
        else:
            return{"message":"area not found"}
    
    def post(self):
        data=Area.parser.parse_args()
        area=AreaModel.find_by_name(data['name'])
        if area:
            return {"message":"this area already exists"}
        else:
            area=AreaModel(data['name'])
            area.insert()
            return area.json()
        
            