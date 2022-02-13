import os
from flask import Blueprint, jsonify, request, send_file

from flask_jwt_extended import jwt_required
from pydantic import ValidationError
from modules.managers.validators import ManagerValidator, FilterValidator
from modules.managers.repository import ManagerRepository
from flask_pydantic import validate

from utils.image_validator_expcetion import ImageValidatorException

managers_controller = Blueprint('ManagersController', __name__,url_prefix='/api')

manager_repository = ManagerRepository()

@managers_controller.route('managers',methods=['POST'])
@jwt_required()
@validate()
def index(body: FilterValidator):
    params = body.dict()
    response, status = manager_repository.get_all(params)
    return jsonify(response), status


@managers_controller.route('managers/store',methods=['POST'])
@jwt_required()
def save_manager():
    body = request.form
    try:

        if 'image' not in request.files:
            raise ImageValidatorException('image','La imagen es requerida')

        file = request.files['image']

        manager = ManagerValidator(**body)
        params = manager.dict()
        params.pop('area_type')
        response, status = manager_repository.save_manager(params, file)
        return response, status
    except ImageValidatorException as e:
        return jsonify( e.errors() ), 422
    except ValidationError as e:
        return jsonify( e.errors() ), 422


@managers_controller.route('managers/<int:id>',methods=['POST'])
@jwt_required()
@validate()
def update_manager( id: int  ):

    body = request.form
    try:

        file = None

        if 'image' in request.files:
            file = request.files['image']

        params = { **body, 'id': id }

        manager = ManagerValidator(**params)
        params_update = manager.dict()
        params_update.pop('area_type')
        response, status = manager_repository.update_manager(params_update, file)
        return response, status
    except ValidationError as e:
        return jsonify( e.errors() ), 422
    
    

@managers_controller.route('managers/<int:id>',methods=['DELETE'])
@jwt_required()
@validate()
def delete_manager( id: int  ):
    response, status = manager_repository.delete_manager(id)
    return response, status



@managers_controller.route('managers/<int:id>/get-by-id',methods=['GET'])
@jwt_required()
@validate()
def get_by_id( id: int  ):
    response, status = manager_repository.get_by_id(id)
    return response, status


@managers_controller.route('managers/get-image',methods=['GET'])
# @jwt_required()
@validate()
def get_image():
    try: 

        filename = request.args.get('filename')

        abs_path = os.path.abspath(f'static/uploads/{filename}')

        return send_file(abs_path), 200
        # return redirect(url_for('static', filename=f'uploads/{filename}' ), 303)
    except Exception as e:
        return { 'error': 'Ocurrio un error' }, 404
   