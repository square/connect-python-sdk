# Square Connect Python SDK [![Build Status](https://travis-ci.org/square/connect-python-sdk.svg?branch=master)](https://travis-ci.org/square/connect-python-sdk)[![PyPI version](https://badge.fury.io/py/squareconnect.svg)](https://badge.fury.io/py/squareconnect)

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

# setup authorization
squareconnect.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the Location API class
api_instance = LocationApi()

try:
    # ListLocations
    api_response = api_instance.list_locations()
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

# setup authorization
squareconnect.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the Transaction API class
api_instance = TransactionApi()
location_id = 'YOUR_LOCATION_ID' 
nonce = 'YOUR_NONCE' 

try:
    # Charge
    idempotency_key = str(uuid.uuid1())
    amount = {'amount': 100, 'currency': 'USD'}
    body = {'idempotency_key': idempotency_key, 'card_nonce': nonce, 'amount_money': amount}
    api_response = api_instance.charge(location_id, body)
    print (api_response.transaction)
except ApiException as e:
    print ('Exception when calling TransactionApi->charge: %s\n' % e)

```

## Documentation for API Endpoints

All URIs are relative to [Square Connect Documentation](https://docs.connect.squareup.com/)


Class | Method | HTTP request 
------------ | ------------- | ------------- 
*CatalogApi* | [**batch_delete_catalog_objects**](docs/CatalogApi.md#batch_delete_catalog_objects) | **POST** /v2/catalog/batch-delete
*CatalogApi* | [**batch_retrieve_catalog_objects**](docs/CatalogApi.md#batch_retrieve_catalog_objects) | **POST** /v2/catalog/batch-retrieve
*CatalogApi* | [**batch_upsert_catalog_objects**](docs/CatalogApi.md#batch_upsert_catalog_objects) | **POST** /v2/catalog/batch-upsert
*CatalogApi* | [**catalog_info**](docs/CatalogApi.md#catalog_info) | **GET** /v2/catalog/info
*CatalogApi* | [**delete_catalog_object**](docs/CatalogApi.md#delete_catalog_object) | **DELETE** /v2/catalog/object/{object_id}
*CatalogApi* | [**list_catalog**](docs/CatalogApi.md#list_catalog) | **GET** /v2/catalog/list
*CatalogApi* | [**retrieve_catalog_object**](docs/CatalogApi.md#retrieve_catalog_object) | **GET** /v2/catalog/object/{object_id}
*CatalogApi* | [**search_catalog_objects**](docs/CatalogApi.md#search_catalog_objects) | **POST** /v2/catalog/search
*CatalogApi* | [**update_item_modifier_lists**](docs/CatalogApi.md#update_item_modifier_lists) | **POST** /v2/catalog/update-item-modifier-lists
*CatalogApi* | [**update_item_taxes**](docs/CatalogApi.md#update_item_taxes) | **POST** /v2/catalog/update-item-taxes
*CatalogApi* | [**upsert_catalog_object**](docs/CatalogApi.md#upsert_catalog_object) | **POST** /v2/catalog/object
*CheckoutApi* | [**create_checkout**](docs/CheckoutApi.md#create_checkout) | **POST** /v2/locations/{location_id}/checkouts
*CustomersApi* | [**create_customer**](docs/CustomersApi.md#create_customer) | **POST** /v2/customers
*CustomersApi* | [**create_customer_card**](docs/CustomersApi.md#create_customer_card) | **POST** /v2/customers/{customer_id}/cards
*CustomersApi* | [**delete_customer**](docs/CustomersApi.md#delete_customer) | **DELETE** /v2/customers/{customer_id}
*CustomersApi* | [**delete_customer_card**](docs/CustomersApi.md#delete_customer_card) | **DELETE** /v2/customers/{customer_id}/cards/{card_id}
*CustomersApi* | [**list_customers**](docs/CustomersApi.md#list_customers) | **GET** /v2/customers
*CustomersApi* | [**retrieve_customer**](docs/CustomersApi.md#retrieve_customer) | **GET** /v2/customers/{customer_id}
*CustomersApi* | [**update_customer**](docs/CustomersApi.md#update_customer) | **PUT** /v2/customers/{customer_id}
*LocationsApi* | [**list_locations**](docs/LocationsApi.md#list_locations) | **GET** /v2/locations
*TransactionsApi* | [**capture_transaction**](docs/TransactionsApi.md#capture_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/capture
*TransactionsApi* | [**charge**](docs/TransactionsApi.md#charge) | **POST** /v2/locations/{location_id}/transactions
*TransactionsApi* | [**create_refund**](docs/TransactionsApi.md#create_refund) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/refund
*TransactionsApi* | [**list_refunds**](docs/TransactionsApi.md#list_refunds) | **GET** /v2/locations/{location_id}/refunds
*TransactionsApi* | [**list_transactions**](docs/TransactionsApi.md#list_transactions) | **GET** /v2/locations/{location_id}/transactions
*TransactionsApi* | [**retrieve_transaction**](docs/TransactionsApi.md#retrieve_transaction) | **GET** /v2/locations/{location_id}/transactions/{transaction_id}
*TransactionsApi* | [**void_transaction**](docs/TransactionsApi.md#void_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/void


## Documentation For Models

 - [Address](docs/Address.md)
 - [BatchDeleteCatalogObjectsRequest](docs/BatchDeleteCatalogObjectsRequest.md)
 - [BatchDeleteCatalogObjectsResponse](docs/BatchDeleteCatalogObjectsResponse.md)
 - [BatchRetrieveCatalogObjectsRequest](docs/BatchRetrieveCatalogObjectsRequest.md)
 - [BatchRetrieveCatalogObjectsResponse](docs/BatchRetrieveCatalogObjectsResponse.md)
 - [BatchUpsertCatalogObjectsRequest](docs/BatchUpsertCatalogObjectsRequest.md)
 - [BatchUpsertCatalogObjectsResponse](docs/BatchUpsertCatalogObjectsResponse.md)
 - [CaptureTransactionRequest](docs/CaptureTransactionRequest.md)
 - [CaptureTransactionResponse](docs/CaptureTransactionResponse.md)
 - [Card](docs/Card.md)
 - [CatalogCategory](docs/CatalogCategory.md)
 - [CatalogDiscount](docs/CatalogDiscount.md)
 - [CatalogIdMapping](docs/CatalogIdMapping.md)
 - [CatalogInfoRequest](docs/CatalogInfoRequest.md)
 - [CatalogInfoResponse](docs/CatalogInfoResponse.md)
 - [CatalogInfoResponseLimits](docs/CatalogInfoResponseLimits.md)
 - [CatalogItem](docs/CatalogItem.md)
 - [CatalogItemModifierListInfo](docs/CatalogItemModifierListInfo.md)
 - [CatalogItemVariation](docs/CatalogItemVariation.md)
 - [CatalogModifier](docs/CatalogModifier.md)
 - [CatalogModifierList](docs/CatalogModifierList.md)
 - [CatalogModifierOverride](docs/CatalogModifierOverride.md)
 - [CatalogObject](docs/CatalogObject.md)
 - [CatalogObjectBatch](docs/CatalogObjectBatch.md)
 - [CatalogQuery](docs/CatalogQuery.md)
 - [CatalogQueryExact](docs/CatalogQueryExact.md)
 - [CatalogQueryItemsForModifierList](docs/CatalogQueryItemsForModifierList.md)
 - [CatalogQueryItemsForTax](docs/CatalogQueryItemsForTax.md)
 - [CatalogQueryPrefix](docs/CatalogQueryPrefix.md)
 - [CatalogQueryRange](docs/CatalogQueryRange.md)
 - [CatalogQuerySortedAttribute](docs/CatalogQuerySortedAttribute.md)
 - [CatalogQueryText](docs/CatalogQueryText.md)
 - [CatalogTax](docs/CatalogTax.md)
 - [CatalogV1Id](docs/CatalogV1Id.md)
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
 - [DeleteCatalogObjectRequest](docs/DeleteCatalogObjectRequest.md)
 - [DeleteCatalogObjectResponse](docs/DeleteCatalogObjectResponse.md)
 - [DeleteCustomerCardRequest](docs/DeleteCustomerCardRequest.md)
 - [DeleteCustomerCardResponse](docs/DeleteCustomerCardResponse.md)
 - [DeleteCustomerRequest](docs/DeleteCustomerRequest.md)
 - [DeleteCustomerResponse](docs/DeleteCustomerResponse.md)
 - [Error](docs/Error.md)
 - [ItemVariationLocationOverrides](docs/ItemVariationLocationOverrides.md)
 - [ListCatalogRequest](docs/ListCatalogRequest.md)
 - [ListCatalogResponse](docs/ListCatalogResponse.md)
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
 - [RetrieveCatalogObjectRequest](docs/RetrieveCatalogObjectRequest.md)
 - [RetrieveCatalogObjectResponse](docs/RetrieveCatalogObjectResponse.md)
 - [RetrieveCustomerRequest](docs/RetrieveCustomerRequest.md)
 - [RetrieveCustomerResponse](docs/RetrieveCustomerResponse.md)
 - [RetrieveTransactionRequest](docs/RetrieveTransactionRequest.md)
 - [RetrieveTransactionResponse](docs/RetrieveTransactionResponse.md)
 - [SearchCatalogObjectsRequest](docs/SearchCatalogObjectsRequest.md)
 - [SearchCatalogObjectsResponse](docs/SearchCatalogObjectsResponse.md)
 - [Tender](docs/Tender.md)
 - [TenderCardDetails](docs/TenderCardDetails.md)
 - [TenderCashDetails](docs/TenderCashDetails.md)
 - [Transaction](docs/Transaction.md)
 - [UpdateCustomerRequest](docs/UpdateCustomerRequest.md)
 - [UpdateCustomerResponse](docs/UpdateCustomerResponse.md)
 - [UpdateItemModifierListsRequest](docs/UpdateItemModifierListsRequest.md)
 - [UpdateItemModifierListsResponse](docs/UpdateItemModifierListsResponse.md)
 - [UpdateItemTaxesRequest](docs/UpdateItemTaxesRequest.md)
 - [UpdateItemTaxesResponse](docs/UpdateItemTaxesResponse.md)
 - [UpsertCatalogObjectRequest](docs/UpsertCatalogObjectRequest.md)
 - [UpsertCatalogObjectResponse](docs/UpsertCatalogObjectResponse.md)
 - [VoidTransactionRequest](docs/VoidTransactionRequest.md)
 - [VoidTransactionResponse](docs/VoidTransactionResponse.md)


## Documentation For Enums

 - [CardBrand](docs/CardBrand.md)
 - [CatalogDiscountType](docs/CatalogDiscountType.md)
 - [CatalogItemProductType](docs/CatalogItemProductType.md)
 - [CatalogModifierListSelectionType](docs/CatalogModifierListSelectionType.md)
 - [CatalogObjectType](docs/CatalogObjectType.md)
 - [CatalogPricingType](docs/CatalogPricingType.md)
 - [Country](docs/Country.md)
 - [Currency](docs/Currency.md)
 - [ErrorCategory](docs/ErrorCategory.md)
 - [ErrorCode](docs/ErrorCode.md)
 - [InventoryAlertType](docs/InventoryAlertType.md)
 - [LocationCapability](docs/LocationCapability.md)
 - [RefundStatus](docs/RefundStatus.md)
 - [SortOrder](docs/SortOrder.md)
 - [TaxCalculationPhase](docs/TaxCalculationPhase.md)
 - [TaxInclusionType](docs/TaxInclusionType.md)
 - [TenderCardDetailsEntryMethod](docs/TenderCardDetailsEntryMethod.md)
 - [TenderCardDetailsStatus](docs/TenderCardDetailsStatus.md)
 - [TenderType](docs/TenderType.md)
 - [TransactionProduct](docs/TransactionProduct.md)


## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: `https://connect.squareup.com/oauth2/authorize?<PARAMETERS>`
- **Scopes**: 
 - **MERCHANT_PROFILE_READ**: GET endpoints related to a merchant's business and location entities. Almost all Connect API applications need this permission in order to obtain a merchant's location IDs
 - **PAYMENTS_READ**: GET endpoints related to transactions and refunds
 - **PAYMENTS_WRITE**: POST, PUT, and DELETE endpoints related to transactions and refunds. E-commerce applications must request this permission
 - **CUSTOMERS_READ**:  GET endpoints related to customer management
 - **CUSTOMERS_WRITE**: POST, PUT, and DELETE endpoints related to customer management
 - **SETTLEMENTS_READ**: GET endpoints related to settlements (deposits)
 - **BANK_ACCOUNTS_READ**: GET endpoints related to a merchant's bank accounts
 - **ITEMS_READ**: GET endpoints related to a merchant's item library
 - **ITEMS_WRITE**: POST, PUT, and DELETE endpoints related to a merchant's item library
 - **ORDERS_READ**: GET endpoints related to a merchant's Square online store.
 - **ORDERS_WRITE**: POST, PUT, and DELETE endpoints related to a merchant's Square online store
 - **EMPLOYEES_READ**: GET endpoints related to employee management
 - **EMPLOYEES_WRITE**: POST, PUT, and DELETE endpoints related to employee management
 - **TIMECARDS_READ**: GET endpoints related to employee timecards
 - **TIMECARDS_WRITE**: POST, PUT, and DELETE endpoints related to employee timecards


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
