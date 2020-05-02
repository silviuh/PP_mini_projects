from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass


    @abstractmethod
    def handle(self, request) -> str:
        pass