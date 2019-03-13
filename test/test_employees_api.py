# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import

import os
import sys
import unittest

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.employees_api import EmployeesApi


class TestEmployeesApi(unittest.TestCase):
    """ EmployeesApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.employees_api.EmployeesApi()

    def tearDown(self):
        pass

    def test_list_employees(self):
        print("Start test case for list_employees")
        pass

    def test_retrieve_employee(self):
        print("Start test case for retrieve_employee")
        pass


if __name__ == '__main__':
    unittest.main()
