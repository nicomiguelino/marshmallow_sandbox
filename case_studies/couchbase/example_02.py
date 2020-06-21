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


def create_user():
    user = User(name="Phum Viphurit", email="phum.viphurit@example.com")
    result = UserSchema().dump(user)

    print(type(result))
    pprint(result)

    CouchbaseHelper.collection.upsert(str(uuid.uuid4()), result)



if __name__ == "__main__":
    create_user()
