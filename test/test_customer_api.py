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
from squareconnect.apis.customer_api import CustomerApi
from squareconnect.models.customer import Customer

from .utils import APITestCase


class TestCustomerApi(APITestCase):
    """ CustomerApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.customer_api.CustomerApi()
        self.account = self.accounts['US-Prod-Sandbox']
        self.access_token = self.account['access_token']

    def tearDown(self):
        pass

    def test01_create_customer(self):
        print ('Start test case for create_customer')

        body = {
            'given_name':"Guido", 
            'family_name':"Rossum", 
            'reference_id':"python21"
        }
        resp = self.api.create_customer(self.access_token, body)
        self.assertIsNone(resp.errors, "Errors in the result.")

        self.__class__.customer = resp.customer
        expected_customer = Customer(given_name="Guido", family_name="Rossum", reference_id="python21")
        self.validate_customer_equality(resp.customer, expected_customer)

    def test02_retrieve_customer(self):
        print ('Start test case for retrieve_customer')

        customer_id = self.__class__.customer.id
        response = self.api.retrieve_customer(self.access_token, customer_id)
        self.assertIsNone(response.errors)
   
    def test03_update_customer(self):
        print ('Start test case for update_customer')

        customer_id = self.__class__.customer.id
        body = {'given_name': "Van"}
        response = self.api.update_customer(self.access_token, customer_id, body)
        self.assertIsNone(response.errors)

        expected_customer = Customer(given_name="Van", family_name="Rossum", reference_id="python21")
        self.validate_customer_equality(response.customer, expected_customer)

    def test04_list_customers(self):
        print ('Start test case for list_customers')
        
        response = self.api.list_customers(authorization=self.access_token)
        self.assertIsNone(response.errors)

        # Second request with previous cursor
        if response.cursor is not None:
          response = self.api.list_customers(authorization, cursor=response.cursor)
          self.assertIsNone(response.errors)

    def test07_delete_customer(self):
        print ('Start test case for delete_customer')
        customer_id = self.__class__.customer.id
        response = self.api.delete_customer(self.access_token, customer_id)
        self.assertIsNone(response.errors)


    def validate_customer_equality(self, actual, expected):
        self.assertEqual(actual.given_name, expected.given_name, 
          "expected: %s ,but got: %s " % (expected.given_name, actual.given_name))
        self.assertEqual(actual.family_name, expected.family_name, 
          "expected: %s ,but got: %s " % (expected.family_name, actual.family_name))
        self.assertEqual(actual.reference_id, expected.reference_id, 
          "expected: %s ,but got: %s " % (expected.reference_id, actual.reference_id))

if __name__ == '__main__':
    unittest.main()
