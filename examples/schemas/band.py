from marshmallow import Schema, fields


class BandMemberSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email()
