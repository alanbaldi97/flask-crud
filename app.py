
from decouple import config as config_decouple
from config import Config, ProductionConfig
from app import create_app

enviroment = Config
if config_decouple('PRODUCTION', default=False):
    enviroment = ProductionConfig



app = create_app(enviroment)

if __name__ == '__main__':
    app.run()