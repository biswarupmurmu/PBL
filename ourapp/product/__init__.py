from flask import Blueprint, render_template
from ourapp.models import Product

product_bp=Blueprint("product_bp",__name__, url_prefix="/products", template_folder="templates")

@product_bp.route('/')
def view_all_products():
    products=Product.query.all()
    return render_template("product/all_products.html",products=products)