from flask_sqlalchemy import SQLAlchemy
from app import db

class store(db.Model):
    __tablename__= 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    content = db.Column(db.String(255))

    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def __ref__(self):
        return self.id