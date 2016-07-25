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
from squareconnect.apis.customer_api import CustomerApi as CustomerApi
from squareconnect.api_client import ApiClient as ApiClient
from squareconnect.models.create_customer_request import CreateCustomerRequest as CreateCustomerRequest
from squareconnect.models.customer import Customer as Customer

import global_setup

class TestCustomerApi(unittest.TestCase):
    """ CustomerApi unit test stubs """
    @classmethod
    def setUpClass(self):
        host_name = global_setup.host_name
        api_client = ApiClient(host=host_name)
        self.access_token = global_setup.account['accessToken']
        self.client_id = global_setup.account['applicationId']
        self.api = CustomerApi(api_client)

    def tearDown(self):
        pass

    def test01_create_customer(self):
        print "Start test case for create_customer"

        body = CreateCustomerRequest(given_name="Guido", family_name="Rossum", reference_id="python21")
        authorization = self.access_token
        response = self.api.create_customer(authorization, body)
        self.assertIsInstance()
        TestCustomerApi.customer = response.customer
        expected_customer = Customer(given_name="Guido", family_name="Rossum", reference_id="python21")
        self.validate_customer_equality(response.customer, expected_customer)

    def test02_retrieve_customer(self):
        print "Start test case for retrieve_customer"
        authorization = self.access_token
        customer_id = TestCustomerApi.customer.id
        response = self.api.retrieve_customer(authorization, customer_id)
        pass

    def test03_update_customer(self):
        print "Start test case for update_customer"
        pass

    def test04_list_customers(self):
        print "Start test case for list_customers"
        pass
       
    def test05_delete_customer(self):
        print "Start test case for delete_customer"

        authorization = self.access_token
        customer_id = TestCustomerApi.customer.id
        response = self.api.delete_customer(authorization, customer_id)

    def validate_customer_equality(self, actual, expected):
        self.assertEqual(actual.given_name, expected.given_name, 
          "expected: %s ,but got: %s " % (expected.given_name, actual.given_name))
        self.assertEqual(actual.family_name, expected.family_name, 
          "expected: %s ,but got: %s " % (expected.family_name, actual.family_name))
        self.assertEqual(actual.reference_id, expected.reference_id, 
          "expected: %s ,but got: %s " % (expected.reference_id, actual.reference_id))

if __name__ == '__main__':
    unittest.main()