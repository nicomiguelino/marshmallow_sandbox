import datetime as dt

from marshmallow import Schema, fields, post_load


class User:
    def __init__(self, name, email, **kwargs):
        self.name = name
        self.email = email
        self.created_at = kwargs.get('created_at', dt.datetime.now())

    def __repr__(self):
        return f"<User(name={ self.name } email={ self.email } " + \
            f"created_at={ self.created_at })>"


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def deserialize(self, data, **kwargs):
        return User(**data)
