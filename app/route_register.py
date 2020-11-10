# -*- coding: utf-8 -*-

from app.service.ApiRegister import ApiRegister
from app.service.Operation import Operation


def register_routes(_app):
    # register scheme of _app
    from app.api.v1 import bp as api_bp, prefix_module
    from app.api.v1.processing import preprocessing_photo

    ApiRegister(Operation('/preprocessing_photo', preprocessing_photo),
                ['POST'], '/preprocessing_photo', api_bp)

    _app.register_blueprint(api_bp, url_prefix=prefix_module)
