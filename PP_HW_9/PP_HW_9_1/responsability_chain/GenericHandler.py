import re
from typing import Any

from responsability_chain.AbstractHandler import AbstractHandler


class GenericHandler(AbstractHandler):

    def __init__(self):
        pass

    def handle(self, request: Any) -> str:
        return "[GenericHandler] --> file extension could not be detected..."


