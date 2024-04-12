from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates

from sqlalchemy_serializer import SerializerMixin

from config import db

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    })

db = SQLAlchemy(metadata=metadata)

# Models go here!

class Venue(db.Model, SerializerMixin):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    def __repr__(self):
        return f"<Restaurant {self.name}>"
    

class Wedding(db.Model, SerializerMixin):
    __tablename__ = 'weddings'

    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String)
    entertainment = db.Column(db.String)
    date = db.Column(db.integer)

    def __repr__(self):
        return f"<Wedding {self.food} {self.entertainment} {self.date}>"
    
class Host(db.Model, SerializerMixin):
    __tablename__ = 'hosts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"<Restaurant {self.name}>"
    
class Invite(db.Model, SerializerMixin):
    __tablename__ = 'invites'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"<Restaurant {self.name}>"




