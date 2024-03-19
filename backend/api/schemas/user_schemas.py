from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class LoginRequest:
    username: str
    password: str


class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    @post_load
    def make_request_object(self, loaded_obj, **kwargs):
        return LoginRequest(**loaded_obj)
