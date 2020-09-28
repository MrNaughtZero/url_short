from flask import Flask
from app.database import setup_db

app = Flask(__name__)
app.secret_key = 'sihoeiu049u2oiwekhkjwehk'
app.debug = True

setup_db(app)

from . import routes