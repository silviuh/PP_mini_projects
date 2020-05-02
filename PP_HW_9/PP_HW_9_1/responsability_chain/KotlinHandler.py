from typing import Any

from commands.Executor import Executor
from responsability_chain.AbstractHandler import AbstractHandler


class KotlinHandler(AbstractHandler):
    tests_passed = dict()
    nr_passed = 0

    def __init__(self):
        self.tests_passed["fun_keyword_test"] = "not_passed"
        self.tests_passed["as_keyword_test"] = "not_passed"
        self.tests_passed["null_keyword_test"] = "not_passed"
        self.tests_passed["when_keyword_test"] = "not_passed"
        self.tests_passed["by_keyword_test"] = "not_passed"
        self.tests_passed["property_keyword_test"] = "not_passed"
        self.tests_passed["companion_keyword_test"] = "not_passed"
        self.tests_passed["data_keyword_test"] = "not_passed"
        self.tests_passed["override_keyword_test"] = "not_passed"
        self.tests_passed["it_keyword_test"] = "not_passed"
        self.tests_passed["===_operator_test"] = "not_passed"
        self.tests_passed[".._operator_test"] = "not_passed"
        self.tests_passed["!!_operator_test"] = "not_passed"
        self.tests_passed["?_operator_test"] = "not_passed"

    def handle(self, request: Any) -> str:
        with open(request) as file:
            file_buffer = file.read()
            if 'fun' in file_buffer:
                self.tests_passed["fun_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'as' in file_buffer:
                self.tests_passed["as_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'null' in file_buffer:
                self.tests_passed["null_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'when' in file_buffer:
                self.tests_passed["when_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'by' in file_buffer:
                self.tests_passed["by_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'property' in file_buffer:
                self.tests_passed["property_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'companion' in file_buffer:
                self.tests_passed["companion_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'data' in file_buffer:
                self.tests_passed["data_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'override' in file_buffer:
                self.tests_passed["override_keyword_test"] = "passed"
                self.nr_passed += 1

            if 'it' in file_buffer:
                self.tests_passed["it_keyword_test"] = "passed"
                self.nr_passed += 1

            if '===' in file_buffer:
                self.tests_passed["===_operator_test"] = "passed"
                self.nr_passed += 1

            if '..' in file_buffer:
                self.tests_passed[".._operator_test"] = "passed"
                self.nr_passed += 1

            if '!!' in file_buffer:
                self.tests_passed["!!_operator_test"] = "passed"
                self.nr_passed += 1

            if '?' in file_buffer:
                self.tests_passed["?_operator_test"] = "passed"
                self.nr_passed += 1

            if self.nr_passed >= 4:
                self.executor = Executor(request, "kotlin")
                self.executor.execute()
                return "[KotlinHandler] --> detected file to be a kt file..."
            else:
                return super().handle(request)  # passing the request further in the chain