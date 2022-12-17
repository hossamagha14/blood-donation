import sys
sys.path.append('models')
from flask_restful import Resource
from models.hospitalsModel import HospitalModel


class AllHospitals(Resource):
    def get(self):
        hospitals= HospitalModel.get_all_hospitals()
        allHospitals=[hospital.json() for hospital in hospitals]
        return {"hospitals":allHospitals}