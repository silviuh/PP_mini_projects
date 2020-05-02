import copy
from abc import ABC


class HTTPGenericRequest():
    URL: str
    params: dict

    def __init__(self, URL: str, params: dict):
        self.URL = URL
        self.params = params

    def clone(self):
        return copy.copy(self)
