from flask import Flask
from modules.managers.routes import managers_controller
from modules.auth.routes import auth_controller
from database import db
from config import Config
from config.extensions import (jwt, bcrypt)
from datetime import datetime, timezone, timedelta

from flask_jwt_extended import get_jwt, create_access_token, get_jwt_identity, set_access_cookies


def register_refreshing_token(app):
    #registro callback despues de la petición para actualizar el tiempo de expiración del token
    @app.after_request
    def refresh_expiring_jwts(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=5))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity(), expires_delta=timedelta(minutes=5))
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original respone
            return response




def register_entities(app, db):
    with app.app_context():
        from modules.area_types.entities import AreaType
        from modules.managers.entities import Manager
        from modules.auth.entities import User
        db.create_all()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    register_refreshing_token(app)

    register_entities(app,db)
    app.register_blueprint(managers_controller)
    app.register_blueprint(auth_controller)
    return app