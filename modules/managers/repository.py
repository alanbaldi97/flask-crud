
import uuid
from config import Config
import os
from modules.managers.entities import Manager
from modules.managers.validators import ManagerValidator
from utils.messages import ROW_DELETED, ROW_INSERTED, ROW_NOT_DELETED, ROW_NOT_INSETED, ROW_NOT_UPDATED, ROW_UPDATED, SERVER_ERROR_500
from werkzeug.utils import secure_filename
from sqlalchemy import or_

class ManagerRepository(object):


    def get_all(self, params: dict):
        try:
            records = Manager.query

            area_type_id = params.get('area_type_id')
            status = params.get('status')
            search = params.get('search')


            if area_type_id is not None:
                records = records.filter( Manager.area_type_id == area_type_id )
            
            if status is not None:
                records = records.filter( Manager.status == status )

            if search is not None and search != "":
                records = records.filter( or_(Manager.name.ilike(search), Manager.last_name.ilike(search) ))


            records = records.all()


            return [ ManagerValidator.from_orm(record).dict() for record in records ], 200
        except Exception as e:
            print(str(e))
            return { 'msg': SERVER_ERROR_500 }, 500
        

    def save_manager(self, params, file):
        try:
            extension = secure_filename(file.filename).split('.')[-1]
            filename = secure_filename(f"{str(uuid.uuid1())}.{extension}" )
            
            params = {**params, 'img': filename}
            manager = Manager(**params)
            manager.save()

            path = os.path.join(Config.UPLOAD_FOLDER, filename)
            file.save(path)

            return { 'success': True, 'msg': ROW_INSERTED },  200

        except Exception as e:
            print(str(e))
            return { 'success': False, 'msg': ROW_NOT_INSETED }, 400
    
    def update_manager(self, params, file):
        try:
            current_manager_db = self.get_by_id(params.get('id'), True)

            old_img = current_manager_db.img

            manager = Manager(**params)
            
            if file is not None:
                extension = secure_filename(file.filename).split('.')[-1]
                filename = secure_filename(f"{str(uuid.uuid1())}.{extension}" )
                manager.img = filename
            else :
                manager.img = old_img

            
            manager.save()


            if file is not None:  

                if old_img is not None:
            
                    img_path = os.path.join(Config.UPLOAD_FOLDER, old_img)
                    
                    if os.path.exists(img_path):
                        os.remove(img_path)

                
                
                path = os.path.join(Config.UPLOAD_FOLDER, filename)
                file.save(path)


            return { 'success': True, 'msg': ROW_UPDATED },  200

        except Exception as e:
            return { 'success': False, 'msg': ROW_NOT_UPDATED }, 400
    
    def delete_manager(self, id):
        try:
            manager = self.get_by_id(id, True)
            old_img = manager.img
            
            manager.delete()

            img_path = os.path.join(Config.UPLOAD_FOLDER, old_img)
                    
            if os.path.exists(img_path):
                os.remove(img_path)


            return { 'success': True, 'msg': ROW_DELETED },  200

        except Exception as e:
            return { 'success': False,'msg': ROW_NOT_DELETED }, 400

    
    def get_by_id(self, id, like_object = False):
        try:
            manager = Manager.query.get(id)

            if like_object: return manager

            return {
                'manager': ManagerValidator.from_orm(manager).dict(), 
                'success': True, 
                'msg': ROW_DELETED 
            },  200

        except Exception as e:
            return { 'success': False, 'msg': SERVER_ERROR_500 }, 500
