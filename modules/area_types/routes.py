from flask import Blueprint
from modules.area_types.repository import AreaTypeRepository

area_type_controller = Blueprint('AreaTypeController', __name__,url_prefix='/api')

area_type_repository = AreaTypeRepository()

@area_type_controller.route('area-types',methods=['GET'])
def index():
    return area_type_repository.get_all()
