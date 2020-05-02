from typing import Any

from commands.Executor import Executor
from responsability_chain.AbstractHandler import AbstractHandler


class BashHandler(AbstractHandler):
    tests_passed = dict()
    nr_passed = 0

    def __init__(self):
        self.tests_passed["shebang_test"] = "not_passed"
        self.tests_passed["function_test"] = "not_passed"
        self.tests_passed["if_test"] = "not_passed"
        self.tests_passed["while_test"] = "not_passed"
        self.tests_passed["case_test"] = "not_passed"
        self.tests_passed["then_keyword_test"] = "not_passed"
        self.tests_passed["done_keyword_test"] = "not_passed"
        self.tests_passed["esac_keyword_test"] = "not_passed"

    def handle(self, request: Any) -> str:
        with open(request) as file:
            file_buffer = file.read()
            if '#!/bin/bash' in file_buffer:
                self.tests_passed["shebang_test"] = "passed"
                self.nr_passed += 1

            if 'function' in file_buffer:
                self.tests_passed["function_test"] = "passed"
                self.nr_passed += 1

            if 'if' in file_buffer:
                self.tests_passed["if_test"] = "passed"
                self.nr_passed += 1

            if 'while' in file_buffer:
                self.tests_passed["while_test"] = "passed"
                self.nr_passed += 1

            if 'case' in file_buffer:
                self.tests_passed["case_test"] = "passed"
                self.nr_passed += 1

            if 'then' in file_buffer:
                self.tests_passed["then_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'done' in file_buffer:
                self.tests_passed["done_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'esac' in file_buffer:
                self.tests_passed["esac_keyword_test"] = "passed"
                self.nr_passed += 1

            if self.nr_passed >= 3:
                self.executor = Executor(request, "bash")
                self.executor.execute()
                return "[BashHandler] --> detected file to be a bash file..."
            else:
                return super().handle(request)  # passing the request further in the chain
