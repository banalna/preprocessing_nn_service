# -*- coding: utf-8 -*-

from flask import Blueprint

prefix_module = '/api/v1'

bp = Blueprint(prefix_module, __name__)

from app.api.v1 import processing
