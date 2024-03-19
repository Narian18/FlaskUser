from http import HTTPStatus

from marshmallow.exceptions import ValidationError

from backend.common.errors import wrap_error


# ToDo: once all formats (file, multipart form, query string) are known, can create
#  a single wrapper for each of these
def json_args(schema, error_code=HTTPStatus.BAD_REQUEST):
    from flask import request

    def _wrap(func):
        def inner():
            try:
                args = schema.load(request.json)
                return func(args)
            except ValidationError as e:
                return wrap_error(str(e), error_code)

        return inner

    return _wrap
