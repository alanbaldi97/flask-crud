from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from pydantic import ValidationError
from modules.managers.validators import ManagerValidator
from modules.managers.repository import ManagerRepository
from flask_pydantic import validate

managers_controller = Blueprint('ManagersController', __name__,url_prefix='/api')

manager_repository = ManagerRepository()

@managers_controller.route('managers',methods=['GET'])
@jwt_required()
def index():
    response, status = manager_repository.get_all()
    return jsonify(response), status


@managers_controller.route('managers',methods=['POST'])
@jwt_required()
def save_manager():
    body = request.form
    try:
        manager = ManagerValidator(**body)
        params = manager.dict()
        params.pop('area_type')
        response, status = manager_repository.save_manager(params)
        return response, status
    except ValidationError as e:
        return jsonify( e.errors() ), 422


@managers_controller.route('managers/<int:id>',methods=['PUT'])
@jwt_required()
@validate()
def update_manager( id: int, body: ManagerValidator  ):
    params = { **body.dict(), 'id': id }
    response, status = manager_repository.update_manager(params)
    return response, status

@managers_controller.route('managers/<int:id>',methods=['DELETE'])
@jwt_required()
@validate()
def delete_manager( id: int  ):
    response, status = manager_repository.delete_manager(id)
    return response, status