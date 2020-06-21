from pprint import pprint

from marshmallow import ValidationError

from examples.decorators import example
from examples.schemas.band import BandMemberSchema


@example(title="Example 06")
def run():
    """Another validation example"""
    user_data = [
        {"email": "mick@stones.com", "name": "Mick"},
        {"email": "invalid", "name": "Invalid"},  # invalid email
        {"email": "keith@stones.com", "name": "Keith"},
        {"email": "charlie@stones.com"},  # missing "name"
    ]

    try:
        result = BandMemberSchema(many=True).load(user_data)
    except ValidationError as err:
        pprint(err.messages)
