from flask_restful import Resource
from flask import Response,request
from flask_restful import reqparse
from pprint import pprint
from serializer import UserSchema
import json
from marshmallow import ValidationError

class record(Resource):
    def get(self):

        return "OK"

    def post(self):
        formData1 = request.form['formData']
        formData2 = json.loads(formData1)
        formData3 = formData2['formData']

        try:
            result = UserSchema().load(formData3)
             
        except ValidationError as err:
            print('err:',err.messages)
            return json.dumps(err.messages)

        return 'submit success'
