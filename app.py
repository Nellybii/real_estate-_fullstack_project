from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from flask_cors import CORS
from models import db, User
from resources.location import Location
from resources.property import PropertyResource
from resources.user import Signup, Login

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['BUNDLE_ERRORS']=True
app.config['SQLALCHEMY_ECHO']=True
app.config["JWT_SECRET_KEY"]="super-secret"
CORS(app)
migrate=Migrate(app,db)

db.init_app(app)
api=Api(app)
bcrypt=Bcrypt(app)
jwt=JWTManager(app)

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none().to_json()

 
class AppResource(Resource):
    def get(self):
        return "Welcome to the real Estate"


api.add_resource(Location, '/locations', '/locations/<int:id>')
api.add_resource(PropertyResource, '/property', '/property/<int:id>')
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')






