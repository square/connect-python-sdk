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
from squareconnect.apis.v1_transactions_api import V1TransactionsApi


class TestV1TransactionsApi(unittest.TestCase):
    """ V1TransactionsApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.v1_transactions_api.V1TransactionsApi()

    def tearDown(self):
        pass

    def test_create_refund(self):
        print ("Start test case for create_refund")
        pass

    def test_list_bank_accounts(self):
        print ("Start test case for list_bank_accounts")
        pass

    def test_list_orders(self):
        print ("Start test case for list_orders")
        pass

    def test_list_payments(self):
        print ("Start test case for list_payments")
        pass

    def test_list_refunds(self):
        print ("Start test case for list_refunds")
        pass

    def test_list_settlements(self):
        print ("Start test case for list_settlements")
        pass

    def test_retrieve_bank_account(self):
        print ("Start test case for retrieve_bank_account")
        pass

    def test_retrieve_order(self):
        print ("Start test case for retrieve_order")
        pass

    def test_retrieve_payment(self):
        print ("Start test case for retrieve_payment")
        pass

    def test_retrieve_settlement(self):
        print ("Start test case for retrieve_settlement")
        pass

    def test_update_order(self):
        print ("Start test case for update_order")
        pass


if __name__ == '__main__':
    unittest.main()
