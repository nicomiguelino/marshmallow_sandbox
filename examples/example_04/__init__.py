from pprint import pprint

from examples.decorators import example
from examples.schemas.user import User, UserSchema


@example(title="Example 04")
def run():
    """Handling Collections of Objects"""
    user1 = User(name="Mick Jagger", email="mick@stones.com")
    user2 = User(name="Keith Richards", email="keith@stones.com")
    users = [user1, user2]

    serialized_result = UserSchema().dump(users, many=True)
    pprint(serialized_result)

    print()

    deserialized_result = UserSchema().load(serialized_result, many=True)
    for user in deserialized_result: print(user)
