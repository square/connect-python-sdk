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
from squareconnect.apis.labor_api import LaborApi


class TestLaborApi(unittest.TestCase):
    """ LaborApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.labor_api.LaborApi()

    def tearDown(self):
        pass

    def test_create_break_type(self):
        print("Start test case for create_break_type")
        pass

    def test_create_shift(self):
        print("Start test case for create_shift")
        pass

    def test_delete_break_type(self):
        print("Start test case for delete_break_type")
        pass

    def test_delete_shift(self):
        print("Start test case for delete_shift")
        pass

    def test_get_break_type(self):
        print("Start test case for get_break_type")
        pass

    def test_get_employee_wage(self):
        print("Start test case for get_employee_wage")
        pass

    def test_get_shift(self):
        print("Start test case for get_shift")
        pass

    def test_list_break_types(self):
        print("Start test case for list_break_types")
        pass

    def test_list_employee_wages(self):
        print("Start test case for list_employee_wages")
        pass

    def test_list_workweek_configs(self):
        print("Start test case for list_workweek_configs")
        pass

    def test_search_shifts(self):
        print("Start test case for search_shifts")
        pass

    def test_update_break_type(self):
        print("Start test case for update_break_type")
        pass

    def test_update_shift(self):
        print("Start test case for update_shift")
        pass

    def test_update_workweek_config(self):
        print("Start test case for update_workweek_config")
        pass


if __name__ == '__main__':
    unittest.main()
