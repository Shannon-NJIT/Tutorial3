from flask import Flask
#from config import app_config
from .models import db, bcrypt

from .views.UserView import user_api as user_blueprint


def create_app(env_name):
    # Creating app
    app = Flask(__name__)
    # app initialization
    #app.config.from_object(app_config[env_name])

    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/vi/users')

    @app.route('/', methods=['GET'])
    def index():
        # example endpoint
        return 'Congratulations! your first endpoint is working'

    return app
