# -*- coding: utf-8 -*-

from app.service.Operation import Operation
from flask import Blueprint


class ApiRegister:
    """
    Register created Operations objects
    """

    def __init__(self, operation: Operation, methods: list, url_rule: str, api_point: Blueprint):
        """
        operation
        methods: list of RESTapi methods
        api_point: flask Blueprint object which register subroutes
        """
        self.operation = operation
        self.api_point = api_point
        self.register(url_rule, operation.operation_route, operation.invoke, methods)

    def register(self, rule: str, endpoint: str, function: callable, methods):
        self.api_point.add_url_rule(rule, endpoint, function, methods=methods)
