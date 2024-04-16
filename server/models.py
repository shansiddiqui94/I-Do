from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
# from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from config import db

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=convention))


# Models go here!
class Venue(db.Model, SerializerMixin):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer, default=0)
    venue_picture = db.Column(db.String)
    

    #relationship
    weddings = db.relationship('Wedding', back_populates='venue')#a venue can have multiple weddings. Wedding only has 1 venue

    def __repr__(self):
        return f"<Restaurant {self.name}>"
    

class Wedding(db.Model, SerializerMixin):
    __tablename__ = 'weddings'

    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String)
    entertainment = db.Column(db.String)
    date = db.Column(db.DateTime)
    venue_id=db.Column(db.Integer, db.ForeignKey('venue.id'))

    #relationship
    invites = db.relationship('Invite', back_populates='wedding')
    venue = db.relationship('Venue', back_populates='weddings') #a venue can have multiple weddings. Wedding only has 1 venue

    #serialization
    serialize_rules = ['-invites.wedding']

    def __repr__(self):
        return f"<Wedding {self.food}, {self.entertainment}, {self.date}>"
    
#the Host is the organizer or the user that signs up on the site
#to create a wedding or to be a guest.
class Host(db.Model, SerializerMixin):
    __tablename__ = 'hosts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)#can't be 2 hosts with same name

    #relationship
    invites = db.relationship('Invite', back_populates='host', cascade='all, delete-orphan')
    #cascade delete deletes everything associated with a host
    #if a host is deleted. A wedding cannot exist without a host, and invite. However, a host can exist without 
    #wedding and invite. 

    #serialization
    serialize_rules = ['-invites.host']

    #ensure value of name is not empty and no duplicate
    @validates('name')
    def validate_name(self, key, name):
        if len(name) == 0:
            raise ValueError('invalid name')
        
        host_name = db.session.query(Host.id).filter_by(name = name).first()
        if host_name is not None:
            raise ValueError('name must be unique')
        
        return name
        


    def __repr__(self):
        return f"<Restaurant {self.name}>"
    
#This table holds our many. A wedding can have many Hosts. A Host can have
#multiple weddings. These 2 tables are linked via invite.
class Invite(db.Model, SerializerMixin):
    __tablename__ = 'invites'

    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String, nullable=False)
    wedding_id = db.Column(db.Integer, db.ForeignKey('weddings.id'))
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'))

    #relationship
    host = db.relationship('Host', back_populates='invites')
    wedding = db.relationship('Wedding', back_populates='invites')

    #serialization
    serialize_rules = ['-host.invites', '-wedding.invites']

    def __repr__(self):
        return f"<Restaurant {self.guest_name}>"

