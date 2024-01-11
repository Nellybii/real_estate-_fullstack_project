from flask_sqlalchemy import SQLAlchemy

#initialize db
db=SQLAlchemy()

#models
class User(db.Model):
    __tablename__= "users"

    id= db.Column(db.Integer, primary_key= True)
    first_name=db.Column(db.Text, nullable= False)
    last_name=db.Column(db.Text, nullable= False)
    phone=db.Column(db.String, nullable= False, unique=True)
    phone=db.Column(db.String, nullable= False, unique=True)
    role=db.Column(db.Text, nullable= False)
    password=db.Column(db.String, nullable= False)
    created_at=db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at= db.Column(db.TIMESTAMP, onupdate=db.func.now())
    # deleted_at= db.Column(db.TIMESTAMP)

class LocationModel(db.Model):
    __tablename__="locations"

    id= db.Column(db.Integer, primary_key= True)
    name=db.Column(db.Text, nullable= False)
    created_at=db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at= db.Column(db.TIMESTAMP, onupdate=db.func.now())

# class Property(db.model):
#     __tablename__ = "properties"

#     id= db.Column(db.Integer, primary_key= True)
#     name=db.Column(db.Text, nullable= False)
#     description=db.Column(db.String, nullable= False)
#     listing_price= db.Column(db.Integer, nullable= False)
#     location=db.Column(db.Text, nullable= False)
#     created_at=db.Column(db.TIMESTAMP, server_default=db.func.now())
#     updated_at= db.Column(db.TIMESTAMP, onupdate=db.func.now())


