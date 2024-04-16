#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Venue, Host, Wedding, Invite

# Function to create dummy venues
def create_venues():
    venues = []
    for _ in range(10):
        venue = Venue(
            name=fake.company(),
            address=fake.address()
        )
        venues.append(venue)
    return venues

# Function to create dummy weddings associated with venues
def create_weddings(venues):
    weddings = []
    for _ in range(5):
        wedding = Wedding(
            food=fake.word(),
            entertainment=fake.word(),
            date=fake.date_time_this_year(),
        )
        weddings.append(wedding)
        # Add the wedding to the session before associating it with a venue
        db.session.add(wedding)
        # Associate the wedding with a random venue
        venue = fake.random_element(venues)
        wedding.venue = venue
        # Ensure the venue is added to the session if it's not already there
        if venue not in db.session:
            db.session.add(venue)
    return weddings

# Function to create dummy hosts
def create_hosts():
    hosts = []
    for _ in range(5):
        host = Host(
            name=fake.name()
        )
        hosts.append(host)
    return hosts

# Function to create dummy invites associated with weddings and hosts
def create_invites(weddings, hosts):
    invites = []
    for _ in range(20):
        invite = Invite(
            guest_name=fake.name(),
        )
        invites.append(invite)
        # Add the invite to the session before associating it with a wedding and host
        db.session.add(invite)
        # Associate the invite with a random wedding and host
        invite.wedding = fake.random_element(weddings)
        invite.host = fake.random_element(hosts)
    return invites

# Main function to seed the database
if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        venues = create_venues(); db.session.add_all(venues); db.session.commit()
        weddings = create_weddings(venues)
        hosts = create_hosts()
        db.session.add_all(hosts)
        db.session.commit()
        invites = create_invites(weddings, hosts)
        db.session.add_all(invites)
        db.session.commit()