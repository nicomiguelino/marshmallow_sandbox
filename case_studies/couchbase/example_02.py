import datetime as dt
from pprint import pprint
import uuid

from common import CouchbaseHelper
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


if __name__ == "__main__":
    users = [
        User(name="Phum Viphurit", email="phum.viphurit@example.com"),
        User(name="Lindsey Jordan", email="snail.mail@example.com"),
        User(name="Hazel English", email="hazel.english@example.com")
    ]

    for user in users:
        CouchbaseHelper.create(user, UserSchema)
