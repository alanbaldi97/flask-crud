
from modules.managers.entities import Manager
from modules.managers.validators import ManagerValidator
from utils.messages import ROW_DELETED, ROW_INSERTED, ROW_NOT_DELETED, ROW_NOT_INSETED, ROW_NOT_UPDATED, ROW_UPDATED, SERVER_ERROR_500


class ManagerRepository(object):


    def get_all(self):
        try:
            records = Manager.query.all()
            ManagerValidator
            return [ ManagerValidator.from_orm(record).dict() for record in records ], 200
        except Exception as e:
            print(str(e))
            return { 'msg': SERVER_ERROR_500 }, 500
        

    def save_manager(self, params):
        try:
            print(params)
            manager = Manager(**params)
            manager.save()

            return { 'msg': ROW_INSERTED },  200

        except Exception as e:
            return { 'msg': ROW_NOT_INSETED }, 400
    
    def update_manager(self, params):
        try:
            manager = Manager(**params)
            manager.save()

            return { 'msg': ROW_UPDATED },  200

        except Exception as e:
            return { 'msg': ROW_NOT_UPDATED }, 400
    
    def delete_manager(self, id):
        try:
            manager = Manager(id = id)
            manager.delete()
            return { 'msg': ROW_DELETED },  200

        except Exception as e:
            print(str(e))
            return { 'msg': ROW_NOT_DELETED }, 400
