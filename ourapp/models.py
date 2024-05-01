from . import db
from flask_login import UserMixin

class Customer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    verified_email = db.Column(db.Boolean, default=False, nullable=False)
    address = db.Column(db.String(150))
    
    # New lines added
    cart = db.relationship('CartItem', backref='customer', lazy=True)
    # orders = db.relationship('Order', backref='customer', lazy=True)
    # End of new lines

    def __repr__(self):
        return f'First name {self.fname}'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    # New lines added

    # End of new lines

    def __repr__(self):
        return f'Product name {self.name}'

# New lines
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, default=1)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref='cart_items')
#
# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
#     customer = db.relationship('Customer', backref='orders')
#     ordered_items = db.relationship('OrderedItem', backref='order', cascade='all, delete-orphan')
#
# class OrderedItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     product = db.relationship('Product')
#     quantity = db.Column(db.Integer, nullable=False)
