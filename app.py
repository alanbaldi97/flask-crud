
# from decouple import config as config_decouple
from app import create_app



app = create_app()

if __name__ == '__main__':
    app.run()