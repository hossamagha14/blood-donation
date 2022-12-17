from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy()
db.init_app(app)