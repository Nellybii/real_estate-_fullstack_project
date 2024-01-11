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
    created_at=db.Column(db.TIMESTAMP)


