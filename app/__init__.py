from flask import Flask
from modules.managers.routes import managers_controller
from modules.auth.routes import auth_controller
from modules.area_types.routes import area_type_controller
from modules.spa.routes import spa_controller
from database import db
from config import Config, ProductionConfig
from config.extensions import (jwt, bcrypt)
from datetime import datetime, timezone, timedelta
from flask_cors import CORS
from flask_jwt_extended import get_jwt, create_access_token, get_jwt_identity, set_access_cookies
from decouple import config as config_decouple

def register_refreshing_token(app):
    #registro callback despues de la petición para actualizar el tiempo de expiración del token
    @app.after_request
    def refresh_expiring_jwts(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(days=365))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity(), expires_delta=timedelta(minutes=365))
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original respone
            return response




def register_entities(app, db):
    with app.app_context():
        from modules.managers.entities import Manager
        from modules.area_types.entities import AreaType
        from modules.auth.entities import User, TokenBlocklist
        db.create_all()



def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    if config_decouple('PRODUCTION', default=False):
        app.config.from_object(ProductionConfig)

    
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    register_refreshing_token(app)
    register_entities(app,db)
    
    app.register_blueprint(managers_controller)
    app.register_blueprint(auth_controller)
    app.register_blueprint(area_type_controller)
    app.register_blueprint(spa_controller)
    return app


