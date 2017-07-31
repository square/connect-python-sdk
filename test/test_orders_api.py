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
from squareconnect.apis.orders_api import OrdersApi
from squareconnect.apis.catalog_api import CatalogApi
from squareconnect.models import CreateOrderRequestLineItem, CreateOrderRequest, CreateOrderRequestModifier, CreateOrderRequestDiscount
from squareconnect.models import CreateOrderRequestTax, Money, OrderLineItem, Order
from squareconnect.models import OrderLineItemModifier, OrderLineItemTax, OrderLineItemDiscount
from .utils import APITestCase, CatalogFixture


class TestOrdersApi(APITestCase):

    def setUp(self):
        account = self.accounts['US-Prod']
        access_token = account['access_token']
        squareconnect.configuration.access_token = access_token
        self.api = OrdersApi()
        self.location_id = account['location_id']
        self.catalog_api = CatalogApi()
        self.catalog_fixture = CatalogFixture(self.catalog_api)


    def test_create_order(self):
        request = CreateOrderRequest(
            idempotency_key=str(uuid.uuid1()),
            reference_id='order ref id',
            line_items=[
                CreateOrderRequestLineItem(
                    name='Espresso',
                    quantity='2',
                    note='some note',
                    base_price_money=Money(
                        amount=200,
                        currency='USD'
                    )
                )
            ]
        )
        response = self.api.create_order(self.location_id, request)
        self.assertIsNone(response.errors)

        subject = response.order
        expected = Order(
            id=subject.id,
            location_id=self.location_id,
            reference_id='order ref id',
            line_items=[
                OrderLineItem(
                    name='Espresso',
                    quantity='2',
                    note='some note',
                    base_price_money=Money(amount=200, currency='USD'),
                    gross_sales_money=Money(amount=400, currency='USD'),
                    total_discount_money=Money(amount=0, currency="USD"),
                    total_money=Money(amount=400, currency="USD"),
                    total_tax_money=Money(amount=0, currency="USD"),
                )
            ],
            total_discount_money=Money(amount=0, currency="USD"),
            total_money=Money(amount=400, currency="USD"),
            total_tax_money=Money(amount=0, currency="USD"),
        )
        self.assertEqual(subject, expected)

    def test_create_order_with_catalog_objects(self):
        large_coffee_id = self.catalog_fixture.large_coffee_id()
        soy_milk_id = self.catalog_fixture.soy_milk_id()
        amount_discount_id = self.catalog_fixture.amount_discount_id()
        sales_tax_id = self.catalog_fixture.sales_tax_id()

        request = CreateOrderRequest(
            idempotency_key=str(uuid.uuid1()),
            reference_id='order ref id with catalog',
            line_items=[
                CreateOrderRequestLineItem(
                    catalog_object_id=large_coffee_id,
                    quantity='2',
                    modifiers=[
                        CreateOrderRequestModifier(
                            catalog_object_id=soy_milk_id
                        )
                    ],
                    discounts=[
                        CreateOrderRequestDiscount(
                            catalog_object_id=amount_discount_id
                        )
                    ],
                    taxes=[
                        CreateOrderRequestTax(
                            catalog_object_id=sales_tax_id
                        )
                    ]
                )
            ]
        )
        response = self.api.create_order(self.location_id, request)
        self.assertIsNone(response.errors)

        subject = response.order
        expected = Order(
            id=subject.id,
            location_id=self.location_id,
            reference_id='order ref id with catalog',
            line_items=[
                OrderLineItem(
                    catalog_object_id=large_coffee_id,
                    name='Coffee',
                    quantity='2',
                    variation_name='Large',
                    modifiers=[
                        OrderLineItemModifier(
                            catalog_object_id=soy_milk_id,
                            name='Soy Milk',
                            base_price_money=Money(amount=50, currency='USD'),
                            total_price_money=Money(amount=100, currency='USD') # $0.50 * 2
                        )
                    ],
                    taxes=[
                        OrderLineItemTax(
                            catalog_object_id=sales_tax_id,
                            name='Sales Tax',
                            type='ADDITIVE',
                            percentage='5.0',
                            # ((($2.50 + $0.50) * 2) - $0.50) * 5% = $0.28
                            applied_money=Money(amount=28, currency='USD'),
                        )
                    ],
                    discounts=[
                        OrderLineItemDiscount(
                            catalog_object_id=amount_discount_id,
                            name='50 cents off',
                            type='FIXED_AMOUNT',
                            amount_money=Money(amount=50, currency='USD'),
                            applied_money=Money(amount=50, currency='USD'),
                            scope='LINE_ITEM'
                      )
                    ],
                    base_price_money=Money(amount=250, currency='USD'),
                    gross_sales_money=Money(amount=600, currency='USD'),
                    total_discount_money=Money(amount=50, currency="USD"),
                    total_money=Money(amount=578, currency="USD"),
                    # ($6 - $0.50) *  5% additive = $0.28
                    total_tax_money=Money(amount=28, currency="USD"),
                )
            ],
            total_discount_money=Money(amount=50, currency="USD"),
            total_money=Money(amount=578, currency="USD"),
            total_tax_money=Money(amount=28, currency="USD"),
        )
        self.assertEqual(subject, expected)

