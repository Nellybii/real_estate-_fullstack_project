from flask_restful import Resource, fields, reqparse, marshal_with
from flask_jwt_extended import jwt_required, current_user
from models import Property, db
from .location import resource_fields as location_fields

resource_fields={
    'id': fields.Integer,
    'name':fields.String,
    'description':fields.String,
    'listing_price': fields.Integer,
    'type_of_property': fields.String,
    "location":fields.Nested(location_fields),
    'is_active':fields.Boolean,
    'created_at':fields.DateTime,
    'updated_at':fields.DateTime
}
class PropertyResource(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('name', help='Name is required', required=True)
    parser.add_argument('description', help='Description is required', required=True)
    parser.add_argument('listing_price', help='Listing price is required', required=True)
    parser.add_argument('location_id', help='Location is required', required=True)
    parser.add_argument('type_of_property', help='Type of property is required', required=True)
    parser.add_argument('is_active', help='Is_active of property is required', required=True)
    # parser.add_argument('created_at', help='Created_at of property is required', required=True)
    # parser.add_argument('updated_at', help='Updated_at  of property is required', required=True)


    @marshal_with(resource_fields)
    def get(self, id= None):
        if id:
            property= Property.query.filter_by(id=id).first()
            if property is not None:
                return property
            else:
                properties = Property.query.all()
                return properties
            
    @jwt_required()
    def post(self):
        if current_user['role'] != 'admin':
            return { "message":"Unauthorized request"}
        data=PropertyResource.parser.parse_args()
        property=Property(**data)
        try:
            db.session.add(property)
            db.session.commit()
            return {"message":"property created successfully", "status": "success"}
        except:
            return {"message":"creation unsuccessful", "status": "fail"}
        

    def patch(self):
        pass