from typing import Any


class Observable:
    observers: list

    def __init__(self):
        self.observers = list()

    def attach(self, observer: Any):
        self.observers.append(observer)

    def detach(self, observer: Any):
        self.observers.remove(observer)

    def notify_all(self):
        pass
