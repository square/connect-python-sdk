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
from nose.tools import set_trace
from datetime import datetime

import faker
import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.customers_api import CustomersApi
from squareconnect.models.create_customer_request import CreateCustomerRequest
from squareconnect.models.customer import Customer
from .utils import APITestCase

class TestCustomersApi(APITestCase):
    """ CustomersApi unit test stubs """

    def setUp(self):
        self.fake = faker.Faker()
        self.api = squareconnect.apis.customers_api.CustomersApi()
        account = self.accounts['US-Prod-Sandbox']
        self.api.api_client.configuration.access_token = account['access_token']

    def tearDown(self):
        pass

    def new_customer(self):
        return Customer(
            given_name=self.fake.first_name(),
            family_name=self.fake.last_name(),
            company_name=self.fake.company(),
            email_address=self.fake.email(),
            phone_number=self.fake.phone_number(),
            address=self.fake.address(),
            note=self.fake.uuid4(),
            reference_id=self.fake.uuid4())

    def test_create_customer(self):
        customer = self.new_customer()
        customer_data = customer.to_dict()

        shared_attributes = [
            'given_name', 'family_name', 'company_name', 'email_address',
            'phone_number', 'note', 'reference_id']

        payload = {
            attribute: customer_data.get(attribute)
            for attribute in shared_attributes
        }

        response = self.api.create_customer(CreateCustomerRequest(**payload))
        response_customer_data = response.customer.to_dict()

        for attribute in shared_attributes:
            self.assertEqual(response_customer_data.get(attribute),
                customer_data.get(attribute))

    def test_create_customer_card(self):
        print ("Start test case for create_customer_card")
        pass

    def test_delete_customer(self):
        print ("Start test case for delete_customer")
        pass

    def test_delete_customer_card(self):
        print ("Start test case for delete_customer_card")
        pass

    def test_list_customers(self):
        print ("Start test case for list_customers")
        response = self.api.list_customers()
        self.assertTrue(response.customers)
        self.assertFalse(response.errors)

    def test_list_customer_sort_alphabetically(self):
        response = self.api.list_customers(sort_order='ASC')
        previous_customer = response.customers[0]
        for customer in response.customers[1:]:
            self.assertTrue(get_default_sort_key(previous_customer) <= get_default_sort_key(customer))
            previous_customer = customer

    def test_list_customer_sort_alphabetically_descending(self):
        response = self.api.list_customers(sort_order='DESC')
        previous_customer = response.customers[0]
        for customer in response.customers[1:]:
            self.assertTrue(get_default_sort_key(previous_customer) >= get_default_sort_key(customer))
            previous_customer = customer

    def test_list_customer_sort_created_at_ascending(self):
        response = self.api.list_customers(sort_field='CREATED_AT', sort_order='ASC')
        previous_customer = response.customers[0]
        for customer in response.customers[1:]:
            self.assertTrue(get_datetime(previous_customer.created_at) <= get_datetime(customer.created_at))
            previous_customer = customer

    def test_list_customer_sort_created_at_descending(self):
        response = self.api.list_customers(sort_field='CREATED_AT', sort_order='DESC')
        previous_customer = response.customers[0]
        for customer in response.customers[1:]:
            self.assertTrue(get_datetime(previous_customer.created_at) >= get_datetime(customer.created_at))
            previous_customer = customer

    def test_retrieve_customer(self):
        print ("Start test case for retrieve_customer")
        pass

    def test_update_customer(self):
        print ("Start test case for update_customer")
        pass


def get_datetime(date):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')


def get_default_sort_key(customer):
    """Create the default sort key for a customer.

    Args:
        customer: the customer to create the default sort key.

    Return:
        the sort key.
    """
    return (
        not bool(customer.given_name or customer.family_name),
        ((customer.given_name or '') + (customer.family_name or '')).strip(),
        bool(customer.company_name),
        (customer.company_name or ''))

if __name__ == '__main__':
    unittest.main()
