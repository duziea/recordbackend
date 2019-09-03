#初始化app

from flask import Flask,request,redirect,url_for
from flask_restful import Api
from flask_cors import CORS
from flask_pymongo import PyMongo,ASCENDING,DESCENDING
from datetime import datetime
from flask_restful import Resource
from flask import Response,request
from flask_restful import reqparse
from pprint import pprint
import json
from marshmallow import ValidationError
import ast
from bson.objectid import ObjectId
from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.Str()
    phone = fields.Str()
    thing = fields.Str()
    note = fields.Str()
    finish = fields.Str()
    create_time = fields.DateTime()


app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb://localhost:27017/mydatabase',
    MONGO_USERNAME='record',
    MONGO_PASSWORD='record'
)
 
mongo = PyMongo(app)
CORS(app,supports_credentials=True)

class datetimeEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj,ObjectId):
            return str(obj)
        


class record(Resource):
    def get(self):
        querydata = request.args    
        print('querydata:',querydata)
        querydata2 = querydata.to_dict()
        querydata3 = json.loads(querydata2['data'])
        print(querydata3)  
        if '_id' in querydata3:
            querydata3['_id'] = ObjectId(querydata3['_id'])
        record = mongo.db.record.find(querydata3).sort('_id', DESCENDING)
        dic = {}
        dic['search'] = []
        for i in record:
            dic['search'].append(i)

        json_dic = json.dumps(dic,ensure_ascii=False,cls=datetimeEncoder )
        print(json_dic)
        return json_dic

    def post(self):
        formData1 = request.json
        formData3 = formData1['data']['formData']
        create_time = datetime.now().isoformat()
        formData3['create_time'] = create_time

        try:
            result = UserSchema().load(formData3)
            print(result)
            print(type(result))
        except ValidationError as err:
            print('err:',err.messages)
            return json.dumps(err.messages)

        mongo.db.record.insert(result)
        return 'submit success'

    def put(self):
        data = request.json
        condition = data['data']
        condition['_id'] = ObjectId(condition['_id'])
        record = mongo.db.record.find_one(condition)
        print(record)
        record['finish'] = '1'
        result = mongo.db.record.update(condition,record)
        print(result)
        return 'update success'

#api资源
api = Api(app)
api.add_resource(record,'/api/record')


if __name__ == "__main__":
    app.run(debug=True)