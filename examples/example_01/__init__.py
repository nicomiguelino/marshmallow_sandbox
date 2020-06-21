from datetime import date
from pprint import pprint

from examples.decorators import example
from examples.schemas import AlbumSchema


@example(title="Example 01")
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
