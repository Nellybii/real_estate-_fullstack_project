from flask_restful import Resource, reqparse, fields, marshal_with
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from models import User, db

user_fields={
       "id":fields.Integer,
       "first_name": fields.String,
        "last_name":fields.String,
        "phone": fields.String,
        "email": fields.String,
        "role":fields.String,
        "created_at":fields.DateTime,
        "updated_at":fields.DateTime,
}
response_field={
    "message":fields.String,
    "status":fields.String,
    "user":fields.Nested(user_fields)
}


# response_field["user"]={ }
# response_field["user"]["id"]=fields.Integer

class Signup(Resource):
    parser= reqparse.RequestParser()
    parser.add_argument('first_name', required= True, help= "Firstname is required")
    parser.add_argument('last_name', required= True, help= "Lastname is required")
    parser.add_argument('phone', required= True, help= "Phone is required")
    parser.add_argument('email', required= True, help= "Email is required")
    # parser.add_argument('role', required= True, help= "Role is required")
    parser.add_argument('password', required= True, help= "Password is required")
    # parser.add_argument('created_at', required= True, help= "Created_at is required")
    # parser.add_argument('updated_at', required= True, help= "Updated_at is required")

    @marshal_with(response_field)
    def post(self):
        data=Signup.parser.parse_args()
        data['password']=generate_password_hash(data['password'])
        data['role']='member'
        user= User(**data)

        email=User.query.filter_by(email=data['email']).one_or_none()
        if email:
            return {"message":"Email already exist", "status":"fail"}, 400
        
        phone=User.query.filter_by(phone=data['phone']).one_or_none()
        if phone:
            return {"message":"Phone already exist", "status":"fail"}, 400
        
        try:
            db.session.add(user)
            db.session. commit()
            db.session.refresh(user)
            user_json=user.to_json()
            access_token=create_access_token(identity=user_json["id"])
            refresh_token=create_refresh_token(identity=user_json["id"])

            return {'message':'acount created succeessfully', 'status':'success',  "access_token": access_token, "refresh_token": refresh_token ,"user":user_json}
        
        except:
            return {"message":"unable to create account", "status":"fail" }

class Login(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('email', required= True, help= "Email is required")
    parser.add_argument('password', required= True, help= "Password is required")

    def post(self):
        data=Login.parser.parse_args()

        user =User.query.filter_by(email= data['email']).first()

        if user:
            is_password_correct = user.check_password(data['password'])

            if is_password_correct:
                user_json=user.to_json()
                access_token=create_access_token(identity=user_json["id"])
                refresh_token=create_refresh_token(identity=user_json["id"])
                return {"message": "login successful", "status":"success", "access_token": access_token, "refresh_token": refresh_token, "user":user_json}, 200
            
            else:
               return {"message": "invalid email/password", "status":"fail"}, 403
        else:
            return {"message": "invalid email/password", "status":"fail"}, 403
        

