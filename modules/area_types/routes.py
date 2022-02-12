from flask import Blueprint

managers_controller = Blueprint('ManagersController', __name__,url_prefix='/api')

@managers_controller.route('managers',methods=['GET'])
def index():
    return 'Hola mundo'
