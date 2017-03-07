# Square Connect V2 Python SDK [![Build Status](https://travis-ci.org/square/connect-python-sdk.svg?branch=master)](https://travis-ci.org/square/connect-python-sdk)[![PyPI version](https://badge.fury.io/py/squareconnect.svg)](https://badge.fury.io/py/squareconnect)

This repository contains the released Python client SDK. Check out our [API
specification repository](https://github.com/square/connect-api-specification)
for the specification and template files we used to generate this.

## Requirements.

Make sure you have Python 2 >=2.7.9 or Python 3 >= 3.4

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/square/connect-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/square/connect-python-sdk.git`)

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Getting Started


Please follow the [installation procedure](#installation--usage):

Then import the package:
```python
import squareconnect
```

### Retrieve your location IDs
```python
from __future__ import print_function 

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.location_api import LocationApi

# create an instance of the Location API class
api_instance = LocationApi()
access_token = 'YOUR_ACCESS_TOKEN' 

try:
    # ListLocations
    api_response = api_instance.list_locations(access_token)
    print (api_response.locations)
except ApiException as e:
    print ('Exception when calling LocationApi->list_locations: %s\n' % e)

```
### Charge the card nonce
```python
from __future__ import print_function 
import uuid

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.transaction_api import TransactionApi

# create an instance of the Transaction API class
api_instance = TransactionApi()
access_token = 'YOUR_ACCESS_TOKEN'
location_id = 'YOUR_LOCATION_ID' 
nonce = 'YOUR_NONCE' 

try:
    # Charge
    idempotency_key = str(uuid.uuid1())
    amount = {'amount': 100, 'currency': 'USD'}
    body = {'idempotency_key': idempotency_key, 'card_nonce': nonce, 'amount_money': amount}
    api_response = api_instance.charge(access_token, location_id, body)
    print (api_response.transaction)
except ApiException as e:
    print ('Exception when calling TransactionApi->charge: %s\n' % e)

```

## Documentation for API Endpoints

All URIs are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Class | Method | HTTP request 
------------ | ------------- | ------------- 
*CheckoutApi* | [**create_checkout**](docs/CheckoutApi.md#create_checkout) | **POST** /v2/locations/{location_id}/checkouts
*CustomerApi* | [**create_customer**](docs/CustomerApi.md#create_customer) | **POST** /v2/customers
*CustomerApi* | [**delete_customer**](docs/CustomerApi.md#delete_customer) | **DELETE** /v2/customers/{customer_id}
*CustomerApi* | [**list_customers**](docs/CustomerApi.md#list_customers) | **GET** /v2/customers
*CustomerApi* | [**retrieve_customer**](docs/CustomerApi.md#retrieve_customer) | **GET** /v2/customers/{customer_id}
*CustomerApi* | [**update_customer**](docs/CustomerApi.md#update_customer) | **PUT** /v2/customers/{customer_id}
*CustomerCardApi* | [**create_customer_card**](docs/CustomerCardApi.md#create_customer_card) | **POST** /v2/customers/{customer_id}/cards
*CustomerCardApi* | [**delete_customer_card**](docs/CustomerCardApi.md#delete_customer_card) | **DELETE** /v2/customers/{customer_id}/cards/{card_id}
*LocationApi* | [**list_locations**](docs/LocationApi.md#list_locations) | **GET** /v2/locations
*RefundApi* | [**create_refund**](docs/RefundApi.md#create_refund) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/refund
*RefundApi* | [**list_refunds**](docs/RefundApi.md#list_refunds) | **GET** /v2/locations/{location_id}/refunds
*TransactionApi* | [**capture_transaction**](docs/TransactionApi.md#capture_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/capture
*TransactionApi* | [**charge**](docs/TransactionApi.md#charge) | **POST** /v2/locations/{location_id}/transactions
*TransactionApi* | [**list_transactions**](docs/TransactionApi.md#list_transactions) | **GET** /v2/locations/{location_id}/transactions
*TransactionApi* | [**retrieve_transaction**](docs/TransactionApi.md#retrieve_transaction) | **GET** /v2/locations/{location_id}/transactions/{transaction_id}
*TransactionApi* | [**void_transaction**](docs/TransactionApi.md#void_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/void


## Documentation For Models

 - [Address](docs/Address.md)
 - [CaptureTransactionRequest](docs/CaptureTransactionRequest.md)
 - [CaptureTransactionResponse](docs/CaptureTransactionResponse.md)
 - [Card](docs/Card.md)
 - [ChargeRequest](docs/ChargeRequest.md)
 - [ChargeResponse](docs/ChargeResponse.md)
 - [Checkout](docs/Checkout.md)
 - [CreateCheckoutRequest](docs/CreateCheckoutRequest.md)
 - [CreateCheckoutResponse](docs/CreateCheckoutResponse.md)
 - [CreateCustomerCardRequest](docs/CreateCustomerCardRequest.md)
 - [CreateCustomerCardResponse](docs/CreateCustomerCardResponse.md)
 - [CreateCustomerRequest](docs/CreateCustomerRequest.md)
 - [CreateCustomerResponse](docs/CreateCustomerResponse.md)
 - [CreateOrderRequest](docs/CreateOrderRequest.md)
 - [CreateOrderRequestLineItem](docs/CreateOrderRequestLineItem.md)
 - [CreateOrderRequestOrder](docs/CreateOrderRequestOrder.md)
 - [CreateRefundRequest](docs/CreateRefundRequest.md)
 - [CreateRefundResponse](docs/CreateRefundResponse.md)
 - [Customer](docs/Customer.md)
 - [CustomerGroupInfo](docs/CustomerGroupInfo.md)
 - [CustomerPreferences](docs/CustomerPreferences.md)
 - [DeleteCustomerCardRequest](docs/DeleteCustomerCardRequest.md)
 - [DeleteCustomerCardResponse](docs/DeleteCustomerCardResponse.md)
 - [DeleteCustomerRequest](docs/DeleteCustomerRequest.md)
 - [DeleteCustomerResponse](docs/DeleteCustomerResponse.md)
 - [Error](docs/Error.md)
 - [ListCustomersRequest](docs/ListCustomersRequest.md)
 - [ListCustomersResponse](docs/ListCustomersResponse.md)
 - [ListLocationsRequest](docs/ListLocationsRequest.md)
 - [ListLocationsResponse](docs/ListLocationsResponse.md)
 - [ListRefundsRequest](docs/ListRefundsRequest.md)
 - [ListRefundsResponse](docs/ListRefundsResponse.md)
 - [ListTransactionsRequest](docs/ListTransactionsRequest.md)
 - [ListTransactionsResponse](docs/ListTransactionsResponse.md)
 - [Location](docs/Location.md)
 - [Money](docs/Money.md)
 - [Order](docs/Order.md)
 - [OrderLineItem](docs/OrderLineItem.md)
 - [Refund](docs/Refund.md)
 - [RetrieveCustomerRequest](docs/RetrieveCustomerRequest.md)
 - [RetrieveCustomerResponse](docs/RetrieveCustomerResponse.md)
 - [RetrieveTransactionRequest](docs/RetrieveTransactionRequest.md)
 - [RetrieveTransactionResponse](docs/RetrieveTransactionResponse.md)
 - [Tender](docs/Tender.md)
 - [TenderCardDetails](docs/TenderCardDetails.md)
 - [TenderCashDetails](docs/TenderCashDetails.md)
 - [Transaction](docs/Transaction.md)
 - [UpdateCustomerRequest](docs/UpdateCustomerRequest.md)
 - [UpdateCustomerResponse](docs/UpdateCustomerResponse.md)
 - [VoidTransactionRequest](docs/VoidTransactionRequest.md)
 - [VoidTransactionResponse](docs/VoidTransactionResponse.md)


## Documentation For Enums

 - [CardBrand](docs/CardBrand.md)
 - [Country](docs/Country.md)
 - [Currency](docs/Currency.md)
 - [ErrorCategory](docs/ErrorCategory.md)
 - [ErrorCode](docs/ErrorCode.md)
 - [LocationCapability](docs/LocationCapability.md)
 - [RefundStatus](docs/RefundStatus.md)
 - [SortOrder](docs/SortOrder.md)
 - [TenderCardDetailsEntryMethod](docs/TenderCardDetailsEntryMethod.md)
 - [TenderCardDetailsStatus](docs/TenderCardDetailsStatus.md)
 - [TenderType](docs/TenderType.md)
 - [TransactionProduct](docs/TransactionProduct.md)


## Contributing

Send bug reports, feature requests, and code contributions to the [API
specifications repository](https://github.com/square/connect-api-specification),
as this repository contains only the generated SDK code.

## License

```
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
