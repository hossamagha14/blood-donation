import sys
sys.path.append("models")
from flask_restful import Resource,reqparse
from models.userModel import UserModel

class User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("username",type=str,required=True,help="please enter your username")
    parser.add_argument("password",type=str,required=True,help="please enter your password")
    parser.add_argument("blood_type",type=str,required=True,help="please enter your blood type")
    parser.add_argument("user_type",type=str,required=True,help="please enter your weither you are blood donor or requester")
    parser.add_argument("area",type=str,required=True,help="please enter your area")
    
    get_parser=reqparse.RequestParser()
    get_parser.add_argument('username',type=str,required=True,help='please enter the username you want to search for')
    
    def get(self):
        data=User.get_parser.parse_args()
        user=UserModel.find_by_username(data['username'])
        if user:
            return user.json()
        else:
            return {"message":"user not found"}
        
        
    
    def post(self):
        data=User.parser.parse_args()
        user=UserModel.find_by_username(data['username'])
        if user:
            return {"message":"username already taken"}
        else:
            user=UserModel(**data)
            user.insert()
            return user.json()
        
    