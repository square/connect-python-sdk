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
from datetime import timedelta, datetime
from operator import attrgetter
import time

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.models.transaction import Transaction
from squareconnect.apis.transaction_api import TransactionApi

from .utils import APITestCase

class TestTransactionApi(APITestCase):

    def setUp(self):
        self.api = squareconnect.apis.transaction_api.TransactionApi()
        self.currency = 'USD'
        self.transaction_api = TransactionApi()
        self.location_id = 'CBASEEffqN8pnVNXwoCL0dSGMVAgAQ'
        self.sleepTime = 20

    def tearDown(self):
        pass

    def test01_charge(self):
        print ("Start test case for charge")
        idempotency_key = str(uuid.uuid1())
        nonce = 'fake-card-nonce-ok'
        amount = {
            'amount': 2000, 
            'currency': self.currency
        }
        account = self.accounts['US-Prod-Sandbox']
        authorization = account['access_token']
        body = {
            'idempotency_key': idempotency_key, 
            'card_nonce': nonce
        }
        self.assertRaises(ApiException, self.transaction_api.charge, authorization, self.location_id, body)
        body = {
            'amount_money': amount, 
            'card_nonce':nonce
        }
        self.assertRaises(ApiException, self.transaction_api.charge, authorization, self.location_id, body)

        body = {
            'idempotency_key': idempotency_key, 
            'amount_money': amount
        }
        self.assertRaises(ApiException, self.transaction_api.charge, authorization, self.location_id, body)

        # Expected Success tests
        # The idempotence key can only be retried with the same request data.
        idempotency_key = str(uuid.uuid1())
        body = {
            'idempotency_key': idempotency_key, 
            'card_nonce': nonce, 
            'amount_money': amount
        }
        response = self.transaction_api.charge(authorization, self.location_id, body)
        self.assertIsNone(response.errors)
        
        TestTransactionApi.transaction = response.transaction
        # Try a transaction 3 times and assert that only one unique transaction
        # was created.
        retried_charges = []
        for i in range(0,3):
            resp = self.transaction_api.charge(authorization, self.location_id, body)
            retried_charges.append(resp)
        
        transaction_ids = {resp.transaction.id for resp in retried_charges}
        self.assertEqual(len(transaction_ids), 1)
        self.assertEqual(TestTransactionApi.transaction.tenders[0].id, 
                        retried_charges[0].transaction.tenders[0].id)        
        # Test the new created transaction can be obtained from ListTransactions endpoint.
        # Sleep for 3 seconds because of the delay of processing the transaction
        time.sleep(self.sleepTime)
        cursor = None
        d =  datetime.now() - timedelta(0.5)
        begin_time = d.isoformat("T") + "Z"
        transaction_ids = []
        while True:
            list_transactions_response = self.transaction_api.list_transactions(authorization=authorization, 
                                                                              location_id=self.location_id,
                                                                              cursor=cursor,
                                                                              begin_time=begin_time)
            cursor = list_transactions_response.cursor
            ids = map(attrgetter('_id'), list_transactions_response.transactions)
            transaction_ids.extend(ids)
            if cursor is None:
                break

        self.assertIn(TestTransactionApi.transaction.id, transaction_ids)

    def test02_retrieve_transaction(self):
        print ('Start test case for retrieve_transaction')
        account = self.accounts['US-Prod-Sandbox']
        authorization = account['access_token']
        response = self.transaction_api.retrieve_transaction(authorization, 
                    self.location_id, TestTransactionApi.transaction.id)
        self.assertIsNone(response.errors)

        expected = TestTransactionApi.transaction
        retrieved = response.transaction
        self.assertEqual(expected.id, retrieved.id)
        self.assertEqual(expected.tenders[0].amount_money, retrieved.tenders[0].amount_money)

    def test03_list_transactions(self):
        print ('Start test case for list_transactions')
        account = self.accounts['US-Prod-Sandbox']
        authorization = account['access_token']
        location_id = self.location_id
        self.assertRaises(ValueError, self.transaction_api.list_transactions, authorization, None)
        self.assertRaises(ValueError, self.transaction_api.list_transactions, None, self.location_id)
        self.assertRaises(ApiException, self.transaction_api.list_transactions, authorization=authorization, location_id='')

        response = self.transaction_api.list_transactions(authorization, self.location_id)
        self.assertIsNone(response.errors)

        transactions = response.transactions
        cursor = response.cursor
        #print ('cursor: %s' % (cursor))
        if cursor is not None:
          list_transactions_response = self.transaction_api.list_transactions(authorization=authorization, 
                                                                              location_id=self.location_id, 
                                                                              cursor=cursor)
          if list_transactions_response.transactions is not None:
            for t in list_transactions_response.transactions:
              self.assertNotIn(t, transactions)

    def test04_capture_transaction(self):
        print ('Start test case for capture_trasaction')
        account = self.accounts['US-Prod-Sandbox']
        authorization = account['access_token']
        idempotency_key = str(uuid.uuid1())
        nonce = 'fake-card-nonce-ok'
        amount = {
            'amount': 2000, 
            'currency': self.currency
        }
        body = {
            'idempotency_key': idempotency_key, 
            'card_nonce': nonce, 
            'amount_money': amount, 
            'delay_capture': True
        }
        charge_response = self.transaction_api.charge(authorization, self.location_id, body)
        
        transaction_id = charge_response.transaction.id
        response = self.transaction_api.capture_transaction(authorization, self.location_id, transaction_id)
        self.assertIsNone(response.errors)
        # The tender card status of the charge above should be 
        # `Captured` in the RetrieveTransaction response.
        time.sleep(self.sleepTime)
        retrieved = self.transaction_api.retrieve_transaction(authorization, self.location_id, 
                                                              transaction_id)
        self.assertEqual("CAPTURED", retrieved.transaction.tenders[0].card_details.status)

    def test05_void_transaction(self):
        print ('Start test case for void_transaction')
        account = self.accounts['US-Prod-Sandbox']
        authorization = account['access_token']
        idempotency_key = str(uuid.uuid1())
        nonce = 'fake-card-nonce-ok'
        amount = {
            'amount': 2000,
            'currency': self.currency
        }
        body = {
            'idempotency_key': idempotency_key, 'card_nonce': nonce, 
            'amount_money': amount, 'delay_capture': True
        }
        charge_response = self.transaction_api.charge(authorization, self.location_id, body)
        
        transaction_id = charge_response.transaction.id
        response = self.transaction_api.void_transaction(authorization, self.location_id, transaction_id)
        self.assertIsNone(response.errors)

        time.sleep(self.sleepTime)
        retrieved = self.transaction_api.retrieve_transaction(authorization, self.location_id, 
                                                              transaction_id)
        self.assertEqual("VOIDED", retrieved.transaction.tenders[0].card_details.status)


if __name__ == '__main__':
    unittest.main()
