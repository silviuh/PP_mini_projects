import json
import os
from datetime import time, datetime
from sys import path
import os.path
from os import path

import recordtype as recordtype
import requests

from GetRequest import GetRequest
from HTTPGenericRequest import HTTPGenericRequest


class CachedRequest(HTTPGenericRequest):
    timeout: float
    get_request: GetRequest
    cache: str
    customized_responses: dict
    UNITIALIZED_TIME_LAPSE_DIFFERENCE = 999999

    def __init__(self, get_request: GetRequest, cache_file: str):
        self.get_request = get_request
        self.cache = cache_file
        self.customized_responses = dict()

    def get_response(self) -> str:
        delta = self.UNITIALIZED_TIME_LAPSE_DIFFERENCE

        if path.exists(self.cache):
            with open(self.cache) as json_file:
                if os.path.getsize(self.cache) > 0:
                    self.customized_responses = json.load(json_file)

                    current_time = datetime.now().time().strftime("%H:%M:%S")
                    FMT = '%H:%M:%S'

                    if self.get_request.URL in self.customized_responses.keys():
                        delta = (datetime.strptime(current_time, FMT)
                                 - datetime.strptime(self.customized_responses[self.get_request.URL]["timestamp"],
                                                     FMT)).seconds

                    if delta < 3600:  # read from cache
                        print("\n[ <- CACHED -> ]")
                        json_file.close()
                        return self.customized_responses[self.get_request.URL]["response_content"]

                    else:
                        with open(self.cache, "w") as json_file:
                            request_init_time = datetime.now().time().strftime("%H:%M:%S")
                            response = self.get_request.get_response_base()

                            self.customized_responses[self.get_request.URL] = ({
                                'timestamp': request_init_time,
                                'response_content': response
                            })

                            json.dump(self.customized_responses, json_file)
                            return self.customized_responses[self.get_request.URL]["response_content"]

                        json_file.close()

                else:
                    with open(self.cache, "w") as json_file:
                        request_init_time = datetime.now().time().strftime("%H:%M:%S")
                        response = self.get_request.get_response_base()

                        self.customized_responses[self.get_request.URL] = ({
                            'timestamp': request_init_time,
                            'response_content': response
                        })

                        json.dump(self.customized_responses, json_file)
                        return self.customized_responses[self.get_request.URL]["response_content"]

                    json_file.close()

        json_file.close()
