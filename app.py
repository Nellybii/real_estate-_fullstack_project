from flask import Flask
from flask_migrate import Migrate
from models import db

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
migrate=Migrate(app,db)

db.init_app(app)

@app.route('/')
def index():
    return "My first Flask App"

