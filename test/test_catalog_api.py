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
from squareconnect.apis.catalog_api import CatalogApi


class TestCatalogApi(unittest.TestCase):
    """ CatalogApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.catalog_api.CatalogApi()

    def tearDown(self):
        pass

    def test_batch_delete_catalog_objects(self):
        print("Start test case for batch_delete_catalog_objects")
        pass

    def test_batch_retrieve_catalog_objects(self):
        print("Start test case for batch_retrieve_catalog_objects")
        pass

    def test_batch_upsert_catalog_objects(self):
        print("Start test case for batch_upsert_catalog_objects")
        pass

    def test_catalog_info(self):
        print("Start test case for catalog_info")
        pass

    def test_delete_catalog_object(self):
        print("Start test case for delete_catalog_object")
        pass

    def test_list_catalog(self):
        print("Start test case for list_catalog")
        pass

    def test_retrieve_catalog_object(self):
        print("Start test case for retrieve_catalog_object")
        pass

    def test_search_catalog_objects(self):
        print("Start test case for search_catalog_objects")
        pass

    def test_update_item_modifier_lists(self):
        print("Start test case for update_item_modifier_lists")
        pass

    def test_update_item_taxes(self):
        print("Start test case for update_item_taxes")
        pass

    def test_upsert_catalog_object(self):
        print("Start test case for upsert_catalog_object")
        pass


if __name__ == '__main__':
    unittest.main()
