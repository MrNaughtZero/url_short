from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

database_name = 'url_short'
database_path = 'mysql://root:@localhost/url_short'

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()