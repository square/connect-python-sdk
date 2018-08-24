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
from squareconnect.apis.reporting_api import ReportingApi
from .utils import APITestCase


class TestReportingApi(APITestCase):
    """ ReportingApi unit test stubs """

    def setUp(self):
        account = self.accounts['US-Prod']
        self.api = squareconnect.apis.ReportingApi()
        self.api.api_client.configuration.access_token = account['access_token']
        self.location_id = account['location_id']

    def test_list_additional_recipient_receivable_refunds(self):
        try:
            self.api.list_additional_recipient_receivable_refunds(self.location_id)
        except ApiException as e:
            self.fail("unexpected ApiException: %s" % e)

    def test_list_additional_recipient_receivables(self):
        try:
            self.api.list_additional_recipient_receivables(self.location_id)
        except ApiException as e:
            self.fail("unexpected ApiException: %s" % e)


if __name__ == '__main__':
    unittest.main()
