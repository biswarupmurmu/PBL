from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from ourapp.models import Customer
from ourapp import db
from ourapp import login_manager
from .form import SignupForm

auth = Blueprint("auth", __name__, template_folder="templates", url_prefix="/auth")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = Customer.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('public.index'))
    return render_template("auth/login.html")

@auth.route("/signup", methods = ["GET", "POST"])
def signup():
    form = SignupForm(request.form)
    if request.method == "POST":
        form.process_data()
        if form.validate():
            fname = form.fname.data
            lname = form.lname.data
            email = form.email.data
            password = form.password.data

            email_exists = Customer.query.filter_by(email=email).first()
            if email_exists:
                form.email.errors = ["Email already in use."]
            else:
                user = Customer(fname=fname, lname=lname, email=email, password=generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
    return render_template("auth/signup.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('public.index'))

# Login Manager setup
login_manager.login_view = "auth.login"
@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))
