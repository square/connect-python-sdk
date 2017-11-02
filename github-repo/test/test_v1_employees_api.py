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
from squareconnect.apis.v1_employees_api import V1EmployeesApi


class TestV1EmployeesApi(unittest.TestCase):
    """ V1EmployeesApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.v1_employees_api.V1EmployeesApi()

    def tearDown(self):
        pass

    def test_create_employee(self):
        print ("Start test case for create_employee")
        pass

    def test_create_employee_role(self):
        print ("Start test case for create_employee_role")
        pass

    def test_create_timecard(self):
        print ("Start test case for create_timecard")
        pass

    def test_delete_timecard(self):
        print ("Start test case for delete_timecard")
        pass

    def test_list_cash_drawer_shifts(self):
        print ("Start test case for list_cash_drawer_shifts")
        pass

    def test_list_employee_roles(self):
        print ("Start test case for list_employee_roles")
        pass

    def test_list_employees(self):
        print ("Start test case for list_employees")
        pass

    def test_list_timecard_events(self):
        print ("Start test case for list_timecard_events")
        pass

    def test_list_timecards(self):
        print ("Start test case for list_timecards")
        pass

    def test_retrieve_cash_drawer_shift(self):
        print ("Start test case for retrieve_cash_drawer_shift")
        pass

    def test_retrieve_employee(self):
        print ("Start test case for retrieve_employee")
        pass

    def test_retrieve_employee_role(self):
        print ("Start test case for retrieve_employee_role")
        pass

    def test_retrieve_timecard(self):
        print ("Start test case for retrieve_timecard")
        pass

    def test_update_employee(self):
        print ("Start test case for update_employee")
        pass

    def test_update_employee_role(self):
        print ("Start test case for update_employee_role")
        pass

    def test_update_timecard(self):
        print ("Start test case for update_timecard")
        pass


if __name__ == '__main__':
    unittest.main()
