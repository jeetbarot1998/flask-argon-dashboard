# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app         import db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


class User(UserMixin, db.Model):

    id       = db.Column(db.Integer,     primary_key=True)
    user     = db.Column(db.String(64),  unique = True)
    email    = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(500))

    def __init__(self, user, email, password):
        self.user       = user
        self.password   = password
        self.email      = email

    def __repr__(self):
        return '<User %r - %s>' % (self.id) % (self.email)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 

class productin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(75), nullable=False)
    specification = db.Column(db.String(75), nullable=False)
    category  = db.Column(db.String(75), nullable=False)
    price =db.Column(db.String(75), nullable=False)
    
    def __init__(self, specification, productname, category, price):
        self.productname       = productname
        self.specification   = specification
        self.category     = category
        self.price = price 
    
    def __repr__(self):
        # return f'<productin : {self.poductname}'
        return '<ID >' % (self.id) % (self.productname) % (self.category) % (self.price)

    def saved(self):
 
        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 
