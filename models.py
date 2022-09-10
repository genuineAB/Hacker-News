from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)

class News(db.Model):
    __tablename__ = 'news'
    
    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, nullable=True)
    type = db.Column(db.String(250), nullable=False)
    by = db.Column(db.String(100), nullable=True)
    time = db.Column(db.Integer, nullable=True)
    dead = db.Column(db.Boolean, nullable=True)
    kids = db.Column(db.JSON, nullable=False)
    parent = db.Column(db.Integer, nullable=True)
    text = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    title = db.Column(db.String, nullable=True)
    parts = db.Column(db.JSON, nullable=True)
    descendants = db.Column(db.Integer, nullable=True)
    score = db.Column(db.Integer, nullable=True)
    