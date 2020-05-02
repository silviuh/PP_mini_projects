from abc import abstractmethod
from typing import Any

from commands import Executor
from responsability_chain.Handler import Handler


class AbstractHandler(Handler):

    _next_handler: Handler = None
    executor: Executor = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None