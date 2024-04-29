from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    verified_email = db.Column(db.Boolean, default=False, nullable=False)
    address = db.Column(db.String(150))
    
    def __repr__(self):
        return f'First name {self.fname}'

class Product(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Product name {self.name}'

class 
