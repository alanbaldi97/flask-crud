
from flask import Blueprint, current_app as app, render_template
spa_controller = Blueprint('SpaController', __name__,url_prefix='/')



@spa_controller.route('/', defaults={'path': ''})
@spa_controller.route('/<path:path>')
def spa(path):
    print(path)
    return render_template('index.html')
