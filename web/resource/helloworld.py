from flask_restful import Resource
from flask import Response
import json

class Helloworld(Resource):
    def get(self):
        data = json.dumps({'hello':'world'})
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp
    
    def post(self):
        pass

