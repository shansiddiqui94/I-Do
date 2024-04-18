#!/usr/bin/env python3
# Standard library imports

# Remote library imports
from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_cors import CORS

# Local imports
from config import app, db

# Add your model imports
from models import Venue, Wedding, Host, Invite

# Views go here!

# Venue Routes *
@app.route('/venues')
def venue_list():
    venues = Venue.query.all()
    return [venue.to_dict(rules=['-weddings']) for venue in venues], 200


@app.route('/venues/<int:id>', methods=['GET', 'DELETE'])
def venue_detail(id):
    venue_detail = Venue.query.filter(Venue.id == id).first()
    if venue_detail is None:
        return 'venue not found', 404

    if request.method == 'GET':
        return venue_detail.to_dict(rules=['-weddings']), 200
        
    elif request.method == "DELETE":
        db.session.delete(venue_detail)
        db.session.commit()

        return {}, 204
    
    
 # Wedding Routes
@app.route('/weddings', methods=['GET'])
def wedding_list():
    weddings = Wedding.query.all()
    request.method == 'GET'
    return [wedding.to_dict(rules=['-venue', '-invites']) for wedding in weddings], 200
   

@app.route('/weddings/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def wedding_detail(id):
    wedding_detail = Wedding.query.get(id)
    if not wedding_detail: #Error handling
        return {}, 404
    
    if request.method == 'GET':
        return wedding_detail.to_dict(), 200
    
    elif request.method == 'PATCH':
        json_data = request.get_json()
        for key, value in json_data.items():
            setattr(wedding_detail, key, value)
        db.session.commit()
        return wedding_detail.to_dict(), 200
    
    elif request.method == "DELETE":
        db.session.delete(wedding_detail)
        db.session.commit()
        return {}, 204


# Invite Routes
@app.route('/invites', methods=['GET', 'POST'])
def invite_list():
    if invite_list is None:
        return 'Guest not found', 404
    invites=Invite.query.all()
    if request.method == 'GET':
        return [invite.to_dict(rules=['-wedding', '-host']) for invite in invites], 200
    
    elif request.method == 'POST':
        json_data = request.get_json()
        new_invite = Invite(**json_data)
        db.session.add(new_invite)
        db.session.commit()
        return new_invite.to_dict(), 201

@app.route('/invites/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def invite_detail(id):
    invite_detail = Invite.query.get(id)
    if not invite_detail:
        return "Guest Not Found", 404
    
    if request.method == 'GET':
        return invite_detail.to_dict(), 200
    
    elif request.method == 'PATCH':
        json_data = request.get_json()
        for key, value in json_data.items():
            setattr(invite_detail, key, value)
        db.session.commit()
        return invite_detail.to_dict(), 200
    
    elif request.method == "DELETE":
        db.session.delete(invite_detail)
        db.session.commit()
        return {}, 204



if __name__ == '__main__':
    app.run(port=5555, debug=True)

#Host routes TBD!!
# Authentication Routes:
# POST /register: Register a new user.
# POST /login: Log in an existing user.
# POST /logout: Log out the current user.
# GET /user: Get information about the current user (optional, for profile viewing).


# Host Routes (Protected by Authentication):
# GET /hosts: Retrieve all hosts (potentially for admin purposes).
# GET /hosts/{id}: Retrieve a specific host by ID.
# POST /hosts: Create a new host (might be automatically created upon registration).
# PATCH /hosts/{id}: Update an existing host by ID.
# DELETE /hosts/{id}: Delete a host by ID.

