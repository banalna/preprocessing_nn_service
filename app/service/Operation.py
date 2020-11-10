# -*- coding: utf-8 -*-

class Operation:
    """
    Create api operation
    """
    def __init__(self, operation_route: str, operation_function: callable):
        """
        operation_route: api route of operation
        operation_function
        """
        self._operation_function = operation_function
        self.operation_route = operation_route

    def invoke(self, *args, **kwargs):
        """
        invoke created operation
        """
        return self._operation_function(*args, **kwargs)