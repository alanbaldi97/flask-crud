
from flask import Blueprint, current_app as app
spa_controller = Blueprint('SpaController', __name__,url_prefix='/')


@spa_controller.route('/', defaults={'path': ''})
@spa_controller.route('/<path:path>')
def spa(path):
    print(app.config)
    return app.send_static_file('index.html')
