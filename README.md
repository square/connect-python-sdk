Square Connect Python SDK [![Build Status](https://travis-ci.org/square/connect-python-sdk.svg?branch=master)](https://travis-ci.org/square/connect-python-sdk)[![PyPI version](https://badge.fury.io/py/squareconnect.svg)](https://badge.fury.io/py/squareconnect)
==================

**If you have feedback about the new SDKs, or just want to talk to other Square Developers, request an invite to the new [slack community for Square Developers](https://squ.re/2q56529)**

This repository contains the released Python client SDK. Check out our [API
specification repository](https://github.com/square/connect-api-specification)
for the specification and template files we used to generate this.

## Requirements.

Make sure you have Python 2 >=2.7.9 or Python 3 >= 3.4

## Installation & Usage
### Option 1: pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/square/connect-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/square/connect-python-sdk.git`)

### Option 2: Setuptools

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
from squareconnect.apis.locations_api import LocationsApi

# create an instance of the Location API class
api_instance = LocationsApi()
# setup authorization
api_instance.api_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

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
from squareconnect.apis.transactions_api import TransactionsApi

# create an instance of the Transaction API class
api_instance = TransactionApi()
# setup authorization
api_instance.api_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

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
*ApplePayApi* | [**register_domain**](docs/ApplePayApi.md#register_domain) | **POST** /v2/apple-pay/domains
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
*CustomersApi* | [**search_customers**](docs/CustomersApi.md#search_customers) | **POST** /v2/customers/search
*CustomersApi* | [**update_customer**](docs/CustomersApi.md#update_customer) | **PUT** /v2/customers/{customer_id}
*EmployeesApi* | [**list_employees**](docs/EmployeesApi.md#list_employees) | **GET** /v2/employees
*EmployeesApi* | [**retrieve_employee**](docs/EmployeesApi.md#retrieve_employee) | **GET** /v2/employees/{id}
*InventoryApi* | [**batch_change_inventory**](docs/InventoryApi.md#batch_change_inventory) | **POST** /v2/inventory/batch-change
*InventoryApi* | [**batch_retrieve_inventory_changes**](docs/InventoryApi.md#batch_retrieve_inventory_changes) | **POST** /v2/inventory/batch-retrieve-changes
*InventoryApi* | [**batch_retrieve_inventory_counts**](docs/InventoryApi.md#batch_retrieve_inventory_counts) | **POST** /v2/inventory/batch-retrieve-counts
*InventoryApi* | [**retrieve_inventory_adjustment**](docs/InventoryApi.md#retrieve_inventory_adjustment) | **GET** /v2/inventory/adjustment/{adjustment_id}
*InventoryApi* | [**retrieve_inventory_changes**](docs/InventoryApi.md#retrieve_inventory_changes) | **GET** /v2/inventory/{catalog_object_id}/changes
*InventoryApi* | [**retrieve_inventory_count**](docs/InventoryApi.md#retrieve_inventory_count) | **GET** /v2/inventory/{catalog_object_id}
*InventoryApi* | [**retrieve_inventory_physical_count**](docs/InventoryApi.md#retrieve_inventory_physical_count) | **GET** /v2/inventory/physical-count/{physical_count_id}
*LaborApi* | [**create_break_type**](docs/LaborApi.md#create_break_type) | **POST** /v2/labor/break-types
*LaborApi* | [**create_shift**](docs/LaborApi.md#create_shift) | **POST** /v2/labor/shifts
*LaborApi* | [**delete_break_type**](docs/LaborApi.md#delete_break_type) | **DELETE** /v2/labor/break-types/{id}
*LaborApi* | [**delete_shift**](docs/LaborApi.md#delete_shift) | **DELETE** /v2/labor/shifts/{id}
*LaborApi* | [**get_break_type**](docs/LaborApi.md#get_break_type) | **GET** /v2/labor/break-types/{id}
*LaborApi* | [**get_employee_wage**](docs/LaborApi.md#get_employee_wage) | **GET** /v2/labor/employee-wages/{id}
*LaborApi* | [**get_shift**](docs/LaborApi.md#get_shift) | **GET** /v2/labor/shifts/{id}
*LaborApi* | [**list_break_types**](docs/LaborApi.md#list_break_types) | **GET** /v2/labor/break-types
*LaborApi* | [**list_employee_wages**](docs/LaborApi.md#list_employee_wages) | **GET** /v2/labor/employee-wages
*LaborApi* | [**list_workweek_configs**](docs/LaborApi.md#list_workweek_configs) | **GET** /v2/labor/workweek-configs
*LaborApi* | [**search_shifts**](docs/LaborApi.md#search_shifts) | **POST** /v2/labor/shifts/search
*LaborApi* | [**update_break_type**](docs/LaborApi.md#update_break_type) | **PUT** /v2/labor/break-types/{id}
*LaborApi* | [**update_shift**](docs/LaborApi.md#update_shift) | **PUT** /v2/labor/shifts/{id}
*LaborApi* | [**update_workweek_config**](docs/LaborApi.md#update_workweek_config) | **PUT** /v2/labor/workweek-configs/{id}
*LocationsApi* | [**list_locations**](docs/LocationsApi.md#list_locations) | **GET** /v2/locations
*MobileAuthorizationApi* | [**create_mobile_authorization_code**](docs/MobileAuthorizationApi.md#create_mobile_authorization_code) | **POST** /mobile/authorization-code
*OAuthApi* | [**obtain_token**](docs/OAuthApi.md#obtain_token) | **POST** /oauth2/token
*OAuthApi* | [**renew_token**](docs/OAuthApi.md#renew_token) | **POST** /oauth2/clients/{client_id}/access-token/renew
*OAuthApi* | [**revoke_token**](docs/OAuthApi.md#revoke_token) | **POST** /oauth2/revoke
*OrdersApi* | [**batch_retrieve_orders**](docs/OrdersApi.md#batch_retrieve_orders) | **POST** /v2/locations/{location_id}/orders/batch-retrieve
*OrdersApi* | [**create_order**](docs/OrdersApi.md#create_order) | **POST** /v2/locations/{location_id}/orders
*OrdersApi* | [**search_orders**](docs/OrdersApi.md#search_orders) | **POST** /v2/orders/search
*ReportingApi* | [**list_additional_recipient_receivable_refunds**](docs/ReportingApi.md#list_additional_recipient_receivable_refunds) | **GET** /v2/locations/{location_id}/additional-recipient-receivable-refunds
*ReportingApi* | [**list_additional_recipient_receivables**](docs/ReportingApi.md#list_additional_recipient_receivables) | **GET** /v2/locations/{location_id}/additional-recipient-receivables
*TransactionsApi* | [**capture_transaction**](docs/TransactionsApi.md#capture_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/capture
*TransactionsApi* | [**charge**](docs/TransactionsApi.md#charge) | **POST** /v2/locations/{location_id}/transactions
*TransactionsApi* | [**create_refund**](docs/TransactionsApi.md#create_refund) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/refund
*TransactionsApi* | [**list_refunds**](docs/TransactionsApi.md#list_refunds) | **GET** /v2/locations/{location_id}/refunds
*TransactionsApi* | [**list_transactions**](docs/TransactionsApi.md#list_transactions) | **GET** /v2/locations/{location_id}/transactions
*TransactionsApi* | [**retrieve_transaction**](docs/TransactionsApi.md#retrieve_transaction) | **GET** /v2/locations/{location_id}/transactions/{transaction_id}
*TransactionsApi* | [**void_transaction**](docs/TransactionsApi.md#void_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/void
*V1EmployeesApi* | [**create_employee**](docs/V1EmployeesApi.md#create_employee) | **POST** /v1/me/employees
*V1EmployeesApi* | [**create_employee_role**](docs/V1EmployeesApi.md#create_employee_role) | **POST** /v1/me/roles
*V1EmployeesApi* | [**create_timecard**](docs/V1EmployeesApi.md#create_timecard) | **POST** /v1/me/timecards
*V1EmployeesApi* | [**delete_timecard**](docs/V1EmployeesApi.md#delete_timecard) | **DELETE** /v1/me/timecards/{timecard_id}
*V1EmployeesApi* | [**list_cash_drawer_shifts**](docs/V1EmployeesApi.md#list_cash_drawer_shifts) | **GET** /v1/{location_id}/cash-drawer-shifts
*V1EmployeesApi* | [**list_employee_roles**](docs/V1EmployeesApi.md#list_employee_roles) | **GET** /v1/me/roles
*V1EmployeesApi* | [**list_employees**](docs/V1EmployeesApi.md#list_employees) | **GET** /v1/me/employees
*V1EmployeesApi* | [**list_timecard_events**](docs/V1EmployeesApi.md#list_timecard_events) | **GET** /v1/me/timecards/{timecard_id}/events
*V1EmployeesApi* | [**list_timecards**](docs/V1EmployeesApi.md#list_timecards) | **GET** /v1/me/timecards
*V1EmployeesApi* | [**retrieve_cash_drawer_shift**](docs/V1EmployeesApi.md#retrieve_cash_drawer_shift) | **GET** /v1/{location_id}/cash-drawer-shifts/{shift_id}
*V1EmployeesApi* | [**retrieve_employee**](docs/V1EmployeesApi.md#retrieve_employee) | **GET** /v1/me/employees/{employee_id}
*V1EmployeesApi* | [**retrieve_employee_role**](docs/V1EmployeesApi.md#retrieve_employee_role) | **GET** /v1/me/roles/{role_id}
*V1EmployeesApi* | [**retrieve_timecard**](docs/V1EmployeesApi.md#retrieve_timecard) | **GET** /v1/me/timecards/{timecard_id}
*V1EmployeesApi* | [**update_employee**](docs/V1EmployeesApi.md#update_employee) | **PUT** /v1/me/employees/{employee_id}
*V1EmployeesApi* | [**update_employee_role**](docs/V1EmployeesApi.md#update_employee_role) | **PUT** /v1/me/roles/{role_id}
*V1EmployeesApi* | [**update_timecard**](docs/V1EmployeesApi.md#update_timecard) | **PUT** /v1/me/timecards/{timecard_id}
*V1ItemsApi* | [**adjust_inventory**](docs/V1ItemsApi.md#adjust_inventory) | **POST** /v1/{location_id}/inventory/{variation_id}
*V1ItemsApi* | [**apply_fee**](docs/V1ItemsApi.md#apply_fee) | **PUT** /v1/{location_id}/items/{item_id}/fees/{fee_id}
*V1ItemsApi* | [**apply_modifier_list**](docs/V1ItemsApi.md#apply_modifier_list) | **PUT** /v1/{location_id}/items/{item_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**create_category**](docs/V1ItemsApi.md#create_category) | **POST** /v1/{location_id}/categories
*V1ItemsApi* | [**create_discount**](docs/V1ItemsApi.md#create_discount) | **POST** /v1/{location_id}/discounts
*V1ItemsApi* | [**create_fee**](docs/V1ItemsApi.md#create_fee) | **POST** /v1/{location_id}/fees
*V1ItemsApi* | [**create_item**](docs/V1ItemsApi.md#create_item) | **POST** /v1/{location_id}/items
*V1ItemsApi* | [**create_modifier_list**](docs/V1ItemsApi.md#create_modifier_list) | **POST** /v1/{location_id}/modifier-lists
*V1ItemsApi* | [**create_modifier_option**](docs/V1ItemsApi.md#create_modifier_option) | **POST** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options
*V1ItemsApi* | [**create_page**](docs/V1ItemsApi.md#create_page) | **POST** /v1/{location_id}/pages
*V1ItemsApi* | [**create_variation**](docs/V1ItemsApi.md#create_variation) | **POST** /v1/{location_id}/items/{item_id}/variations
*V1ItemsApi* | [**delete_category**](docs/V1ItemsApi.md#delete_category) | **DELETE** /v1/{location_id}/categories/{category_id}
*V1ItemsApi* | [**delete_discount**](docs/V1ItemsApi.md#delete_discount) | **DELETE** /v1/{location_id}/discounts/{discount_id}
*V1ItemsApi* | [**delete_fee**](docs/V1ItemsApi.md#delete_fee) | **DELETE** /v1/{location_id}/fees/{fee_id}
*V1ItemsApi* | [**delete_item**](docs/V1ItemsApi.md#delete_item) | **DELETE** /v1/{location_id}/items/{item_id}
*V1ItemsApi* | [**delete_modifier_list**](docs/V1ItemsApi.md#delete_modifier_list) | **DELETE** /v1/{location_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**delete_modifier_option**](docs/V1ItemsApi.md#delete_modifier_option) | **DELETE** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options/{modifier_option_id}
*V1ItemsApi* | [**delete_page**](docs/V1ItemsApi.md#delete_page) | **DELETE** /v1/{location_id}/pages/{page_id}
*V1ItemsApi* | [**delete_page_cell**](docs/V1ItemsApi.md#delete_page_cell) | **DELETE** /v1/{location_id}/pages/{page_id}/cells
*V1ItemsApi* | [**delete_variation**](docs/V1ItemsApi.md#delete_variation) | **DELETE** /v1/{location_id}/items/{item_id}/variations/{variation_id}
*V1ItemsApi* | [**list_categories**](docs/V1ItemsApi.md#list_categories) | **GET** /v1/{location_id}/categories
*V1ItemsApi* | [**list_discounts**](docs/V1ItemsApi.md#list_discounts) | **GET** /v1/{location_id}/discounts
*V1ItemsApi* | [**list_fees**](docs/V1ItemsApi.md#list_fees) | **GET** /v1/{location_id}/fees
*V1ItemsApi* | [**list_inventory**](docs/V1ItemsApi.md#list_inventory) | **GET** /v1/{location_id}/inventory
*V1ItemsApi* | [**list_items**](docs/V1ItemsApi.md#list_items) | **GET** /v1/{location_id}/items
*V1ItemsApi* | [**list_modifier_lists**](docs/V1ItemsApi.md#list_modifier_lists) | **GET** /v1/{location_id}/modifier-lists
*V1ItemsApi* | [**list_pages**](docs/V1ItemsApi.md#list_pages) | **GET** /v1/{location_id}/pages
*V1ItemsApi* | [**remove_fee**](docs/V1ItemsApi.md#remove_fee) | **DELETE** /v1/{location_id}/items/{item_id}/fees/{fee_id}
*V1ItemsApi* | [**remove_modifier_list**](docs/V1ItemsApi.md#remove_modifier_list) | **DELETE** /v1/{location_id}/items/{item_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**retrieve_item**](docs/V1ItemsApi.md#retrieve_item) | **GET** /v1/{location_id}/items/{item_id}
*V1ItemsApi* | [**retrieve_modifier_list**](docs/V1ItemsApi.md#retrieve_modifier_list) | **GET** /v1/{location_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**update_category**](docs/V1ItemsApi.md#update_category) | **PUT** /v1/{location_id}/categories/{category_id}
*V1ItemsApi* | [**update_discount**](docs/V1ItemsApi.md#update_discount) | **PUT** /v1/{location_id}/discounts/{discount_id}
*V1ItemsApi* | [**update_fee**](docs/V1ItemsApi.md#update_fee) | **PUT** /v1/{location_id}/fees/{fee_id}
*V1ItemsApi* | [**update_item**](docs/V1ItemsApi.md#update_item) | **PUT** /v1/{location_id}/items/{item_id}
*V1ItemsApi* | [**update_modifier_list**](docs/V1ItemsApi.md#update_modifier_list) | **PUT** /v1/{location_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**update_modifier_option**](docs/V1ItemsApi.md#update_modifier_option) | **PUT** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options/{modifier_option_id}
*V1ItemsApi* | [**update_page**](docs/V1ItemsApi.md#update_page) | **PUT** /v1/{location_id}/pages/{page_id}
*V1ItemsApi* | [**update_page_cell**](docs/V1ItemsApi.md#update_page_cell) | **PUT** /v1/{location_id}/pages/{page_id}/cells
*V1ItemsApi* | [**update_variation**](docs/V1ItemsApi.md#update_variation) | **PUT** /v1/{location_id}/items/{item_id}/variations/{variation_id}
*V1LocationsApi* | [**list_locations**](docs/V1LocationsApi.md#list_locations) | **GET** /v1/me/locations
*V1LocationsApi* | [**retrieve_business**](docs/V1LocationsApi.md#retrieve_business) | **GET** /v1/me
*V1TransactionsApi* | [**create_refund**](docs/V1TransactionsApi.md#create_refund) | **POST** /v1/{location_id}/refunds
*V1TransactionsApi* | [**list_bank_accounts**](docs/V1TransactionsApi.md#list_bank_accounts) | **GET** /v1/{location_id}/bank-accounts
*V1TransactionsApi* | [**list_orders**](docs/V1TransactionsApi.md#list_orders) | **GET** /v1/{location_id}/orders
*V1TransactionsApi* | [**list_payments**](docs/V1TransactionsApi.md#list_payments) | **GET** /v1/{location_id}/payments
*V1TransactionsApi* | [**list_refunds**](docs/V1TransactionsApi.md#list_refunds) | **GET** /v1/{location_id}/refunds
*V1TransactionsApi* | [**list_settlements**](docs/V1TransactionsApi.md#list_settlements) | **GET** /v1/{location_id}/settlements
*V1TransactionsApi* | [**retrieve_bank_account**](docs/V1TransactionsApi.md#retrieve_bank_account) | **GET** /v1/{location_id}/bank-accounts/{bank_account_id}
*V1TransactionsApi* | [**retrieve_order**](docs/V1TransactionsApi.md#retrieve_order) | **GET** /v1/{location_id}/orders/{order_id}
*V1TransactionsApi* | [**retrieve_payment**](docs/V1TransactionsApi.md#retrieve_payment) | **GET** /v1/{location_id}/payments/{payment_id}
*V1TransactionsApi* | [**retrieve_settlement**](docs/V1TransactionsApi.md#retrieve_settlement) | **GET** /v1/{location_id}/settlements/{settlement_id}
*V1TransactionsApi* | [**update_order**](docs/V1TransactionsApi.md#update_order) | **PUT** /v1/{location_id}/orders/{order_id}


## Documentation For Models

 - [AdditionalRecipient](docs/AdditionalRecipient.md)
 - [AdditionalRecipientReceivable](docs/AdditionalRecipientReceivable.md)
 - [AdditionalRecipientReceivableRefund](docs/AdditionalRecipientReceivableRefund.md)
 - [Address](docs/Address.md)
 - [BatchChangeInventoryRequest](docs/BatchChangeInventoryRequest.md)
 - [BatchChangeInventoryResponse](docs/BatchChangeInventoryResponse.md)
 - [BatchDeleteCatalogObjectsRequest](docs/BatchDeleteCatalogObjectsRequest.md)
 - [BatchDeleteCatalogObjectsResponse](docs/BatchDeleteCatalogObjectsResponse.md)
 - [BatchRetrieveCatalogObjectsRequest](docs/BatchRetrieveCatalogObjectsRequest.md)
 - [BatchRetrieveCatalogObjectsResponse](docs/BatchRetrieveCatalogObjectsResponse.md)
 - [BatchRetrieveInventoryChangesRequest](docs/BatchRetrieveInventoryChangesRequest.md)
 - [BatchRetrieveInventoryChangesResponse](docs/BatchRetrieveInventoryChangesResponse.md)
 - [BatchRetrieveInventoryCountsRequest](docs/BatchRetrieveInventoryCountsRequest.md)
 - [BatchRetrieveInventoryCountsResponse](docs/BatchRetrieveInventoryCountsResponse.md)
 - [BatchRetrieveOrdersRequest](docs/BatchRetrieveOrdersRequest.md)
 - [BatchRetrieveOrdersResponse](docs/BatchRetrieveOrdersResponse.md)
 - [BatchUpsertCatalogObjectsRequest](docs/BatchUpsertCatalogObjectsRequest.md)
 - [BatchUpsertCatalogObjectsResponse](docs/BatchUpsertCatalogObjectsResponse.md)
 - [BreakType](docs/BreakType.md)
 - [BusinessHours](docs/BusinessHours.md)
 - [BusinessHoursPeriod](docs/BusinessHoursPeriod.md)
 - [CaptureTransactionRequest](docs/CaptureTransactionRequest.md)
 - [CaptureTransactionResponse](docs/CaptureTransactionResponse.md)
 - [Card](docs/Card.md)
 - [CatalogCategory](docs/CatalogCategory.md)
 - [CatalogDiscount](docs/CatalogDiscount.md)
 - [CatalogIdMapping](docs/CatalogIdMapping.md)
 - [CatalogImage](docs/CatalogImage.md)
 - [CatalogInfoRequest](docs/CatalogInfoRequest.md)
 - [CatalogInfoResponse](docs/CatalogInfoResponse.md)
 - [CatalogInfoResponseLimits](docs/CatalogInfoResponseLimits.md)
 - [CatalogItem](docs/CatalogItem.md)
 - [CatalogItemModifierListInfo](docs/CatalogItemModifierListInfo.md)
 - [CatalogItemVariation](docs/CatalogItemVariation.md)
 - [CatalogMeasurementUnit](docs/CatalogMeasurementUnit.md)
 - [CatalogModifier](docs/CatalogModifier.md)
 - [CatalogModifierList](docs/CatalogModifierList.md)
 - [CatalogModifierOverride](docs/CatalogModifierOverride.md)
 - [CatalogObject](docs/CatalogObject.md)
 - [CatalogObjectBatch](docs/CatalogObjectBatch.md)
 - [CatalogPricingRule](docs/CatalogPricingRule.md)
 - [CatalogProductSet](docs/CatalogProductSet.md)
 - [CatalogQuery](docs/CatalogQuery.md)
 - [CatalogQueryExact](docs/CatalogQueryExact.md)
 - [CatalogQueryItemsForModifierList](docs/CatalogQueryItemsForModifierList.md)
 - [CatalogQueryItemsForTax](docs/CatalogQueryItemsForTax.md)
 - [CatalogQueryPrefix](docs/CatalogQueryPrefix.md)
 - [CatalogQueryRange](docs/CatalogQueryRange.md)
 - [CatalogQuerySortedAttribute](docs/CatalogQuerySortedAttribute.md)
 - [CatalogQueryText](docs/CatalogQueryText.md)
 - [CatalogTax](docs/CatalogTax.md)
 - [CatalogTimePeriod](docs/CatalogTimePeriod.md)
 - [CatalogV1Id](docs/CatalogV1Id.md)
 - [ChargeRequest](docs/ChargeRequest.md)
 - [ChargeRequestAdditionalRecipient](docs/ChargeRequestAdditionalRecipient.md)
 - [ChargeResponse](docs/ChargeResponse.md)
 - [Checkout](docs/Checkout.md)
 - [Coordinates](docs/Coordinates.md)
 - [CreateBreakTypeRequest](docs/CreateBreakTypeRequest.md)
 - [CreateBreakTypeResponse](docs/CreateBreakTypeResponse.md)
 - [CreateCheckoutRequest](docs/CreateCheckoutRequest.md)
 - [CreateCheckoutResponse](docs/CreateCheckoutResponse.md)
 - [CreateCustomerCardRequest](docs/CreateCustomerCardRequest.md)
 - [CreateCustomerCardResponse](docs/CreateCustomerCardResponse.md)
 - [CreateCustomerRequest](docs/CreateCustomerRequest.md)
 - [CreateCustomerResponse](docs/CreateCustomerResponse.md)
 - [CreateMobileAuthorizationCodeRequest](docs/CreateMobileAuthorizationCodeRequest.md)
 - [CreateMobileAuthorizationCodeResponse](docs/CreateMobileAuthorizationCodeResponse.md)
 - [CreateOrderRequest](docs/CreateOrderRequest.md)
 - [CreateOrderRequestDiscount](docs/CreateOrderRequestDiscount.md)
 - [CreateOrderRequestLineItem](docs/CreateOrderRequestLineItem.md)
 - [CreateOrderRequestModifier](docs/CreateOrderRequestModifier.md)
 - [CreateOrderRequestTax](docs/CreateOrderRequestTax.md)
 - [CreateOrderResponse](docs/CreateOrderResponse.md)
 - [CreateRefundRequest](docs/CreateRefundRequest.md)
 - [CreateRefundResponse](docs/CreateRefundResponse.md)
 - [CreateShiftRequest](docs/CreateShiftRequest.md)
 - [CreateShiftResponse](docs/CreateShiftResponse.md)
 - [Customer](docs/Customer.md)
 - [CustomerCreationSourceFilter](docs/CustomerCreationSourceFilter.md)
 - [CustomerFilter](docs/CustomerFilter.md)
 - [CustomerGroupInfo](docs/CustomerGroupInfo.md)
 - [CustomerPreferences](docs/CustomerPreferences.md)
 - [CustomerQuery](docs/CustomerQuery.md)
 - [CustomerSort](docs/CustomerSort.md)
 - [DateRange](docs/DateRange.md)
 - [DeleteBreakTypeRequest](docs/DeleteBreakTypeRequest.md)
 - [DeleteBreakTypeResponse](docs/DeleteBreakTypeResponse.md)
 - [DeleteCatalogObjectRequest](docs/DeleteCatalogObjectRequest.md)
 - [DeleteCatalogObjectResponse](docs/DeleteCatalogObjectResponse.md)
 - [DeleteCustomerCardRequest](docs/DeleteCustomerCardRequest.md)
 - [DeleteCustomerCardResponse](docs/DeleteCustomerCardResponse.md)
 - [DeleteCustomerRequest](docs/DeleteCustomerRequest.md)
 - [DeleteCustomerResponse](docs/DeleteCustomerResponse.md)
 - [DeleteShiftRequest](docs/DeleteShiftRequest.md)
 - [DeleteShiftResponse](docs/DeleteShiftResponse.md)
 - [Device](docs/Device.md)
 - [Employee](docs/Employee.md)
 - [EmployeeWage](docs/EmployeeWage.md)
 - [Error](docs/Error.md)
 - [GetBreakTypeRequest](docs/GetBreakTypeRequest.md)
 - [GetBreakTypeResponse](docs/GetBreakTypeResponse.md)
 - [GetEmployeeWageRequest](docs/GetEmployeeWageRequest.md)
 - [GetEmployeeWageResponse](docs/GetEmployeeWageResponse.md)
 - [GetShiftRequest](docs/GetShiftRequest.md)
 - [GetShiftResponse](docs/GetShiftResponse.md)
 - [InventoryAdjustment](docs/InventoryAdjustment.md)
 - [InventoryChange](docs/InventoryChange.md)
 - [InventoryCount](docs/InventoryCount.md)
 - [InventoryPhysicalCount](docs/InventoryPhysicalCount.md)
 - [InventoryTransfer](docs/InventoryTransfer.md)
 - [ItemVariationLocationOverrides](docs/ItemVariationLocationOverrides.md)
 - [ListAdditionalRecipientReceivableRefundsRequest](docs/ListAdditionalRecipientReceivableRefundsRequest.md)
 - [ListAdditionalRecipientReceivableRefundsResponse](docs/ListAdditionalRecipientReceivableRefundsResponse.md)
 - [ListAdditionalRecipientReceivablesRequest](docs/ListAdditionalRecipientReceivablesRequest.md)
 - [ListAdditionalRecipientReceivablesResponse](docs/ListAdditionalRecipientReceivablesResponse.md)
 - [ListBreakTypesRequest](docs/ListBreakTypesRequest.md)
 - [ListBreakTypesResponse](docs/ListBreakTypesResponse.md)
 - [ListCatalogRequest](docs/ListCatalogRequest.md)
 - [ListCatalogResponse](docs/ListCatalogResponse.md)
 - [ListCustomersRequest](docs/ListCustomersRequest.md)
 - [ListCustomersResponse](docs/ListCustomersResponse.md)
 - [ListEmployeeWagesRequest](docs/ListEmployeeWagesRequest.md)
 - [ListEmployeeWagesResponse](docs/ListEmployeeWagesResponse.md)
 - [ListEmployeesRequest](docs/ListEmployeesRequest.md)
 - [ListEmployeesResponse](docs/ListEmployeesResponse.md)
 - [ListLocationsRequest](docs/ListLocationsRequest.md)
 - [ListLocationsResponse](docs/ListLocationsResponse.md)
 - [ListRefundsRequest](docs/ListRefundsRequest.md)
 - [ListRefundsResponse](docs/ListRefundsResponse.md)
 - [ListTransactionsRequest](docs/ListTransactionsRequest.md)
 - [ListTransactionsResponse](docs/ListTransactionsResponse.md)
 - [ListWorkweekConfigsRequest](docs/ListWorkweekConfigsRequest.md)
 - [ListWorkweekConfigsResponse](docs/ListWorkweekConfigsResponse.md)
 - [Location](docs/Location.md)
 - [MeasurementUnit](docs/MeasurementUnit.md)
 - [MeasurementUnitCustom](docs/MeasurementUnitCustom.md)
 - [ModelBreak](docs/ModelBreak.md)
 - [Money](docs/Money.md)
 - [ObtainTokenRequest](docs/ObtainTokenRequest.md)
 - [ObtainTokenResponse](docs/ObtainTokenResponse.md)
 - [Order](docs/Order.md)
 - [OrderEntry](docs/OrderEntry.md)
 - [OrderFulfillment](docs/OrderFulfillment.md)
 - [OrderFulfillmentPickupDetails](docs/OrderFulfillmentPickupDetails.md)
 - [OrderFulfillmentRecipient](docs/OrderFulfillmentRecipient.md)
 - [OrderLineItem](docs/OrderLineItem.md)
 - [OrderLineItemDiscount](docs/OrderLineItemDiscount.md)
 - [OrderLineItemModifier](docs/OrderLineItemModifier.md)
 - [OrderLineItemTax](docs/OrderLineItemTax.md)
 - [OrderMoneyAmounts](docs/OrderMoneyAmounts.md)
 - [OrderQuantityUnit](docs/OrderQuantityUnit.md)
 - [OrderReturn](docs/OrderReturn.md)
 - [OrderReturnDiscount](docs/OrderReturnDiscount.md)
 - [OrderReturnLineItem](docs/OrderReturnLineItem.md)
 - [OrderReturnLineItemModifier](docs/OrderReturnLineItemModifier.md)
 - [OrderReturnServiceCharge](docs/OrderReturnServiceCharge.md)
 - [OrderReturnTax](docs/OrderReturnTax.md)
 - [OrderRoundingAdjustment](docs/OrderRoundingAdjustment.md)
 - [OrderServiceCharge](docs/OrderServiceCharge.md)
 - [OrderSource](docs/OrderSource.md)
 - [Refund](docs/Refund.md)
 - [RegisterDomainRequest](docs/RegisterDomainRequest.md)
 - [RegisterDomainResponse](docs/RegisterDomainResponse.md)
 - [RenewTokenRequest](docs/RenewTokenRequest.md)
 - [RenewTokenResponse](docs/RenewTokenResponse.md)
 - [RetrieveCatalogObjectRequest](docs/RetrieveCatalogObjectRequest.md)
 - [RetrieveCatalogObjectResponse](docs/RetrieveCatalogObjectResponse.md)
 - [RetrieveCustomerRequest](docs/RetrieveCustomerRequest.md)
 - [RetrieveCustomerResponse](docs/RetrieveCustomerResponse.md)
 - [RetrieveEmployeeRequest](docs/RetrieveEmployeeRequest.md)
 - [RetrieveEmployeeResponse](docs/RetrieveEmployeeResponse.md)
 - [RetrieveInventoryAdjustmentRequest](docs/RetrieveInventoryAdjustmentRequest.md)
 - [RetrieveInventoryAdjustmentResponse](docs/RetrieveInventoryAdjustmentResponse.md)
 - [RetrieveInventoryChangesRequest](docs/RetrieveInventoryChangesRequest.md)
 - [RetrieveInventoryChangesResponse](docs/RetrieveInventoryChangesResponse.md)
 - [RetrieveInventoryCountRequest](docs/RetrieveInventoryCountRequest.md)
 - [RetrieveInventoryCountResponse](docs/RetrieveInventoryCountResponse.md)
 - [RetrieveInventoryPhysicalCountRequest](docs/RetrieveInventoryPhysicalCountRequest.md)
 - [RetrieveInventoryPhysicalCountResponse](docs/RetrieveInventoryPhysicalCountResponse.md)
 - [RetrieveTransactionRequest](docs/RetrieveTransactionRequest.md)
 - [RetrieveTransactionResponse](docs/RetrieveTransactionResponse.md)
 - [RevokeTokenRequest](docs/RevokeTokenRequest.md)
 - [RevokeTokenResponse](docs/RevokeTokenResponse.md)
 - [SearchCatalogObjectsRequest](docs/SearchCatalogObjectsRequest.md)
 - [SearchCatalogObjectsResponse](docs/SearchCatalogObjectsResponse.md)
 - [SearchCustomersRequest](docs/SearchCustomersRequest.md)
 - [SearchCustomersResponse](docs/SearchCustomersResponse.md)
 - [SearchOrdersCustomerFilter](docs/SearchOrdersCustomerFilter.md)
 - [SearchOrdersDateTimeFilter](docs/SearchOrdersDateTimeFilter.md)
 - [SearchOrdersFilter](docs/SearchOrdersFilter.md)
 - [SearchOrdersFulfillmentFilter](docs/SearchOrdersFulfillmentFilter.md)
 - [SearchOrdersQuery](docs/SearchOrdersQuery.md)
 - [SearchOrdersRequest](docs/SearchOrdersRequest.md)
 - [SearchOrdersResponse](docs/SearchOrdersResponse.md)
 - [SearchOrdersSort](docs/SearchOrdersSort.md)
 - [SearchOrdersSourceFilter](docs/SearchOrdersSourceFilter.md)
 - [SearchOrdersStateFilter](docs/SearchOrdersStateFilter.md)
 - [SearchShiftsRequest](docs/SearchShiftsRequest.md)
 - [SearchShiftsResponse](docs/SearchShiftsResponse.md)
 - [Shift](docs/Shift.md)
 - [ShiftFilter](docs/ShiftFilter.md)
 - [ShiftQuery](docs/ShiftQuery.md)
 - [ShiftSort](docs/ShiftSort.md)
 - [ShiftWage](docs/ShiftWage.md)
 - [ShiftWorkday](docs/ShiftWorkday.md)
 - [SourceApplication](docs/SourceApplication.md)
 - [StandardUnitDescription](docs/StandardUnitDescription.md)
 - [StandardUnitDescriptionGroup](docs/StandardUnitDescriptionGroup.md)
 - [Tender](docs/Tender.md)
 - [TenderCardDetails](docs/TenderCardDetails.md)
 - [TenderCashDetails](docs/TenderCashDetails.md)
 - [TimeRange](docs/TimeRange.md)
 - [Transaction](docs/Transaction.md)
 - [UpdateBreakTypeRequest](docs/UpdateBreakTypeRequest.md)
 - [UpdateBreakTypeResponse](docs/UpdateBreakTypeResponse.md)
 - [UpdateCustomerRequest](docs/UpdateCustomerRequest.md)
 - [UpdateCustomerResponse](docs/UpdateCustomerResponse.md)
 - [UpdateItemModifierListsRequest](docs/UpdateItemModifierListsRequest.md)
 - [UpdateItemModifierListsResponse](docs/UpdateItemModifierListsResponse.md)
 - [UpdateItemTaxesRequest](docs/UpdateItemTaxesRequest.md)
 - [UpdateItemTaxesResponse](docs/UpdateItemTaxesResponse.md)
 - [UpdateShiftRequest](docs/UpdateShiftRequest.md)
 - [UpdateShiftResponse](docs/UpdateShiftResponse.md)
 - [UpdateWorkweekConfigRequest](docs/UpdateWorkweekConfigRequest.md)
 - [UpdateWorkweekConfigResponse](docs/UpdateWorkweekConfigResponse.md)
 - [UpsertCatalogObjectRequest](docs/UpsertCatalogObjectRequest.md)
 - [UpsertCatalogObjectResponse](docs/UpsertCatalogObjectResponse.md)
 - [V1AdjustInventoryRequest](docs/V1AdjustInventoryRequest.md)
 - [V1ApplyFeeRequest](docs/V1ApplyFeeRequest.md)
 - [V1ApplyModifierListRequest](docs/V1ApplyModifierListRequest.md)
 - [V1BankAccount](docs/V1BankAccount.md)
 - [V1CashDrawerEvent](docs/V1CashDrawerEvent.md)
 - [V1CashDrawerShift](docs/V1CashDrawerShift.md)
 - [V1Category](docs/V1Category.md)
 - [V1CreateCategoryRequest](docs/V1CreateCategoryRequest.md)
 - [V1CreateDiscountRequest](docs/V1CreateDiscountRequest.md)
 - [V1CreateEmployeeRoleRequest](docs/V1CreateEmployeeRoleRequest.md)
 - [V1CreateFeeRequest](docs/V1CreateFeeRequest.md)
 - [V1CreateItemRequest](docs/V1CreateItemRequest.md)
 - [V1CreateModifierListRequest](docs/V1CreateModifierListRequest.md)
 - [V1CreateModifierOptionRequest](docs/V1CreateModifierOptionRequest.md)
 - [V1CreatePageRequest](docs/V1CreatePageRequest.md)
 - [V1CreateRefundRequest](docs/V1CreateRefundRequest.md)
 - [V1CreateVariationRequest](docs/V1CreateVariationRequest.md)
 - [V1DeleteCategoryRequest](docs/V1DeleteCategoryRequest.md)
 - [V1DeleteDiscountRequest](docs/V1DeleteDiscountRequest.md)
 - [V1DeleteFeeRequest](docs/V1DeleteFeeRequest.md)
 - [V1DeleteItemRequest](docs/V1DeleteItemRequest.md)
 - [V1DeleteModifierListRequest](docs/V1DeleteModifierListRequest.md)
 - [V1DeleteModifierOptionRequest](docs/V1DeleteModifierOptionRequest.md)
 - [V1DeletePageCellRequest](docs/V1DeletePageCellRequest.md)
 - [V1DeletePageRequest](docs/V1DeletePageRequest.md)
 - [V1DeleteTimecardRequest](docs/V1DeleteTimecardRequest.md)
 - [V1DeleteTimecardResponse](docs/V1DeleteTimecardResponse.md)
 - [V1DeleteVariationRequest](docs/V1DeleteVariationRequest.md)
 - [V1Discount](docs/V1Discount.md)
 - [V1Employee](docs/V1Employee.md)
 - [V1EmployeeRole](docs/V1EmployeeRole.md)
 - [V1Fee](docs/V1Fee.md)
 - [V1InventoryEntry](docs/V1InventoryEntry.md)
 - [V1Item](docs/V1Item.md)
 - [V1ItemImage](docs/V1ItemImage.md)
 - [V1ListBankAccountsRequest](docs/V1ListBankAccountsRequest.md)
 - [V1ListBankAccountsResponse](docs/V1ListBankAccountsResponse.md)
 - [V1ListCashDrawerShiftsRequest](docs/V1ListCashDrawerShiftsRequest.md)
 - [V1ListCashDrawerShiftsResponse](docs/V1ListCashDrawerShiftsResponse.md)
 - [V1ListCategoriesRequest](docs/V1ListCategoriesRequest.md)
 - [V1ListCategoriesResponse](docs/V1ListCategoriesResponse.md)
 - [V1ListDiscountsRequest](docs/V1ListDiscountsRequest.md)
 - [V1ListDiscountsResponse](docs/V1ListDiscountsResponse.md)
 - [V1ListEmployeeRolesRequest](docs/V1ListEmployeeRolesRequest.md)
 - [V1ListEmployeeRolesResponse](docs/V1ListEmployeeRolesResponse.md)
 - [V1ListEmployeesRequest](docs/V1ListEmployeesRequest.md)
 - [V1ListEmployeesResponse](docs/V1ListEmployeesResponse.md)
 - [V1ListFeesRequest](docs/V1ListFeesRequest.md)
 - [V1ListFeesResponse](docs/V1ListFeesResponse.md)
 - [V1ListInventoryRequest](docs/V1ListInventoryRequest.md)
 - [V1ListInventoryResponse](docs/V1ListInventoryResponse.md)
 - [V1ListItemsRequest](docs/V1ListItemsRequest.md)
 - [V1ListItemsResponse](docs/V1ListItemsResponse.md)
 - [V1ListLocationsRequest](docs/V1ListLocationsRequest.md)
 - [V1ListLocationsResponse](docs/V1ListLocationsResponse.md)
 - [V1ListModifierListsRequest](docs/V1ListModifierListsRequest.md)
 - [V1ListModifierListsResponse](docs/V1ListModifierListsResponse.md)
 - [V1ListOrdersRequest](docs/V1ListOrdersRequest.md)
 - [V1ListOrdersResponse](docs/V1ListOrdersResponse.md)
 - [V1ListPagesRequest](docs/V1ListPagesRequest.md)
 - [V1ListPagesResponse](docs/V1ListPagesResponse.md)
 - [V1ListPaymentsRequest](docs/V1ListPaymentsRequest.md)
 - [V1ListPaymentsResponse](docs/V1ListPaymentsResponse.md)
 - [V1ListRefundsRequest](docs/V1ListRefundsRequest.md)
 - [V1ListRefundsResponse](docs/V1ListRefundsResponse.md)
 - [V1ListSettlementsRequest](docs/V1ListSettlementsRequest.md)
 - [V1ListSettlementsResponse](docs/V1ListSettlementsResponse.md)
 - [V1ListTimecardEventsRequest](docs/V1ListTimecardEventsRequest.md)
 - [V1ListTimecardEventsResponse](docs/V1ListTimecardEventsResponse.md)
 - [V1ListTimecardsRequest](docs/V1ListTimecardsRequest.md)
 - [V1ListTimecardsResponse](docs/V1ListTimecardsResponse.md)
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
 - [V1PaymentSurcharge](docs/V1PaymentSurcharge.md)
 - [V1PaymentTax](docs/V1PaymentTax.md)
 - [V1PhoneNumber](docs/V1PhoneNumber.md)
 - [V1Refund](docs/V1Refund.md)
 - [V1RemoveFeeRequest](docs/V1RemoveFeeRequest.md)
 - [V1RemoveModifierListRequest](docs/V1RemoveModifierListRequest.md)
 - [V1RetrieveBankAccountRequest](docs/V1RetrieveBankAccountRequest.md)
 - [V1RetrieveBusinessRequest](docs/V1RetrieveBusinessRequest.md)
 - [V1RetrieveCashDrawerShiftRequest](docs/V1RetrieveCashDrawerShiftRequest.md)
 - [V1RetrieveEmployeeRequest](docs/V1RetrieveEmployeeRequest.md)
 - [V1RetrieveEmployeeRoleRequest](docs/V1RetrieveEmployeeRoleRequest.md)
 - [V1RetrieveItemRequest](docs/V1RetrieveItemRequest.md)
 - [V1RetrieveModifierListRequest](docs/V1RetrieveModifierListRequest.md)
 - [V1RetrieveOrderRequest](docs/V1RetrieveOrderRequest.md)
 - [V1RetrievePaymentRequest](docs/V1RetrievePaymentRequest.md)
 - [V1RetrieveSettlementRequest](docs/V1RetrieveSettlementRequest.md)
 - [V1RetrieveTimecardRequest](docs/V1RetrieveTimecardRequest.md)
 - [V1Settlement](docs/V1Settlement.md)
 - [V1SettlementEntry](docs/V1SettlementEntry.md)
 - [V1Tender](docs/V1Tender.md)
 - [V1Timecard](docs/V1Timecard.md)
 - [V1TimecardEvent](docs/V1TimecardEvent.md)
 - [V1UpdateCategoryRequest](docs/V1UpdateCategoryRequest.md)
 - [V1UpdateDiscountRequest](docs/V1UpdateDiscountRequest.md)
 - [V1UpdateEmployeeRequest](docs/V1UpdateEmployeeRequest.md)
 - [V1UpdateEmployeeRoleRequest](docs/V1UpdateEmployeeRoleRequest.md)
 - [V1UpdateFeeRequest](docs/V1UpdateFeeRequest.md)
 - [V1UpdateItemRequest](docs/V1UpdateItemRequest.md)
 - [V1UpdateModifierListRequest](docs/V1UpdateModifierListRequest.md)
 - [V1UpdateModifierOptionRequest](docs/V1UpdateModifierOptionRequest.md)
 - [V1UpdateOrderRequest](docs/V1UpdateOrderRequest.md)
 - [V1UpdatePageCellRequest](docs/V1UpdatePageCellRequest.md)
 - [V1UpdatePageRequest](docs/V1UpdatePageRequest.md)
 - [V1UpdateTimecardRequest](docs/V1UpdateTimecardRequest.md)
 - [V1UpdateVariationRequest](docs/V1UpdateVariationRequest.md)
 - [V1Variation](docs/V1Variation.md)
 - [VoidTransactionRequest](docs/VoidTransactionRequest.md)
 - [VoidTransactionResponse](docs/VoidTransactionResponse.md)
 - [WorkweekConfig](docs/WorkweekConfig.md)


## Documentation For Enums

 - [AggregationStrategy](docs/AggregationStrategy.md)
 - [CardBrand](docs/CardBrand.md)
 - [CatalogDiscountType](docs/CatalogDiscountType.md)
 - [CatalogItemProductType](docs/CatalogItemProductType.md)
 - [CatalogModifierListSelectionType](docs/CatalogModifierListSelectionType.md)
 - [CatalogObjectType](docs/CatalogObjectType.md)
 - [CatalogPricingType](docs/CatalogPricingType.md)
 - [Country](docs/Country.md)
 - [Currency](docs/Currency.md)
 - [CustomerCreationSource](docs/CustomerCreationSource.md)
 - [CustomerInclusionExclusion](docs/CustomerInclusionExclusion.md)
 - [CustomerSortField](docs/CustomerSortField.md)
 - [DayOfWeek](docs/DayOfWeek.md)
 - [EmployeeStatus](docs/EmployeeStatus.md)
 - [ErrorCategory](docs/ErrorCategory.md)
 - [ErrorCode](docs/ErrorCode.md)
 - [InventoryAlertType](docs/InventoryAlertType.md)
 - [InventoryChangeType](docs/InventoryChangeType.md)
 - [InventoryState](docs/InventoryState.md)
 - [LocationCapability](docs/LocationCapability.md)
 - [LocationStatus](docs/LocationStatus.md)
 - [LocationType](docs/LocationType.md)
 - [MeasurementUnitArea](docs/MeasurementUnitArea.md)
 - [MeasurementUnitGeneric](docs/MeasurementUnitGeneric.md)
 - [MeasurementUnitLength](docs/MeasurementUnitLength.md)
 - [MeasurementUnitVolume](docs/MeasurementUnitVolume.md)
 - [MeasurementUnitWeight](docs/MeasurementUnitWeight.md)
 - [OrderFulfillmentPickupDetailsScheduleType](docs/OrderFulfillmentPickupDetailsScheduleType.md)
 - [OrderFulfillmentState](docs/OrderFulfillmentState.md)
 - [OrderFulfillmentType](docs/OrderFulfillmentType.md)
 - [OrderLineItemDiscountScope](docs/OrderLineItemDiscountScope.md)
 - [OrderLineItemDiscountType](docs/OrderLineItemDiscountType.md)
 - [OrderLineItemTaxScope](docs/OrderLineItemTaxScope.md)
 - [OrderLineItemTaxType](docs/OrderLineItemTaxType.md)
 - [OrderServiceChargeCalculationPhase](docs/OrderServiceChargeCalculationPhase.md)
 - [OrderState](docs/OrderState.md)
 - [Product](docs/Product.md)
 - [RefundStatus](docs/RefundStatus.md)
 - [RegisterDomainResponseStatus](docs/RegisterDomainResponseStatus.md)
 - [SearchOrdersSortField](docs/SearchOrdersSortField.md)
 - [ShiftFilterStatus](docs/ShiftFilterStatus.md)
 - [ShiftSortField](docs/ShiftSortField.md)
 - [ShiftStatus](docs/ShiftStatus.md)
 - [ShiftWorkdayMatcher](docs/ShiftWorkdayMatcher.md)
 - [SortOrder](docs/SortOrder.md)
 - [TaxCalculationPhase](docs/TaxCalculationPhase.md)
 - [TaxInclusionType](docs/TaxInclusionType.md)
 - [TenderCardDetailsEntryMethod](docs/TenderCardDetailsEntryMethod.md)
 - [TenderCardDetailsStatus](docs/TenderCardDetailsStatus.md)
 - [TenderType](docs/TenderType.md)
 - [TransactionProduct](docs/TransactionProduct.md)
 - [V1AdjustInventoryRequestAdjustmentType](docs/V1AdjustInventoryRequestAdjustmentType.md)
 - [V1BankAccountType](docs/V1BankAccountType.md)
 - [V1CashDrawerEventEventType](docs/V1CashDrawerEventEventType.md)
 - [V1CashDrawerShiftEventType](docs/V1CashDrawerShiftEventType.md)
 - [V1CreateRefundRequestType](docs/V1CreateRefundRequestType.md)
 - [V1DiscountColor](docs/V1DiscountColor.md)
 - [V1DiscountDiscountType](docs/V1DiscountDiscountType.md)
 - [V1EmployeeRolePermissions](docs/V1EmployeeRolePermissions.md)
 - [V1EmployeeStatus](docs/V1EmployeeStatus.md)
 - [V1FeeAdjustmentType](docs/V1FeeAdjustmentType.md)
 - [V1FeeCalculationPhase](docs/V1FeeCalculationPhase.md)
 - [V1FeeInclusionType](docs/V1FeeInclusionType.md)
 - [V1FeeType](docs/V1FeeType.md)
 - [V1ItemColor](docs/V1ItemColor.md)
 - [V1ItemType](docs/V1ItemType.md)
 - [V1ItemVisibility](docs/V1ItemVisibility.md)
 - [V1ListEmployeesRequestStatus](docs/V1ListEmployeesRequestStatus.md)
 - [V1ListSettlementsRequestStatus](docs/V1ListSettlementsRequestStatus.md)
 - [V1MerchantAccountType](docs/V1MerchantAccountType.md)
 - [V1MerchantBusinessType](docs/V1MerchantBusinessType.md)
 - [V1ModifierListSelectionType](docs/V1ModifierListSelectionType.md)
 - [V1OrderHistoryEntryAction](docs/V1OrderHistoryEntryAction.md)
 - [V1OrderState](docs/V1OrderState.md)
 - [V1PageCellObjectType](docs/V1PageCellObjectType.md)
 - [V1PageCellPlaceholderType](docs/V1PageCellPlaceholderType.md)
 - [V1PaymentItemizationItemizationType](docs/V1PaymentItemizationItemizationType.md)
 - [V1PaymentSurchargeType](docs/V1PaymentSurchargeType.md)
 - [V1PaymentTaxInclusionType](docs/V1PaymentTaxInclusionType.md)
 - [V1RefundType](docs/V1RefundType.md)
 - [V1SettlementEntryType](docs/V1SettlementEntryType.md)
 - [V1SettlementStatus](docs/V1SettlementStatus.md)
 - [V1TenderCardBrand](docs/V1TenderCardBrand.md)
 - [V1TenderEntryMethod](docs/V1TenderEntryMethod.md)
 - [V1TenderType](docs/V1TenderType.md)
 - [V1TimecardEventEventType](docs/V1TimecardEventEventType.md)
 - [V1UpdateModifierListRequestSelectionType](docs/V1UpdateModifierListRequestSelectionType.md)
 - [V1UpdateOrderRequestAction](docs/V1UpdateOrderRequestAction.md)
 - [V1VariationInventoryAlertType](docs/V1VariationInventoryAlertType.md)
 - [V1VariationPricingType](docs/V1VariationPricingType.md)
 - [Weekday](docs/Weekday.md)


## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: `https://connect.squareup.com/oauth2/authorize`
- **Scopes**: 
 - **BANK_ACCOUNTS_READ**: __HTTP Method__: `GET`  Grants read access to bank account information associated with the targeted Square account. For example, to call the Connect v1 ListBankAccounts endpoint.
 - **CUSTOMERS_READ**: __HTTP Method__: `GET`  Grants read access to customer information. For example, to call the ListCustomers endpoint.
 - **CUSTOMERS_WRITE**: __HTTP Method__: `POST`, `PUT`, `DELETE`  Grants write access to customer information. For example, to create and update customer profiles.
 - **EMPLOYEES_READ**: __HTTP Method__: `GET`  Grants read access to employee profile information. For example, to call the Connect v1 Employees API.
 - **EMPLOYEES_WRITE**: __HTTP Method__: `POST`, `PUT`, `DELETE`  Grants write access to employee profile information. For example, to create and modify employee profiles.
 - **INVENTORY_READ**: __HTTP Method__: `GET`  Grants read access to inventory information. For example, to call the RetrieveInventoryCount endpoint.
 - **INVENTORY_WRITE**: __HTTP Method__:  `POST`, `PUT`, `DELETE`  Grants write access to inventory information. For example, to call the BatchChangeInventory endpoint.
 - **ITEMS_READ**: __HTTP Method__: `GET`  Grants read access to business and location information. For example, to obtain a location ID for subsequent activity.
 - **ITEMS_WRITE**: __HTTP Method__: `POST`, `PUT`, `DELETE`  Grants write access to product catalog information. For example, to modify or add to a product catalog.
 - **MERCHANT_PROFILE_READ**: __HTTP Method__: `GET`  Grants read access to business and location information. For example, to obtain a location ID for subsequent activity.
 - **ORDERS_READ**: __HTTP Method__: `GET`  Grants read access to order information. For example, to call the BatchRetrieveOrders endpoint.
 - **ORDERS_WRITE**: __HTTP Method__: `POST`, `PUT`, `DELETE`  Grants write access to order information. For example, to call the CreateCheckout endpoint.
 - **PAYMENTS_READ**: __HTTP Method__: `GET`  Grants read access to transaction and refund information. For example, to call the RetrieveTransaction endpoint.
 - **PAYMENTS_WRITE**: __HTTP Method__: `POST`, `PUT`, `DELETE`  Grants write access to transaction and refunds information. For example, to process payments with the Transactions or Checkout API.
 - **PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS**: __HTTP Method__: `POST`, `PUT`, `DELETE`  Allow third party applications to deduct a portion of each transaction amount. __Required__ to use multiparty transaction functionality with the Transactions API.
 - **PAYMENTS_WRITE_IN_PERSON**: __HTTP Method__: `POST`, `PUT`, `DELETE`  Grants write access to transaction and refunds information. For example, to process in-person payments.
 - **SETTLEMENTS_READ**: __HTTP Method__: `GET`  Grants read access to settlement (deposit) information. For example, to call the Connect v1 ListSettlements endpoint.
 - **TIMECARDS_READ**: __HTTP Method__: `GET`  Grants read access to employee timecard information. For example, to call the Connect v1 ListTimecards endpoint.
 - **TIMECARDS_WRITE**: __HTTP Method__: `POST`, `PUT`, `DELETE`  Grants write access to employee timecard information. For example, to create and modify timecards.
 - **TIMECARDS_SETTINGS_READ**: __HTTP Method__: `GET`  Grants read access to employee timecard settings information. For example, to call the GetBreakType endpoint.
 - **TIMECARDS_SETTINGS_WRITE**: __HTTP Method__: `POST`, `PUT`, `DELETE`  Grants write access to employee timecard settings information. For example, to call the UpdateBreakType endpoint.

## oauth2ClientSecret

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Pagination of V1 Endpoints

V1 Endpoints return pagination information via HTTP headers. In order to obtain
response headers and extract the `batch_token` parameter you will need to get it
from the response object after each call as follows:

### Example

```python
from __future__ import print_function

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.v1_employees_api import V1EmployeesApi

# create an instance of the V1 Employee API class
api_instance = V1EmployeesApi()
# setup authorization
api_instance.api_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
has_next_page = True
token = None

try:
    while has_next_page:
        # ListEmployeeRoles
        api_response = api_instance.list_employee_roles(batch_token=token)
        print (api_response.locations)

        token = api_instance.api_client.last_response.getbatch_token()
        has_next_page = token != None
except ApiException as e:
    print ('Exception when calling V1EmployeesApi->list_employee_roles: %s\n' % e)
```

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
