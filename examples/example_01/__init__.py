from datetime import date
from pprint import pprint

import marshmallow

class ArtistSchema(marshmallow.Schema):
    name = marshmallow.fields.Str()

class AlbumSchema(marshmallow.Schema):
    title = marshmallow.fields.Str()
    release_date = marshmallow.fields.Date()
    artist = marshmallow.fields.Nested(ArtistSchema())

def run():
    """Having a taste of marshmallow..."""
    bowie = { 'name': 'David Bowie' }
    album = {
        'artist': bowie,
        'title': 'Hunky Dory',
        'release_date': date(1971, 12, 17)
    }

    schema = AlbumSchema()
    result = schema.dump(album)
    pprint(result, indent=2)
