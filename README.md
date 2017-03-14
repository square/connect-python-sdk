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
*EmployeesApi* | [**v1_create_employee**](docs/EmployeesApi.md#v1_create_employee) | **POST** /v1/me/employees
*EmployeesApi* | [**v1_create_employee_role**](docs/EmployeesApi.md#v1_create_employee_role) | **POST** /v1/me/roles
*EmployeesApi* | [**v1_create_timecard**](docs/EmployeesApi.md#v1_create_timecard) | **POST** /v1/me/timecards
*EmployeesApi* | [**v1_delete_timecard**](docs/EmployeesApi.md#v1_delete_timecard) | **DELETE** /v1/me/timecards/{timecard_id}
*EmployeesApi* | [**v1_list_cash_drawer_shifts**](docs/EmployeesApi.md#v1_list_cash_drawer_shifts) | **GET** /v1/{location_id}/cash-drawer-shifts
*EmployeesApi* | [**v1_list_employee_roles**](docs/EmployeesApi.md#v1_list_employee_roles) | **GET** /v1/me/roles
*EmployeesApi* | [**v1_list_employees**](docs/EmployeesApi.md#v1_list_employees) | **GET** /v1/me/employees
*EmployeesApi* | [**v1_list_timecard_events**](docs/EmployeesApi.md#v1_list_timecard_events) | **GET** /v1/me/timecards/{timecard_id}/events
*EmployeesApi* | [**v1_list_timecards**](docs/EmployeesApi.md#v1_list_timecards) | **GET** /v1/me/timecards
*EmployeesApi* | [**v1_retrieve_cash_drawer_shift**](docs/EmployeesApi.md#v1_retrieve_cash_drawer_shift) | **GET** /v1/{location_id}/cash-drawer-shifts/{shift_id}
*EmployeesApi* | [**v1_retrieve_employee**](docs/EmployeesApi.md#v1_retrieve_employee) | **GET** /v1/me/employees/{employee_id}
*EmployeesApi* | [**v1_retrieve_employee_role**](docs/EmployeesApi.md#v1_retrieve_employee_role) | **GET** /v1/me/roles/{role_id}
*EmployeesApi* | [**v1_retrieve_timecard**](docs/EmployeesApi.md#v1_retrieve_timecard) | **GET** /v1/me/timecards/{timecard_id}
*EmployeesApi* | [**v1_update_employee**](docs/EmployeesApi.md#v1_update_employee) | **PUT** /v1/me/employees/{employee_id}
*EmployeesApi* | [**v1_update_employee_role**](docs/EmployeesApi.md#v1_update_employee_role) | **PUT** /v1/me/roles/{role_id}
*EmployeesApi* | [**v1_update_timecard**](docs/EmployeesApi.md#v1_update_timecard) | **PUT** /v1/me/timecards/{timecard_id}
*ItemsApi* | [**v1_adjust_inventory**](docs/ItemsApi.md#v1_adjust_inventory) | **POST** /v1/{location_id}/inventory/{variation_id}
*ItemsApi* | [**v1_apply_fee**](docs/ItemsApi.md#v1_apply_fee) | **PUT** /v1/{location_id}/items/{item_id}/fees/{fee_id}
*ItemsApi* | [**v1_apply_modifier_list**](docs/ItemsApi.md#v1_apply_modifier_list) | **PUT** /v1/{location_id}/items/{item_id}/modifier-lists/{modifier_list_id}
*ItemsApi* | [**v1_create_category**](docs/ItemsApi.md#v1_create_category) | **POST** /v1/{location_id}/categories
*ItemsApi* | [**v1_create_discount**](docs/ItemsApi.md#v1_create_discount) | **POST** /v1/{location_id}/discounts
*ItemsApi* | [**v1_create_fee**](docs/ItemsApi.md#v1_create_fee) | **POST** /v1/{location_id}/fees
*ItemsApi* | [**v1_create_item**](docs/ItemsApi.md#v1_create_item) | **POST** /v1/{location_id}/items
*ItemsApi* | [**v1_create_modifier_list**](docs/ItemsApi.md#v1_create_modifier_list) | **POST** /v1/{location_id}/modifier-lists
*ItemsApi* | [**v1_create_modifier_option**](docs/ItemsApi.md#v1_create_modifier_option) | **POST** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options
*ItemsApi* | [**v1_create_page**](docs/ItemsApi.md#v1_create_page) | **POST** /v1/{location_id}/pages
*ItemsApi* | [**v1_create_variation**](docs/ItemsApi.md#v1_create_variation) | **POST** /v1/{location_id}/items/{item_id}/variations
*ItemsApi* | [**v1_delete_category**](docs/ItemsApi.md#v1_delete_category) | **DELETE** /v1/{location_id}/categories/{category_id}
*ItemsApi* | [**v1_delete_discount**](docs/ItemsApi.md#v1_delete_discount) | **DELETE** /v1/{location_id}/discounts/{discount_id}
*ItemsApi* | [**v1_delete_fee**](docs/ItemsApi.md#v1_delete_fee) | **DELETE** /v1/{location_id}/fees/{fee_id}
*ItemsApi* | [**v1_delete_item**](docs/ItemsApi.md#v1_delete_item) | **DELETE** /v1/{location_id}/items/{item_id}
*ItemsApi* | [**v1_delete_modifier_list**](docs/ItemsApi.md#v1_delete_modifier_list) | **DELETE** /v1/{location_id}/modifier-lists/{modifier_list_id}
*ItemsApi* | [**v1_delete_modifier_option**](docs/ItemsApi.md#v1_delete_modifier_option) | **DELETE** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options/{modifier_option_id}
*ItemsApi* | [**v1_delete_page**](docs/ItemsApi.md#v1_delete_page) | **DELETE** /v1/{location_id}/pages/{page_id}
*ItemsApi* | [**v1_delete_page_cell**](docs/ItemsApi.md#v1_delete_page_cell) | **DELETE** /v1/{location_id}/pages/{page_id}/cells
*ItemsApi* | [**v1_delete_variation**](docs/ItemsApi.md#v1_delete_variation) | **DELETE** /v1/{location_id}/items/{item_id}/variations/{variation_id}
*ItemsApi* | [**v1_list_categories**](docs/ItemsApi.md#v1_list_categories) | **GET** /v1/{location_id}/categories
*ItemsApi* | [**v1_list_discounts**](docs/ItemsApi.md#v1_list_discounts) | **GET** /v1/{location_id}/discounts
*ItemsApi* | [**v1_list_fees**](docs/ItemsApi.md#v1_list_fees) | **GET** /v1/{location_id}/fees
*ItemsApi* | [**v1_list_inventory**](docs/ItemsApi.md#v1_list_inventory) | **GET** /v1/{location_id}/inventory
*ItemsApi* | [**v1_list_items**](docs/ItemsApi.md#v1_list_items) | **GET** /v1/{location_id}/items
*ItemsApi* | [**v1_list_modifier_lists**](docs/ItemsApi.md#v1_list_modifier_lists) | **GET** /v1/{location_id}/modifier-lists
*ItemsApi* | [**v1_list_pages**](docs/ItemsApi.md#v1_list_pages) | **GET** /v1/{location_id}/pages
*ItemsApi* | [**v1_remove_fee**](docs/ItemsApi.md#v1_remove_fee) | **DELETE** /v1/{location_id}/items/{item_id}/fees/{fee_id}
*ItemsApi* | [**v1_remove_modifier_list**](docs/ItemsApi.md#v1_remove_modifier_list) | **DELETE** /v1/{location_id}/items/{item_id}/modifier-lists/{modifier_list_id}
*ItemsApi* | [**v1_retrieve_item**](docs/ItemsApi.md#v1_retrieve_item) | **GET** /v1/{location_id}/items/{item_id}
*ItemsApi* | [**v1_retrieve_modifier_list**](docs/ItemsApi.md#v1_retrieve_modifier_list) | **GET** /v1/{location_id}/modifier-lists/{modifier_list_id}
*ItemsApi* | [**v1_update_category**](docs/ItemsApi.md#v1_update_category) | **PUT** /v1/{location_id}/categories/{category_id}
*ItemsApi* | [**v1_update_discount**](docs/ItemsApi.md#v1_update_discount) | **PUT** /v1/{location_id}/discounts/{discount_id}
*ItemsApi* | [**v1_update_fee**](docs/ItemsApi.md#v1_update_fee) | **PUT** /v1/{location_id}/fees/{fee_id}
*ItemsApi* | [**v1_update_item**](docs/ItemsApi.md#v1_update_item) | **PUT** /v1/{location_id}/items/{item_id}
*ItemsApi* | [**v1_update_modifier_list**](docs/ItemsApi.md#v1_update_modifier_list) | **PUT** /v1/{location_id}/modifier-lists/{modifier_list_id}
*ItemsApi* | [**v1_update_modifier_option**](docs/ItemsApi.md#v1_update_modifier_option) | **PUT** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options/{modifier_option_id}
*ItemsApi* | [**v1_update_page**](docs/ItemsApi.md#v1_update_page) | **PUT** /v1/{location_id}/pages/{page_id}
*ItemsApi* | [**v1_update_page_cell**](docs/ItemsApi.md#v1_update_page_cell) | **PUT** /v1/{location_id}/pages/{page_id}/cells
*ItemsApi* | [**v1_update_variation**](docs/ItemsApi.md#v1_update_variation) | **PUT** /v1/{location_id}/items/{item_id}/variations/{variation_id}
*LocationApi* | [**list_locations**](docs/LocationApi.md#list_locations) | **GET** /v2/locations
*LocationApi* | [**v1_list_locations**](docs/LocationApi.md#v1_list_locations) | **GET** /v1/me/locations
*LocationApi* | [**v1_retrieve_business**](docs/LocationApi.md#v1_retrieve_business) | **GET** /v1/me
*RefundApi* | [**create_refund**](docs/RefundApi.md#create_refund) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/refund
*RefundApi* | [**list_refunds**](docs/RefundApi.md#list_refunds) | **GET** /v2/locations/{location_id}/refunds
*TransactionApi* | [**capture_transaction**](docs/TransactionApi.md#capture_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/capture
*TransactionApi* | [**charge**](docs/TransactionApi.md#charge) | **POST** /v2/locations/{location_id}/transactions
*TransactionApi* | [**list_transactions**](docs/TransactionApi.md#list_transactions) | **GET** /v2/locations/{location_id}/transactions
*TransactionApi* | [**retrieve_transaction**](docs/TransactionApi.md#retrieve_transaction) | **GET** /v2/locations/{location_id}/transactions/{transaction_id}
*TransactionApi* | [**void_transaction**](docs/TransactionApi.md#void_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/void
*TransactionsApi* | [**v1_create_refund**](docs/TransactionsApi.md#v1_create_refund) | **POST** /v1/{location_id}/refunds
*TransactionsApi* | [**v1_list_bank_accounts**](docs/TransactionsApi.md#v1_list_bank_accounts) | **GET** /v1/{location_id}/bank-accounts
*TransactionsApi* | [**v1_list_orders**](docs/TransactionsApi.md#v1_list_orders) | **GET** /v1/{location_id}/orders
*TransactionsApi* | [**v1_list_payments**](docs/TransactionsApi.md#v1_list_payments) | **GET** /v1/{location_id}/payments
*TransactionsApi* | [**v1_list_refunds**](docs/TransactionsApi.md#v1_list_refunds) | **GET** /v1/{location_id}/refunds
*TransactionsApi* | [**v1_list_settlements**](docs/TransactionsApi.md#v1_list_settlements) | **GET** /v1/{location_id}/settlements
*TransactionsApi* | [**v1_retrieve_bank_account**](docs/TransactionsApi.md#v1_retrieve_bank_account) | **GET** /v1/{location_id}/bank-accounts/{bank_account_id}
*TransactionsApi* | [**v1_retrieve_order**](docs/TransactionsApi.md#v1_retrieve_order) | **GET** /v1/{location_id}/orders/{order_id}
*TransactionsApi* | [**v1_retrieve_payment**](docs/TransactionsApi.md#v1_retrieve_payment) | **GET** /v1/{location_id}/payments/{payment_id}
*TransactionsApi* | [**v1_retrieve_settlement**](docs/TransactionsApi.md#v1_retrieve_settlement) | **GET** /v1/{location_id}/settlements/{settlement_id}
*TransactionsApi* | [**v1_update_order**](docs/TransactionsApi.md#v1_update_order) | **PUT** /v1/{location_id}/orders/{order_id}


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
 - [Device](docs/Device.md)
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
 - [V1AdjustInventoryRequest](docs/V1AdjustInventoryRequest.md)
 - [V1BankAccount](docs/V1BankAccount.md)
 - [V1CashDrawerEvent](docs/V1CashDrawerEvent.md)
 - [V1CashDrawerShift](docs/V1CashDrawerShift.md)
 - [V1Category](docs/V1Category.md)
 - [V1CreateRefundRequest](docs/V1CreateRefundRequest.md)
 - [V1Discount](docs/V1Discount.md)
 - [V1Employee](docs/V1Employee.md)
 - [V1EmployeeRole](docs/V1EmployeeRole.md)
 - [V1Fee](docs/V1Fee.md)
 - [V1InventoryEntry](docs/V1InventoryEntry.md)
 - [V1Item](docs/V1Item.md)
 - [V1ItemImage](docs/V1ItemImage.md)
 - [V1Merchant](docs/V1Merchant.md)
 - [V1MerchantLocationDetails](docs/V1MerchantLocationDetails.md)
 - [V1ModifierList](docs/V1ModifierList.md)
 - [V1ModifierOption](docs/V1ModifierOption.md)
 - [V1Money](docs/V1Money.md)
 - [V1Order](docs/V1Order.md)
 - [V1OrderHistoryEntry](docs/V1OrderHistoryEntry.md)
 - [V1Page](docs/V1Page.md)
 - [V1PageCell](docs/V1PageCell.md)
 - [V1Payment](docs/V1Payment.md)
 - [V1PaymentDiscount](docs/V1PaymentDiscount.md)
 - [V1PaymentItemDetail](docs/V1PaymentItemDetail.md)
 - [V1PaymentItemization](docs/V1PaymentItemization.md)
 - [V1PaymentModifier](docs/V1PaymentModifier.md)
 - [V1PaymentTax](docs/V1PaymentTax.md)
 - [V1PhoneNumber](docs/V1PhoneNumber.md)
 - [V1Refund](docs/V1Refund.md)
 - [V1Settlement](docs/V1Settlement.md)
 - [V1SettlementEntry](docs/V1SettlementEntry.md)
 - [V1Tender](docs/V1Tender.md)
 - [V1Timecard](docs/V1Timecard.md)
 - [V1TimecardEvent](docs/V1TimecardEvent.md)
 - [V1UpdateModifierListRequest](docs/V1UpdateModifierListRequest.md)
 - [V1UpdateOrderRequest](docs/V1UpdateOrderRequest.md)
 - [V1Variation](docs/V1Variation.md)
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
