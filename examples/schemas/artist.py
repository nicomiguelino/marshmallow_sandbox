from marshmallow import Schema, fields


class ArtistSchema(Schema):
    name = fields.Str()
