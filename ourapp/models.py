from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    verified_email = db.Column(db.Boolean, default=False, nullable=False)
    address = db.Column(db.String(150))
    
    def __repr__(self):
        return f'<User {self.fname}>'
