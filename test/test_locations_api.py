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
from squareconnect.apis.locations_api import LocationsApi
from squareconnect.models.location import Location

from .utils import APITestCase

class TestLocationsApi(APITestCase):
    """ LocationsApi unit test stubs """

    def setUp(self):
        account = self.accounts['US-Prod-Sandbox']
        access_token = account['access_token']
        squareconnect.configuration.access_token = access_token
        self.api = squareconnect.apis.locations_api.LocationsApi()

    def tearDown(self):
        pass

    def test_list_locations(self):
        print ("Start test case for list_locations")
        result = self.api.list_locations()
        self.assertIsNone(result.errors, "Errors in the result.")
        self.assertGreater(len(result.locations), 0, "Empty location list.")
        first_location = result.locations[0]
        self.assertIsInstance(first_location, Location, "Result instance is not instance of Location.")
        self.assertEqual(first_location.id, "CBASEEffqN8pnVNXwoCL0dSGMVAgAQ", "First location id doesn't match.")
        pass


if __name__ == '__main__':
    unittest.main()
