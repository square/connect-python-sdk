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

import uuid
import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.checkout_api import CheckoutApi
from squareconnect.models import CreateCheckoutRequest, CreateOrderRequestLineItem, CreateOrderRequest, Money
from squareconnect.models import CreateOrderRequestDiscount, CreateOrderRequestTax, Address
from .utils import APITestCase


class TestCheckoutApi(APITestCase):
    """ CheckoutApi unit test stubs """

    def setUp(self):
        account = self.accounts['US-Prod-Sandbox']
        self.api = squareconnect.apis.checkout_api.CheckoutApi()
        self.api.api_client.configuration.access_token = account['access_token']
        self.location_id = account['location_id']

    def test_create_checkout(self):
        body = CreateCheckoutRequest(
            idempotency_key=str(uuid.uuid1()),
            order=CreateOrderRequest(
                reference_id= "reference_id",
                line_items=[
                    CreateOrderRequestLineItem(
                        name="Printed T Shirt",
                        quantity="2",
                        base_price_money=Money(
                            amount=1500,
                            currency="USD"
                        ),
                        discounts=[
                            CreateOrderRequestDiscount(
                                name="7% off previous season item",
                                percentage="7"
                            ),
                            CreateOrderRequestDiscount(
                                name="$3 off Customer Discount",
                                amount_money=Money(
                                    amount=300,
                                    currency="USD"
                                )
                            )
                        ]
                    ),
                    CreateOrderRequestLineItem(
                        name="Slim Jeans",
                        quantity="1",
                        base_price_money=Money(
                            amount=2500,
                            currency="USD"
                        )
                    ),
                    CreateOrderRequestLineItem(
                        name="Woven Sweater",
                        quantity="3",
                        base_price_money=Money(
                            amount=3500,
                            currency="USD"
                        ),
                        discounts=[
                            CreateOrderRequestDiscount(
                                name="$11 off Customer Discount",
                                amount_money=Money(
                                    amount=1100,
                                    currency="USD"
                                )
                            )
                        ],
                        taxes=[
                            CreateOrderRequestTax(
                                name="Fair Trade Tax",
                                percentage="5"
                            )
                        ]

                    )
                ],
                discounts=[
                    CreateOrderRequestDiscount(
                        name="Father's day 12% OFF",
                        percentage="12"
                    ),
                    CreateOrderRequestDiscount(
                        name="Global Sales $55 OFF",
                        amount_money=Money(
                            amount=5500,
                            currency="USD"
                        )
                    )
                ],
                taxes=[
                    CreateOrderRequestTax(
                        name="Sales Tax",
                        percentage="8.5"
                    )
                ]
            ),
            ask_for_shipping_address=True,
            merchant_support_email="merchant+support@website.com",
            pre_populate_buyer_email="example@email.com",
            pre_populate_shipping_address=Address(
                address_line_1="1455 Market St.",
                address_line_2="Suite 600",
                locality="San Francisco",
                administrative_district_level_1="CA",
                postal_code="94103",
                country="US",
                first_name="Jane",
                last_name="Doe"
            ),
            redirect_url="https://docs.connect.squareup.com/order-confirm"
        )

        response = self.api.create_checkout(self.location_id, body)

        self.assertIsNone(response.errors)
        self.assertTrue(response.checkout.checkout_page_url.startswith('https://connect.'))


if __name__ == '__main__':
    unittest.main()
