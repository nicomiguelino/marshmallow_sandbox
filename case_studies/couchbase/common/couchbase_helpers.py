import uuid

from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator


"""Improvement Items
- You could let marshmallow do the serialization/deserialization. Refer to
  https://marshmallow.readthedocs.io/en/stable/ for documentation.
- Add support for flushing buckets.
"""

class CouchbaseConfig:
    USERNAME = "Administrator"
    PASSWORD = "Administrator"
    URL = "couchbase://localhost"
    BUCKET_NANE = "django"


class CouchbaseHelper:
    password_authenticator = PasswordAuthenticator(CouchbaseConfig.USERNAME, CouchbaseConfig.PASSWORD)
    cluster_options = ClusterOptions(password_authenticator)

    cluster = Cluster(CouchbaseConfig.URL, cluster_options)
    bucket = cluster.bucket(CouchbaseConfig.BUCKET_NANE)
    collection = bucket.default_collection()

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
