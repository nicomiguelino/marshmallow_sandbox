import datetime as dt
import os
from pprint import pprint

from examples.decorators import example
from examples.schemas import UserSchema, User


@example(title="example_02")
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
