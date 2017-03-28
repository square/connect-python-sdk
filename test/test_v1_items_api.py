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
from squareconnect.apis.v1_items_api import V1ItemsApi


class TestV1ItemsApi(unittest.TestCase):
    """ V1ItemsApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.v1_items_api.V1ItemsApi()

    def tearDown(self):
        pass

    def test_adjust_inventory(self):
        print ("Start test case for adjust_inventory")
        pass

    def test_apply_fee(self):
        print ("Start test case for apply_fee")
        pass

    def test_apply_modifier_list(self):
        print ("Start test case for apply_modifier_list")
        pass

    def test_create_category(self):
        print ("Start test case for create_category")
        pass

    def test_create_discount(self):
        print ("Start test case for create_discount")
        pass

    def test_create_fee(self):
        print ("Start test case for create_fee")
        pass

    def test_create_item(self):
        print ("Start test case for create_item")
        pass

    def test_create_modifier_list(self):
        print ("Start test case for create_modifier_list")
        pass

    def test_create_modifier_option(self):
        print ("Start test case for create_modifier_option")
        pass

    def test_create_page(self):
        print ("Start test case for create_page")
        pass

    def test_create_variation(self):
        print ("Start test case for create_variation")
        pass

    def test_delete_category(self):
        print ("Start test case for delete_category")
        pass

    def test_delete_discount(self):
        print ("Start test case for delete_discount")
        pass

    def test_delete_fee(self):
        print ("Start test case for delete_fee")
        pass

    def test_delete_item(self):
        print ("Start test case for delete_item")
        pass

    def test_delete_modifier_list(self):
        print ("Start test case for delete_modifier_list")
        pass

    def test_delete_modifier_option(self):
        print ("Start test case for delete_modifier_option")
        pass

    def test_delete_page(self):
        print ("Start test case for delete_page")
        pass

    def test_delete_page_cell(self):
        print ("Start test case for delete_page_cell")
        pass

    def test_delete_variation(self):
        print ("Start test case for delete_variation")
        pass

    def test_list_categories(self):
        print ("Start test case for list_categories")
        pass

    def test_list_discounts(self):
        print ("Start test case for list_discounts")
        pass

    def test_list_fees(self):
        print ("Start test case for list_fees")
        pass

    def test_list_inventory(self):
        print ("Start test case for list_inventory")
        pass

    def test_list_items(self):
        print ("Start test case for list_items")
        pass

    def test_list_modifier_lists(self):
        print ("Start test case for list_modifier_lists")
        pass

    def test_list_pages(self):
        print ("Start test case for list_pages")
        pass

    def test_remove_fee(self):
        print ("Start test case for remove_fee")
        pass

    def test_remove_modifier_list(self):
        print ("Start test case for remove_modifier_list")
        pass

    def test_retrieve_item(self):
        print ("Start test case for retrieve_item")
        pass

    def test_retrieve_modifier_list(self):
        print ("Start test case for retrieve_modifier_list")
        pass

    def test_update_category(self):
        print ("Start test case for update_category")
        pass

    def test_update_discount(self):
        print ("Start test case for update_discount")
        pass

    def test_update_fee(self):
        print ("Start test case for update_fee")
        pass

    def test_update_item(self):
        print ("Start test case for update_item")
        pass

    def test_update_modifier_list(self):
        print ("Start test case for update_modifier_list")
        pass

    def test_update_modifier_option(self):
        print ("Start test case for update_modifier_option")
        pass

    def test_update_page(self):
        print ("Start test case for update_page")
        pass

    def test_update_page_cell(self):
        print ("Start test case for update_page_cell")
        pass

    def test_update_variation(self):
        print ("Start test case for update_variation")
        pass


if __name__ == '__main__':
    unittest.main()
