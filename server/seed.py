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
            venue=fake.random_element(venues)
        )
        weddings.append(wedding)
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
            wedding=fake.random_element(weddings),
            host=fake.random_element(hosts)
        )
        invites.append(invite)
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
        db.session.add_all(weddings)
        db.session.add_all(hosts)
        db.session.commit()
        invites = create_invites(weddings, hosts)

        
        db.session.add_all(invites)
        db.session.commit()