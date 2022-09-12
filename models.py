import os
from sqlalchemy import Column, String, Integer, Boolean, JSON
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# database_name = 'hacker_news'
database_path = 'postgresql://postgres:12345@localhost:5432/hacker_news'


db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all()

class News(db.Model):
    __tablename__ = 'news'
    
    id = Column(Integer, primary_key=True)
    deleted = Column(Boolean, nullable=True)
    type = Column(String(250), nullable=False)
    by = Column(String(100), nullable=True)
    time = Column(Integer, nullable=True)
    dead = Column(Boolean, nullable=True)
    kids = Column(JSON, nullable=True)
    parent = Column(Integer, nullable=True)
    text = Column(String, nullable=True)
    url = Column(String, nullable=True)
    title = Column(String, nullable=True)
    parts = Column(JSON, nullable=True)
    descendants = Column(Integer, nullable=True)
    score = Column(Integer, nullable=True)
    
    def __init__(self, id, deleted, by, time, dead, kids, parent, text, url, type, title, parts, descendants, score):
        self.id = id
        self.deleted = deleted
        self.type = type
        self.by = by
        self.time = time
        self.dead = dead
        self.kids = kids
        self.parent = parent
        self.text = text
        self.url = url
        self.title = title
        self.parts = parts
        self.descendants = descendants
        self.score = score
        

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def serialize(self):
        return {
            "id": self.id,
            "deleted": self.deleted,
            "type": self.type,
            "by": self.by,
            "time": self.time,
            "dead": self.dead,
            "kids": self.kids,
            "parent": self.parent,
            "text": self.text,
            "url": self.url,
            "title": self.title,
            "parts": self.parts,
            "descendants": self.descendants,
            "score": self.score
            }
        
    def __repr__(self):
        return f"<statement>"

    