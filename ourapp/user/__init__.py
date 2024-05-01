from flask import Blueprint, render_template
from flask_login import current_user, login_required
from ourapp import db
from ourapp.models import CartItem, Product

user_bp = Blueprint("user", __name__, template_folder="templates", url_prefix="/")

@user_bp.route("/profile")
@login_required
def view_profile():
    return render_template("user/profile.html")

@user_bp.route("/add-to-cart/<int:id>")
@login_required
def add_to_cart(id):
    product = Product.query.filter_by(id=id).first()
    if product:
        # Check if product is already in the cart
        cart_item = CartItem.query.filter_by(product_id=id, customer_id=current_user.id).first()
        if cart_item:
            cart_item.quantity += 1
        else:
            new_cart_item = CartItem(product_id=id, customer_id=current_user.id)
            db.session.add(new_cart_item)
        db.session.commit()

        for cartitem in current_user.cart:
            print(cartitem.product, cartitem.quantity)
        
        return f"{product.name}"
    else:
        return "No products found"
