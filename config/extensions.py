from flask import jsonify
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from modules.auth.entities import TokenBlocklist, User

bcrypt = Bcrypt()
jwt = JWTManager()


#metodo para obtener usuario si esta autenticado
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

#Metodo callback para customizar el json de respuesta cuando el token ha expirado
@jwt.expired_token_loader
def expired_token_callback(_jwt_header, jwt_payload):
    return jsonify(msg="Token Expirado"), 401



@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = TokenBlocklist.select(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None
