import re
from typing import Any

from commands.Executor import Executor
from responsability_chain.AbstractHandler import AbstractHandler


class JavaHandler(AbstractHandler):
    tests_passed = dict()
    nr_passed = 0

    def __init__(self):
        self.tests_passed["main_method_test"] = "not_passed"
        self.tests_passed["imports_test"] = "not_passed"
        self.tests_passed["extends_keyword_test"] = "not_passed"
        self.tests_passed["implements_keyword_test"] = "not_passed"
        self.tests_passed["this_test"] = "not_passed"
        self.tests_passed["boolean_test"] = "not_passed"
        self.tests_passed["interface_test"] = "not_passed"
        self.tests_passed["static_keyword_test"] = "not_passed"
        self.tests_passed["void_keyword_test"] = "not_passed"
        self.tests_passed["new_keyword_test"] = "not_passed"

    def handle(self, request: Any) -> str:
        with open(request) as file:
            file_buffer = file.read()
            if 'public static void main(String[] args)' in file_buffer:
                self.tests_passed["main_method_test"] = "passed"
                self.nr_passed += 1

            if re.search('((?<=\bimport\s)\s*([^\s]+ )*([a-z.A-Z0-9]+.(?=;)))', file_buffer):
                self.tests_passed["imports_test"] = "passed"
                self.nr_passed += 1

            if 'extends' in file_buffer:
                self.tests_passed["extends_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'implements' in file_buffer:
                self.tests_passed["implements_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'this' in file_buffer:
                self.tests_passed["this_test"] = "passed"
                self.nr_passed += 1

            if 'interface' in file_buffer:
                self.tests_passed["interface_test"] = "passed"
                self.nr_passed += 1

            if 'static' in file_buffer:
                self.tests_passed["static_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'void' in file_buffer:
                self.tests_passed["void_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'new' in file_buffer:
                self.tests_passed["new_keyword_test"] = "passed"
                self.nr_passed += 1

            if self.nr_passed >= 4:
                self.executor = Executor(request, "java")
                self.executor.execute()
                return "[JavaHandler] --> detected file to be a java file..."
            else:
                return super().handle(request)  # passing the request further in the chain