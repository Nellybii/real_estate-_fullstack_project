from flask_restful import Resource, fields, marshal_with, reqparse
from flask_jwt_extended import jwt_required, current_user
from models import LocationModel, db

resource_fields={
    'id': fields.Integer,
    'name': fields.String,
    'created_at': fields.DateTime,
    'updated-at': fields.DateTime
    }
    
class Location(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('name', help= "Name is required", required = True)

    @marshal_with(resource_fields)
    def get(self, id=None):
        if id:
            location= LocationModel.query.filter_by(id=id).first()
            if id is not None:
                return location
        else: 
            locations = LocationModel.query.all()
            return locations
        
    @jwt_required
    def post(self):
        if current_user['role'] != 'admin':
            return { "message":"Unauthorized request"}
        data=Location.parser.parse_args()
        location = LocationModel(**data)
        try:
           db.session.add(location)
           db.session.commit()
           return {"message":"location created successfully", "status":"success"}
        except:
            return {"message":"location creation unsuccessfully", "status":"fail"}

       
    
    
