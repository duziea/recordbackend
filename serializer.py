from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.Str()
    phone = fields.Str()
    thing = fields.Str()
    note = fields.Str()
    finish = fields.Str()
    create_time = fields.DateTime()