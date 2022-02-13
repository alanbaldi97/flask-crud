
from flask import jsonify
from modules.area_types.entities import AreaType
from modules.area_types.validators import AreaTypeValidator

class AreaTypeRepository(object):
    


    def get_all(self):
        areas = AreaType.query.all()
        return jsonify([ AreaTypeValidator.from_orm(area).dict() for area in areas]), 200