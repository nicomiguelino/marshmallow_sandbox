import uuid

from common import CouchbaseHelper

class User(CouchbaseHelper):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

        self.first_name = kwargs.get("first_name", None)
        self.last_name = kwargs.get("last_name", None)
        self.email = kwargs.get("email", None)
        self.interests = kwargs.get("interests", None)

    def save(self):
        self.collection.upsert(str(uuid.uuid4()), {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "interests": self.interests
        })


if __name__ == "__main__":
    user = User(
        first_name="Lindsey", last_name="Jordan",
        email="lindsey.jordan@snailmail.com",
        interests=[
            "Indie Music",
            "Ice Hockey"
        ]
    )

    user.interests.append("Guitars")
    user.save()
