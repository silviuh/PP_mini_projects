import asyncio

import aiohttp as aiohttp

from LoadBalancing import LoadBalancing
from Strategy import Strategy


class HTTPBrowser:
    session_is_on = True
    previous_list_size: int
    requests_list_size: int
    current_number_of_tasks: int
    worker_consumer_tasks = []
    worker_producer_tasks = []
    used_strategy: Strategy

    incoming_requests = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
        "https://docs.python.org/3/library/multiprocessing.html",
        "https://www.guru99.com/python-check-if-file-exists.html"
    ]

    def __init__(self, given_number_of_task: int, url_list_size: int, load_balancing: Strategy):
        self.current_number_of_tasks = given_number_of_task
        self.previous_list_size = url_list_size
        self.requests_list_size = url_list_size
        self.used_strategy = load_balancing

    @staticmethod
    async def http_get(worker_name, worker_queue):
        async with aiohttp.ClientSession() as session:
            while not worker_queue.empty():
                url = await worker_queue.get()
                print(f"Task {worker_name} --> getting URL: {url}")
                async with session.get(url) as response:
                    await response.text()

    async def receive_requests(self, worker_queue):
        await asyncio.sleep(1)
        for req in self.incoming_requests:
            await worker_queue.put(req)

        self.requests_list_size = worker_queue.qsize()

    def close_session(self):
        self.session_is_on = False

    async def browser_session(self, work_queue):
        self.worker_producer_tasks.append(self.receive_requests(work_queue))
        self.worker_producer_tasks.append(self.receive_requests(work_queue))

        while self.session_is_on:
            await self.receive_requests(work_queue)
            print(f'CURRENT_LIST_SIZE: {self.requests_list_size}   PREVIOUS_LIST_SIZE: {self.previous_list_size}')
            # if self.requests_list_size > (self.previous_list_size + 5):
            #     for i in range(self.current_number_of_tasks):
            #         self.worker_consumer_tasks.append(self.http_get(i, work_queue))
            #     self.current_number_of_tasks = self.current_number_of_tasks * 2  # double the workers number
            self.used_strategy.do_algorithm(self,
                                            work_queue
                                            )

            asyncio.gather(*self.worker_consumer_tasks)
            self.previous_list_size = self.requests_list_size
