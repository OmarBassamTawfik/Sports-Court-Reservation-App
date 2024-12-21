import os

from flask import Flask
from .models import db
from . import routes

def create_app(test_config=None):
    # create and configure the app
    app = Flask("Sports_Court_Reservation", instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SQLALCHEMY_DATABASE_URI='postgresql://sport%20court%20reservation_owner:cYoU2qvJO7Gz@ep-yellow-thunder-a2egfzro.eu-central-1.aws.neon.tech/sport%20court%20reservation?sslmode=require',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def hello():
        return "Welcome to the Sports Court Reservation App!"
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    app.register_blueprint(routes.bp)
    
    with app.app_context():
        db.create_all()
    
    return app
