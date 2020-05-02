import asyncio
from threading import Timer

from HTTPBrowser import HTTPBrowser
from LoadBalancing import LoadBalancing


async def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    work_queue = asyncio.Queue()

    # Put some work in the queue
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]:
        await work_queue.put(url)

    browser = HTTPBrowser(2,
                          work_queue.qsize(),
                          LoadBalancing()
                          )

    await browser.browser_session(work_queue)


if __name__ == "__main__":
    asyncio.run(main())
