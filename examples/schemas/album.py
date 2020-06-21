from marshmallow import Schema, fields

from .artist import ArtistSchema


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())
