from flask import Flask
from flask_mysqldb import MySQL

db = MySQL()

def create_app():
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'MyDB'

    db.init_app(app)

    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

