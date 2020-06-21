import uuid

from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator


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

    @classmethod
    def create(cls, obj, schema_cls):
        schema = schema_cls()
        result = schema.dump(obj)
        cls.collection.upsert(str(uuid.uuid4()), result)
