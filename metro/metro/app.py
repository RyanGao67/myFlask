from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()
import sys
sys.path.append('.')
def create_app(settings_override=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.setting')
    app.config.from_pyfile('settings.py', silent=True)
    if settings_override:
        app.config.update(settings_override)

    from users import users_api
    users_api.init_app(app)

    # @app.before_first_request
    # def create_tables():
    #     db.create_all()

    @app.route('/', methods=['GET'])
    def welcome():
        return "hello, api is working", 200
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)