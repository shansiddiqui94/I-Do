#!/usr/bin/env python3
# Standard library imports

# Remote library imports
from flask import Flask, make_response, request
from flask_migrate import Migrate

# Local imports
from config import app, db

# Add your model imports
from models import Venue, Wedding, Host, Invite


# Views go here!

# Venue Routes
@app.route('/venues', methods=['GET', 'POST'])
def venue_list():
    pass

@app.route('/venues/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def venue_detail(id):
    pass

# Wedding Routes
@app.route('/weddings', methods=['GET', 'POST'])
def wedding_list():
    pass

@app.route('/weddings/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def wedding_detail(id):
    pass

# Invite Routes
@app.route('/invites', methods=['GET', 'POST'])
def invite_list():
    pass

@app.route('/invites/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def invite_detail(id):
    pass

#Host routes TBD!!














if __name__ == '__main__':
    app.run(port=5555, debug=True)

    #crud for each of the tables 
    #Get req for all of them 
    #read request, and all of the data: 

    #Wedding creating 
        #selecting food
        # entertainment

    #invites:
    #post
    #patch/rsvp, pending 

    #5 - 10 venues seed in DB


    #Sending an Invite 