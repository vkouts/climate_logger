from influxdb import InfluxDBClient
from app import app, db

from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with, reqparse

from .models import Record


api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('co2')

class GetDataApi(Resource):

    def get(self):
        return {}

    def post(self):
        args = parser.parse_args()
        influxdb = InfluxDBClient(host=app.config.get('INFLUXDB_HOST'), port=app.config.get('INFLUXDB_PORT'))
        influxdb.switch_database(app.config.get('INFLUXDB_DB'))
        influxdb.write_points([{'measurement': 'record', 'fields': {'co2': args.get('co2'), 'temp': 0, 'hum': 0}}])
        #record =  Record(co2=args.get('co2'))
        #db.session.add(record)
        #db.session.commit()
        return '', 201


api.add_resource(GetDataApi, '/api/v1/record/')