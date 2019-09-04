from flask import Flask
from config import Config
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
admin = Admin(app, name='myclimate', template_mode='bootstrap3')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes, modelviews, api