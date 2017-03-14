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
from squareconnect.models.customer import Customer
from squareconnect.apis.customer_api import CustomerApi

from .utils import APITestCase

class TestCustomerApi(APITestCase):

    def setUp(self):
        self.api = squareconnect.apis.customer_api.CustomerApi()

    def tearDown(self):
        pass

    def test01_create_customer(self):
        print ("Start test case for create_customer")

        body = {
            'given_name':"Friendly", 
            'family_name':"Sparks", 
            'reference_id':"ontour34"
        }
        account = self.accounts['US-Prod-Sandbox']
        authorization = account['access_token']
        result = self.api.create_customer(authorization, body)
        self.__class__.customer = result.customer
        self.assertIsNone(result.errors)

        self.assertIsInstance(result.customer, Customer, "Result instance is not instance of Customer.")
        self.assertEqual(result.customer.given_name, "Friendly", "Given name doesn't match.")
        self.assertEqual(result.customer.family_name, "Sparks", "Family name doesn't match.")
        self.assertEqual(result.customer.reference_id, "ontour34", "reference_id name doesn't match.")

    def test02_retrieve_customer(self):
        print ("Start test case for retrieve_customer")
        account = self.accounts['US-Prod-Sandbox']
        authorization = account['access_token']
        customer_id = self.__class__.customer.id
        result = self.api.retrieve_customer(authorization, customer_id)
        self.assertIsNone(result.errors)

        self.assertIsInstance(result.customer, Customer, "Result instance is not instance of Customer.")
        self.assertEqual(result.customer.given_name, "Friendly", "Given name doesn't match.")
        self.assertEqual(result.customer.family_name, "Sparks", "Family name doesn't match.")
        self.assertEqual(result.customer.reference_id, "ontour34", "reference_id name doesn't match.")

    def test03_list_customers(self):
        print ('Start test case for list_customers')
        # Problem in retrieve a large list of customers
        account = self.accounts['US-Prod-Sandbox']       
        authorization = account['access_token']
        result = self.api.list_customers(authorization=authorization)
        self.assertIsNone(result.errors)

        # Second request with previous cursor
        if result.cursor is not None:
          result = self.customer_api.list_customers(authorization, cursor=result.cursor)
          self.assertIsNone(result.errors)

    def test_update_customer(self):
        print ("Start test case for update_customer")
        pass

    def test04_delete_customer(self):
        print ('Start test case for delete_customer')
        account = self.accounts['US-Prod-Sandbox']
        authorization = account['access_token']
        customer_id = self.__class__.customer.id
        result = self.api.delete_customer(authorization, customer_id)
        self.assertIsNone(result.errors)


if __name__ == '__main__':
    unittest.main()
