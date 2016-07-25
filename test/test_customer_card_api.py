# coding: utf-8

"""
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import

import os
import sys
import unittest

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.customer_card_api import CustomerCardApi


class TestCustomerCardApi(unittest.TestCase):
    """ CustomerCardApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.customer_card_api.CustomerCardApi()

    def tearDown(self):
        pass

    def test_create_customer_card(self):
        """
        Test case for create_customer_card

        CreateCustomerCard
        """
        pass

    def test_delete_customer_card(self):
        """
        Test case for delete_customer_card

        DeleteCustomerCard
        """
        pass


if __name__ == '__main__':
    unittest.main()