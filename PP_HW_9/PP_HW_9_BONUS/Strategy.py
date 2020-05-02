from abc import ABC, abstractmethod

import HTTPBrowser


class Strategy(ABC):

    def do_algorithm(self, browser: HTTPBrowser, workers):
        pass
