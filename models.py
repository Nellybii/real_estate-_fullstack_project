from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash

#initialize db
db=SQLAlchemy()

#models
class User(db.Model):
    __tablename__= "users"

    id= db.Column(db.Integer, primary_key= True)
    first_name=db.Column(db.Text, nullable= False)
    last_name=db.Column(db.Text, nullable= False)
    phone=db.Column(db.String, nullable= False, unique=True)
    email=db.Column(db.String, nullable= False, unique=True)
    role=db.Column(db.Text, nullable= False)
    password=db.Column(db.String, nullable= False)
    created_at=db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at= db.Column(db.TIMESTAMP, onupdate=db.func.now())
    # deleted_at= db.Column(db.TIMESTAMP)

    def check_password(self, plain_password):
        return check_password_hash(self.password, plain_password)
    
    def to_json(self):
        return {"id":self.id, "role":self.role}

class LocationModel(db.Model):
    __tablename__="locations"

    id= db.Column(db.Integer, primary_key= True)
    name=db.Column(db.Text, nullable= False)
    created_at=db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at= db.Column(db.TIMESTAMP, onupdate=db.func.now())

class Property(db.Model):
    __tablename__ = "properties"

    id= db.Column(db.Integer, primary_key= True)
    name=db.Column(db.Text, nullable= False)
    description=db.Column(db.String, nullable= False)
    listing_price= db.Column(db.Integer, nullable= False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    type_of_property=db.Column(db.Text, nullable= False)
    is_active= db.Column(db.Boolean, default=True)
    created_at=db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at= db.Column(db.TIMESTAMP, onupdate=db.func.now())

    location= db.relationship("LocationModel", backref="properties")


