from flask import Blueprint, render_template
from flask_login import current_user, login_required
from ourapp import db
from ourapp.models import CartItem, Product

user_bp = Blueprint("user", __name__, template_folder="templates", url_prefix="/")

@user_bp.route("/profile")
@login_required
def view_profile():
    return render_template("user/profile.html")


