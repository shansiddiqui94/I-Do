from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData, DateTime
from sqlalchemy.orm import validates

from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from config import db


# Models go here!
class Venue(db.Model, SerializerMixin):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    weddings = db.relationship('Wedding', back_populates='venue') 


    def __repr__(self):
        return f"<Restaurant {self.name}>"
    

class Wedding(db.Model, SerializerMixin):
    __tablename__ = 'weddings'

    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String)
    entertainment = db.Column(db.String)
    date = db.Column(db.DateTime)
    venue_id=db.Column(db.Integer, db.ForeignKey('venues.id'))

    invites = db.relationship('Invite', back_populates='wedding')
    venue = db.relationship('Venue', back_populates='weddings') #a venue can have muliple weddings. Wedding only has 1 venue

    serialize_rules = ['-invites.wedding']

    def __repr__(self):
        return f"<Wedding {self.food}, {self.entertainment}, {self.date}>"
    
#the Host is the organizer or the user that signs up on the site
#to create a wedding.
class Host(db.Model, SerializerMixin):
    __tablename__ = 'hosts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    invites = db.relationship('Invite', back_populates='host', cascade='all, delete-orphan')
    #cascade delete deletes everything associated with a host
    #if a host is deleted. A wedding cannot exist without a host, and invite. However, a host can exist without 
    #wedding and invite. 

    serialize_rules = ['-invites.host']

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

    host = db.relationship('Host', back_populates='invites')
    wedding = db.relationship('Wedding', back_populates='invites')

    serialize_rules = ['-host.invites', '-wedding.invites']

    def __repr__(self):
        return f"<Restaurant {self.guest_name}>"

