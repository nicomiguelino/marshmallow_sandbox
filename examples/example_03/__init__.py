from pprint import pprint

from examples.decorators import example
from examples.schemas.user import UserSchema


@example(title="Example 03")
def run():
    """Deserializing Objects ("Loading")"""
    user_data = {
        "created_at": "2014-08-11T05:26:03.869245",
        "email": "ken@yahoo.com",
        "name": "Ken"
    }

    schema = UserSchema()
    result = schema.load(user_data)

    print(f"type(result): { type(result) }")
