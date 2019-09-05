import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    # --------------------- INFLUXDB ---------------------------
    INFLUXDB_HOST = os.environ.get('INFLUXDB_HOST', '127.0.0.1')
    INFLUXDB_PORT = os.environ.get('INFLUXDB_PORT', 8086)
    INFLUXDB_DB = os.environ.get('INFLUXDB_DB', 'myclimate')

