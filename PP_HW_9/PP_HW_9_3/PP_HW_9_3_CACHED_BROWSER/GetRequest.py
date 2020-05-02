from typing import Any

import requests

from HTTPGenericRequest import HTTPGenericRequest


class GetRequest(HTTPGenericRequest):
    timeout: float

    def __init__(self, URL: str, params: dict, timeout: float):
        self.URL = URL
        self.params = params
        self.timeout = timeout

    def get_response_base(self) -> Any:
        response = requests.get(self.URL, timeout=self.timeout).text
        return response
