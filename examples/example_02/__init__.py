import datetime as dt
import os
from pprint import pprint

from marshmallow import Schema, fields


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


def run():
    """Serializing Objects ("Dumping")"""
    user = User(name="Monty", email="monty@python.org")
    schema = UserSchema()
    dict_result = schema.dump(user)
    json_result = schema.dumps(user)

    print(f"type(dict_result): { type(dict_result) }")
    pprint(f"dict_result: { dict_result }")

    print()

    print(f"type(json_result): { type(json_result) }")
    print(f"json_result: { json_result }")
