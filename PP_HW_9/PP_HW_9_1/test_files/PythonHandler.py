from typing import Any

from responsability_chain.AbstractHandler import AbstractHandler


class PythonHandler(AbstractHandler):
    tests_passed = dict()
    nr_passed = 0

    def __init__(self):
        self.tests_passed["shebang_test"] = "not_passed"
        self.tests_passed["def_test"] = "not_passed"
        self.tests_passed["elif_test_keyword"] = "not_passed"
        self.tests_passed["raise_test_keyword"] = "not_passed"
        self.tests_passed["yield_test_keyword"] = "not_passed"
        self.tests_passed["finally_test_keyword"] = "not_passed"
        self.tests_passed["False_test_keyword"] = "not_passed"
        self.tests_passed["True_test_keyword"] = "not_passed"
        self.tests_passed["assert_test_keyword"] = "not_passed"

    def handle(self, request: Any) -> str:
        with open(request) as file:
            file_buffer = file.read()
            if '#!/bin/python' in file_buffer:
                self.tests_passed["shebang_test"] = "passed"
                self.nr_passed += 1

            if 'elif' in file_buffer:
                self.tests_passed["elif_test_keyword"] = "passed"
                self.nr_passed += 1

            if 'raise' in file_buffer:
                self.tests_passed["raise_test_keyword"] = "passed"
                self.nr_passed += 1

            if 'yield' in file_buffer:
                self.tests_passed["yield_test_keyword"] = "passed"
                self.nr_passed += 1

            if 'finally' in file_buffer:
                self.tests_passed["finally_test_keyword"] = "passed"
                self.nr_passed += 1

            if 'False' in file_buffer:
                self.tests_passed["False_test_keyword"] = "passed"
                self.nr_passed += 1

            if 'True' in file_buffer:
                self.tests_passed["True_test_keyword"] = "passed"
                self.nr_passed += 1

            if 'assert' in file_buffer:
                self.tests_passed["assert_test_keyword"] = "passed"
                self.nr_passed += 1

            if self.nr_passed >= 3:
                return "[PythonHandler] --> detected file to be a python file..."
            else:
                return super().handle(request)  # passing the request further in the chain