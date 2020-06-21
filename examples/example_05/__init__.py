from marshmallow import ValidationError

from examples.decorators import example
from examples.schemas.user import UserSchema


@example(title="Example 05")
def run():
    """Validation"""
    try:
        result = UserSchema().load({ "name": "John", "email": "Foo" })
    except ValidationError as err:
        print(err.messages)
        print(err.valid_data)
