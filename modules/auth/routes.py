from flask import Blueprint
from modules.auth.validators import UserValidator
from modules.auth.repository import AuthRepository
from flask_pydantic import validate

auth_controller = Blueprint('AuthController', __name__,url_prefix='/api/auth/')
repository = AuthRepository()

@auth_controller.route('login',methods=['POST'])
@validate()
def login(body: UserValidator):
    params = body.dict()
    return repository.autenticate(**params)








