from abc import abstractmethod

import HTTPBrowser
from Strategy import Strategy


class LoadBalancing(Strategy):

    def do_algorithm(self, browser: HTTPBrowser, workers):
        if browser.requests_list_size > (browser.previous_list_size + 5):
            for i in range(browser.current_number_of_tasks):
                browser.worker_consumer_tasks.append(browser.http_get(i + browser.current_number_of_tasks, workers))
            browser.current_number_of_tasks = browser.current_number_of_tasks * 2
        print(f'NUMBER OF TASKS [{browser.current_number_of_tasks}]')
