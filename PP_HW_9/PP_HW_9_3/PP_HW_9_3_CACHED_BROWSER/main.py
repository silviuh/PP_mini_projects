import requests

from CachedRequest import CachedRequest
from GetRequest import GetRequest

if __name__ == '__main__':
    # FISIERUL CACHE TREBUIE SA FIE DEJA CREAT!!!

    browser_session_is_Active = True

    while browser_session_is_Active:
        print("\n\n\n")
        print("----------------------------------------------------------------------------")
        print("WELCOME TO THE CACHED BROWSER SESSION...[ V.01 ]")
        print("                                   MENU")
        print("                  1. Get HTTP request + print response body")
        print("                  2. Exit")
        print("----------------------------------------------------------------------------")

        choice = int(input("\n\nChoice? [1/2]: "))

        if choice == 1:
            url = input("Introduce URL: ")
            get_request = GetRequest(url, dict(), 1000)
            request = CachedRequest(get_request, "get_cache.txt")
            print("\t[Response]:\n" + "\t\t" + request.get_response())

        elif choice == 2:
            choice = input("\n\nDo you wish to continue? [y/n]: ")
            if choice == "n":
                browser_session_is_Active = False
                print("\n\n-----> YOU HAVE EXITED THE SESSION...")
