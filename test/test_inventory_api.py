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
from squareconnect.apis.inventory_api import InventoryApi


class TestInventoryApi(unittest.TestCase):
    """ InventoryApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.inventory_api.InventoryApi()

    def tearDown(self):
        pass

    def test_batch_change_inventory(self):
        print("Start test case for batch_change_inventory")
        pass

    def test_batch_retrieve_inventory_changes(self):
        print("Start test case for batch_retrieve_inventory_changes")
        pass

    def test_batch_retrieve_inventory_counts(self):
        print("Start test case for batch_retrieve_inventory_counts")
        pass

    def test_retrieve_inventory_adjustment(self):
        print("Start test case for retrieve_inventory_adjustment")
        pass

    def test_retrieve_inventory_changes(self):
        print("Start test case for retrieve_inventory_changes")
        pass

    def test_retrieve_inventory_count(self):
        print("Start test case for retrieve_inventory_count")
        pass

    def test_retrieve_inventory_physical_count(self):
        print("Start test case for retrieve_inventory_physical_count")
        pass


if __name__ == '__main__':
    unittest.main()
