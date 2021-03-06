from flask import jsonify
from modules.auth.entities import TokenBlocklist, User
from flask_jwt_extended import create_access_token
from modules.auth.validators import UserValidator
from utils.messages import SERVER_ERROR_500
from datetime import (datetime, timezone)

class AuthRepository(object):

    def autenticate(self,username, password):
        try:
            user = User.query.filter( User.username == username  ).first()

            if user is None:
                return { 'msg' : 'No existe el usuario' }, 403
            
            autorized = user.check_password(password)

            if not autorized:
                return { 'msg': 'Contraseña no válida' }, 401

            access_token = create_access_token(identity=str(user.id))
            return { 
                'success': True,
                'user': UserValidator.from_orm(user).dict(), 
                'access_token': access_token 
            }, 200

        except Exception as e:
            return { 'msg': SERVER_ERROR_500 }, 500
    

    def logout(self, jti):
        
        now = datetime.now(timezone.utc)
        token_block_list = TokenBlocklist(jti=jti, created_at=now)
        token_block_list.save()
        return jsonify({'success': True, 'msg': "JWT revoked"}), 200
        
        
