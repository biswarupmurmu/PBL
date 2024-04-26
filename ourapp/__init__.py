from flask import Flask
from .extensions import db, migrate, login_manager

def create_app():
    app = Flask(__name__)
    # app.config.from_envvar('OURAPPLICATION_SETTINGS')
    ######################################################
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config['SECRET_KEY'] = "Super secret key"
    ######################################################

    from .auth import auth
    from .public import public
    from .user import user_bp
    app.register_blueprint(auth)
    app.register_blueprint(public)
    app.register_blueprint(user_bp)


    # Initialize Flask extensions here
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    login_manager.init_app(app=app)


    # Create the database tables
    with app.app_context():
        db.create_all()


    return app
