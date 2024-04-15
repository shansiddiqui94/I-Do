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
    if request.method == 'GET':
        all_venues = []
        for location in Venue.query.all():
            all_venues.append(location.to_dict())
        return all_venues, 200
    
    elif request.method == 'POST':
        json_data = request.get_json()
        new_venue = Venue()
        for key, value in json_data.items():
            setattr(new_venue, key, value)

        db.session.add(new_venue)
        db.session.commit()

        return new_venue.to_dict(), 201

@app.route('/venues/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def venue_detail(id):
    venue_detail = Venue.query.filter(Venue.id == id).first()
    if request.method == 'GET':
        return venue_detail.to_dict(), 200
    
    elif request.method == 'PATCH':
        json_data = request.get_json()
        if 'venue_id' in json_data:  #venue_id IS pointing at models.py
            venue_detail.venue_id = json_data.get('venue_id') # in this line I am accessing the venueId key in models

            db.session.add(venue_detail)
            db.session.commit()

            return venue_detail.to_dict(), 200
        
    elif request.method == "DELETE":
        db.session.delete(venue_detail)
        db.session.commit()

        return {}, 204
    
    
 # Wedding Routes
@app.route('/weddings', methods=['GET', 'POST'])
def wedding_list():
    if request.method == 'GET':
        all_weddings = [wedding.to_dict() for wedding in Wedding.query.all()]
        return all_weddings, 200
    
    elif request.method == 'POST':
        json_data = request.get_json() 
        new_wedding = Wedding(**json_data) #whats the asterik read up
        db.session.add(new_wedding)
        db.session.commit()
        return new_wedding.to_dict(), 201

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
    if request.method == 'GET':
        all_invites = [invite.to_dict() for invite in Invite.query.all()]
        return all_invites, 200
    
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
        return {}, 404
    
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

