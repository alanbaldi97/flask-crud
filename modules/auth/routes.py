from flask import Blueprint, jsonify
from modules.auth.validators import UserValidator
from modules.auth.repository import AuthRepository
from flask_pydantic import validate
from flask_jwt_extended import  (
    jwt_required,
    get_jwt_identity,
    current_user,
    create_access_token
)
from datetime import timedelta


auth_controller = Blueprint('AuthController', __name__,url_prefix='/api/auth/')
repository = AuthRepository()

@auth_controller.route('login',methods=['POST'])
@validate()
def login(body: UserValidator):
    params = body.dict()
    return repository.autenticate(**params)



@auth_controller.route('user',methods=['GET'])
@jwt_required()
def get_user():

    access_token = create_access_token(identity=get_jwt_identity(), expires_delta=timedelta(minutes=5))
    return jsonify({ 
        'user': UserValidator.from_orm(current_user).dict(),
        'access_token' : access_token
    }), 200
     
    










