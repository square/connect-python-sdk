# Square Connect Python SDK Technical Reference

---
## The Square Connect Python SDK is retired (EOL) as of 2019-08-15 and will no longer receive bug fixes or product updates.
---

## Requirements

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
*ApplePayApi* | [**register_domain**](ApplePayApi.md#register_domain) | **POST** /v2/apple-pay/domains
*CatalogApi* | [**batch_delete_catalog_objects**](CatalogApi.md#batch_delete_catalog_objects) | **POST** /v2/catalog/batch-delete
*CatalogApi* | [**batch_retrieve_catalog_objects**](CatalogApi.md#batch_retrieve_catalog_objects) | **POST** /v2/catalog/batch-retrieve
*CatalogApi* | [**batch_upsert_catalog_objects**](CatalogApi.md#batch_upsert_catalog_objects) | **POST** /v2/catalog/batch-upsert
*CatalogApi* | [**catalog_info**](CatalogApi.md#catalog_info) | **GET** /v2/catalog/info
*CatalogApi* | [**delete_catalog_object**](CatalogApi.md#delete_catalog_object) | **DELETE** /v2/catalog/object/{object_id}
*CatalogApi* | [**list_catalog**](CatalogApi.md#list_catalog) | **GET** /v2/catalog/list
*CatalogApi* | [**retrieve_catalog_object**](CatalogApi.md#retrieve_catalog_object) | **GET** /v2/catalog/object/{object_id}
*CatalogApi* | [**search_catalog_objects**](CatalogApi.md#search_catalog_objects) | **POST** /v2/catalog/search
*CatalogApi* | [**update_item_modifier_lists**](CatalogApi.md#update_item_modifier_lists) | **POST** /v2/catalog/update-item-modifier-lists
*CatalogApi* | [**update_item_taxes**](CatalogApi.md#update_item_taxes) | **POST** /v2/catalog/update-item-taxes
*CatalogApi* | [**upsert_catalog_object**](CatalogApi.md#upsert_catalog_object) | **POST** /v2/catalog/object
*CheckoutApi* | [**create_checkout**](CheckoutApi.md#create_checkout) | **POST** /v2/locations/{location_id}/checkouts
*CustomersApi* | [**create_customer**](CustomersApi.md#create_customer) | **POST** /v2/customers
*CustomersApi* | [**create_customer_card**](CustomersApi.md#create_customer_card) | **POST** /v2/customers/{customer_id}/cards
*CustomersApi* | [**delete_customer**](CustomersApi.md#delete_customer) | **DELETE** /v2/customers/{customer_id}
*CustomersApi* | [**delete_customer_card**](CustomersApi.md#delete_customer_card) | **DELETE** /v2/customers/{customer_id}/cards/{card_id}
*CustomersApi* | [**list_customers**](CustomersApi.md#list_customers) | **GET** /v2/customers
*CustomersApi* | [**retrieve_customer**](CustomersApi.md#retrieve_customer) | **GET** /v2/customers/{customer_id}
*CustomersApi* | [**search_customers**](CustomersApi.md#search_customers) | **POST** /v2/customers/search
*CustomersApi* | [**update_customer**](CustomersApi.md#update_customer) | **PUT** /v2/customers/{customer_id}
*EmployeesApi* | [**list_employees**](EmployeesApi.md#list_employees) | **GET** /v2/employees
*EmployeesApi* | [**retrieve_employee**](EmployeesApi.md#retrieve_employee) | **GET** /v2/employees/{id}
*InventoryApi* | [**batch_change_inventory**](InventoryApi.md#batch_change_inventory) | **POST** /v2/inventory/batch-change
*InventoryApi* | [**batch_retrieve_inventory_changes**](InventoryApi.md#batch_retrieve_inventory_changes) | **POST** /v2/inventory/batch-retrieve-changes
*InventoryApi* | [**batch_retrieve_inventory_counts**](InventoryApi.md#batch_retrieve_inventory_counts) | **POST** /v2/inventory/batch-retrieve-counts
*InventoryApi* | [**retrieve_inventory_adjustment**](InventoryApi.md#retrieve_inventory_adjustment) | **GET** /v2/inventory/adjustment/{adjustment_id}
*InventoryApi* | [**retrieve_inventory_changes**](InventoryApi.md#retrieve_inventory_changes) | **GET** /v2/inventory/{catalog_object_id}/changes
*InventoryApi* | [**retrieve_inventory_count**](InventoryApi.md#retrieve_inventory_count) | **GET** /v2/inventory/{catalog_object_id}
*InventoryApi* | [**retrieve_inventory_physical_count**](InventoryApi.md#retrieve_inventory_physical_count) | **GET** /v2/inventory/physical-count/{physical_count_id}
*LaborApi* | [**create_break_type**](LaborApi.md#create_break_type) | **POST** /v2/labor/break-types
*LaborApi* | [**create_shift**](LaborApi.md#create_shift) | **POST** /v2/labor/shifts
*LaborApi* | [**delete_break_type**](LaborApi.md#delete_break_type) | **DELETE** /v2/labor/break-types/{id}
*LaborApi* | [**delete_shift**](LaborApi.md#delete_shift) | **DELETE** /v2/labor/shifts/{id}
*LaborApi* | [**get_break_type**](LaborApi.md#get_break_type) | **GET** /v2/labor/break-types/{id}
*LaborApi* | [**get_employee_wage**](LaborApi.md#get_employee_wage) | **GET** /v2/labor/employee-wages/{id}
*LaborApi* | [**get_shift**](LaborApi.md#get_shift) | **GET** /v2/labor/shifts/{id}
*LaborApi* | [**list_break_types**](LaborApi.md#list_break_types) | **GET** /v2/labor/break-types
*LaborApi* | [**list_employee_wages**](LaborApi.md#list_employee_wages) | **GET** /v2/labor/employee-wages
*LaborApi* | [**list_workweek_configs**](LaborApi.md#list_workweek_configs) | **GET** /v2/labor/workweek-configs
*LaborApi* | [**search_shifts**](LaborApi.md#search_shifts) | **POST** /v2/labor/shifts/search
*LaborApi* | [**update_break_type**](LaborApi.md#update_break_type) | **PUT** /v2/labor/break-types/{id}
*LaborApi* | [**update_shift**](LaborApi.md#update_shift) | **PUT** /v2/labor/shifts/{id}
*LaborApi* | [**update_workweek_config**](LaborApi.md#update_workweek_config) | **PUT** /v2/labor/workweek-configs/{id}
*LocationsApi* | [**list_locations**](LocationsApi.md#list_locations) | **GET** /v2/locations
*MobileAuthorizationApi* | [**create_mobile_authorization_code**](MobileAuthorizationApi.md#create_mobile_authorization_code) | **POST** /mobile/authorization-code
*OAuthApi* | [**obtain_token**](OAuthApi.md#obtain_token) | **POST** /oauth2/token
*OAuthApi* | [**renew_token**](OAuthApi.md#renew_token) | **POST** /oauth2/clients/{client_id}/access-token/renew
*OAuthApi* | [**revoke_token**](OAuthApi.md#revoke_token) | **POST** /oauth2/revoke
*OrdersApi* | [**batch_retrieve_orders**](OrdersApi.md#batch_retrieve_orders) | **POST** /v2/locations/{location_id}/orders/batch-retrieve
*OrdersApi* | [**create_order**](OrdersApi.md#create_order) | **POST** /v2/locations/{location_id}/orders
*OrdersApi* | [**search_orders**](OrdersApi.md#search_orders) | **POST** /v2/orders/search
*ReportingApi* | [**list_additional_recipient_receivable_refunds**](ReportingApi.md#list_additional_recipient_receivable_refunds) | **GET** /v2/locations/{location_id}/additional-recipient-receivable-refunds
*ReportingApi* | [**list_additional_recipient_receivables**](ReportingApi.md#list_additional_recipient_receivables) | **GET** /v2/locations/{location_id}/additional-recipient-receivables
*TransactionsApi* | [**capture_transaction**](TransactionsApi.md#capture_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/capture
*TransactionsApi* | [**charge**](TransactionsApi.md#charge) | **POST** /v2/locations/{location_id}/transactions
*TransactionsApi* | [**create_refund**](TransactionsApi.md#create_refund) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/refund
*TransactionsApi* | [**list_refunds**](TransactionsApi.md#list_refunds) | **GET** /v2/locations/{location_id}/refunds
*TransactionsApi* | [**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /v2/locations/{location_id}/transactions
*TransactionsApi* | [**retrieve_transaction**](TransactionsApi.md#retrieve_transaction) | **GET** /v2/locations/{location_id}/transactions/{transaction_id}
*TransactionsApi* | [**void_transaction**](TransactionsApi.md#void_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/void
*V1EmployeesApi* | [**create_employee**](V1EmployeesApi.md#create_employee) | **POST** /v1/me/employees
*V1EmployeesApi* | [**create_employee_role**](V1EmployeesApi.md#create_employee_role) | **POST** /v1/me/roles
*V1EmployeesApi* | [**create_timecard**](V1EmployeesApi.md#create_timecard) | **POST** /v1/me/timecards
*V1EmployeesApi* | [**delete_timecard**](V1EmployeesApi.md#delete_timecard) | **DELETE** /v1/me/timecards/{timecard_id}
*V1EmployeesApi* | [**list_cash_drawer_shifts**](V1EmployeesApi.md#list_cash_drawer_shifts) | **GET** /v1/{location_id}/cash-drawer-shifts
*V1EmployeesApi* | [**list_employee_roles**](V1EmployeesApi.md#list_employee_roles) | **GET** /v1/me/roles
*V1EmployeesApi* | [**list_employees**](V1EmployeesApi.md#list_employees) | **GET** /v1/me/employees
*V1EmployeesApi* | [**list_timecard_events**](V1EmployeesApi.md#list_timecard_events) | **GET** /v1/me/timecards/{timecard_id}/events
*V1EmployeesApi* | [**list_timecards**](V1EmployeesApi.md#list_timecards) | **GET** /v1/me/timecards
*V1EmployeesApi* | [**retrieve_cash_drawer_shift**](V1EmployeesApi.md#retrieve_cash_drawer_shift) | **GET** /v1/{location_id}/cash-drawer-shifts/{shift_id}
*V1EmployeesApi* | [**retrieve_employee**](V1EmployeesApi.md#retrieve_employee) | **GET** /v1/me/employees/{employee_id}
*V1EmployeesApi* | [**retrieve_employee_role**](V1EmployeesApi.md#retrieve_employee_role) | **GET** /v1/me/roles/{role_id}
*V1EmployeesApi* | [**retrieve_timecard**](V1EmployeesApi.md#retrieve_timecard) | **GET** /v1/me/timecards/{timecard_id}
*V1EmployeesApi* | [**update_employee**](V1EmployeesApi.md#update_employee) | **PUT** /v1/me/employees/{employee_id}
*V1EmployeesApi* | [**update_employee_role**](V1EmployeesApi.md#update_employee_role) | **PUT** /v1/me/roles/{role_id}
*V1EmployeesApi* | [**update_timecard**](V1EmployeesApi.md#update_timecard) | **PUT** /v1/me/timecards/{timecard_id}
*V1ItemsApi* | [**adjust_inventory**](V1ItemsApi.md#adjust_inventory) | **POST** /v1/{location_id}/inventory/{variation_id}
*V1ItemsApi* | [**apply_fee**](V1ItemsApi.md#apply_fee) | **PUT** /v1/{location_id}/items/{item_id}/fees/{fee_id}
*V1ItemsApi* | [**apply_modifier_list**](V1ItemsApi.md#apply_modifier_list) | **PUT** /v1/{location_id}/items/{item_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**create_category**](V1ItemsApi.md#create_category) | **POST** /v1/{location_id}/categories
*V1ItemsApi* | [**create_discount**](V1ItemsApi.md#create_discount) | **POST** /v1/{location_id}/discounts
*V1ItemsApi* | [**create_fee**](V1ItemsApi.md#create_fee) | **POST** /v1/{location_id}/fees
*V1ItemsApi* | [**create_item**](V1ItemsApi.md#create_item) | **POST** /v1/{location_id}/items
*V1ItemsApi* | [**create_modifier_list**](V1ItemsApi.md#create_modifier_list) | **POST** /v1/{location_id}/modifier-lists
*V1ItemsApi* | [**create_modifier_option**](V1ItemsApi.md#create_modifier_option) | **POST** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options
*V1ItemsApi* | [**create_page**](V1ItemsApi.md#create_page) | **POST** /v1/{location_id}/pages
*V1ItemsApi* | [**create_variation**](V1ItemsApi.md#create_variation) | **POST** /v1/{location_id}/items/{item_id}/variations
*V1ItemsApi* | [**delete_category**](V1ItemsApi.md#delete_category) | **DELETE** /v1/{location_id}/categories/{category_id}
*V1ItemsApi* | [**delete_discount**](V1ItemsApi.md#delete_discount) | **DELETE** /v1/{location_id}/discounts/{discount_id}
*V1ItemsApi* | [**delete_fee**](V1ItemsApi.md#delete_fee) | **DELETE** /v1/{location_id}/fees/{fee_id}
*V1ItemsApi* | [**delete_item**](V1ItemsApi.md#delete_item) | **DELETE** /v1/{location_id}/items/{item_id}
*V1ItemsApi* | [**delete_modifier_list**](V1ItemsApi.md#delete_modifier_list) | **DELETE** /v1/{location_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**delete_modifier_option**](V1ItemsApi.md#delete_modifier_option) | **DELETE** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options/{modifier_option_id}
*V1ItemsApi* | [**delete_page**](V1ItemsApi.md#delete_page) | **DELETE** /v1/{location_id}/pages/{page_id}
*V1ItemsApi* | [**delete_page_cell**](V1ItemsApi.md#delete_page_cell) | **DELETE** /v1/{location_id}/pages/{page_id}/cells
*V1ItemsApi* | [**delete_variation**](V1ItemsApi.md#delete_variation) | **DELETE** /v1/{location_id}/items/{item_id}/variations/{variation_id}
*V1ItemsApi* | [**list_categories**](V1ItemsApi.md#list_categories) | **GET** /v1/{location_id}/categories
*V1ItemsApi* | [**list_discounts**](V1ItemsApi.md#list_discounts) | **GET** /v1/{location_id}/discounts
*V1ItemsApi* | [**list_fees**](V1ItemsApi.md#list_fees) | **GET** /v1/{location_id}/fees
*V1ItemsApi* | [**list_inventory**](V1ItemsApi.md#list_inventory) | **GET** /v1/{location_id}/inventory
*V1ItemsApi* | [**list_items**](V1ItemsApi.md#list_items) | **GET** /v1/{location_id}/items
*V1ItemsApi* | [**list_modifier_lists**](V1ItemsApi.md#list_modifier_lists) | **GET** /v1/{location_id}/modifier-lists
*V1ItemsApi* | [**list_pages**](V1ItemsApi.md#list_pages) | **GET** /v1/{location_id}/pages
*V1ItemsApi* | [**remove_fee**](V1ItemsApi.md#remove_fee) | **DELETE** /v1/{location_id}/items/{item_id}/fees/{fee_id}
*V1ItemsApi* | [**remove_modifier_list**](V1ItemsApi.md#remove_modifier_list) | **DELETE** /v1/{location_id}/items/{item_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**retrieve_item**](V1ItemsApi.md#retrieve_item) | **GET** /v1/{location_id}/items/{item_id}
*V1ItemsApi* | [**retrieve_modifier_list**](V1ItemsApi.md#retrieve_modifier_list) | **GET** /v1/{location_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**update_category**](V1ItemsApi.md#update_category) | **PUT** /v1/{location_id}/categories/{category_id}
*V1ItemsApi* | [**update_discount**](V1ItemsApi.md#update_discount) | **PUT** /v1/{location_id}/discounts/{discount_id}
*V1ItemsApi* | [**update_fee**](V1ItemsApi.md#update_fee) | **PUT** /v1/{location_id}/fees/{fee_id}
*V1ItemsApi* | [**update_item**](V1ItemsApi.md#update_item) | **PUT** /v1/{location_id}/items/{item_id}
*V1ItemsApi* | [**update_modifier_list**](V1ItemsApi.md#update_modifier_list) | **PUT** /v1/{location_id}/modifier-lists/{modifier_list_id}
*V1ItemsApi* | [**update_modifier_option**](V1ItemsApi.md#update_modifier_option) | **PUT** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options/{modifier_option_id}
*V1ItemsApi* | [**update_page**](V1ItemsApi.md#update_page) | **PUT** /v1/{location_id}/pages/{page_id}
*V1ItemsApi* | [**update_page_cell**](V1ItemsApi.md#update_page_cell) | **PUT** /v1/{location_id}/pages/{page_id}/cells
*V1ItemsApi* | [**update_variation**](V1ItemsApi.md#update_variation) | **PUT** /v1/{location_id}/items/{item_id}/variations/{variation_id}
*V1LocationsApi* | [**list_locations**](V1LocationsApi.md#list_locations) | **GET** /v1/me/locations
*V1LocationsApi* | [**retrieve_business**](V1LocationsApi.md#retrieve_business) | **GET** /v1/me
*V1TransactionsApi* | [**create_refund**](V1TransactionsApi.md#create_refund) | **POST** /v1/{location_id}/refunds
*V1TransactionsApi* | [**list_bank_accounts**](V1TransactionsApi.md#list_bank_accounts) | **GET** /v1/{location_id}/bank-accounts
*V1TransactionsApi* | [**list_orders**](V1TransactionsApi.md#list_orders) | **GET** /v1/{location_id}/orders
*V1TransactionsApi* | [**list_payments**](V1TransactionsApi.md#list_payments) | **GET** /v1/{location_id}/payments
*V1TransactionsApi* | [**list_refunds**](V1TransactionsApi.md#list_refunds) | **GET** /v1/{location_id}/refunds
*V1TransactionsApi* | [**list_settlements**](V1TransactionsApi.md#list_settlements) | **GET** /v1/{location_id}/settlements
*V1TransactionsApi* | [**retrieve_bank_account**](V1TransactionsApi.md#retrieve_bank_account) | **GET** /v1/{location_id}/bank-accounts/{bank_account_id}
*V1TransactionsApi* | [**retrieve_order**](V1TransactionsApi.md#retrieve_order) | **GET** /v1/{location_id}/orders/{order_id}
*V1TransactionsApi* | [**retrieve_payment**](V1TransactionsApi.md#retrieve_payment) | **GET** /v1/{location_id}/payments/{payment_id}
*V1TransactionsApi* | [**retrieve_settlement**](V1TransactionsApi.md#retrieve_settlement) | **GET** /v1/{location_id}/settlements/{settlement_id}
*V1TransactionsApi* | [**update_order**](V1TransactionsApi.md#update_order) | **PUT** /v1/{location_id}/orders/{order_id}


## Documentation For Models

 - [AdditionalRecipient](AdditionalRecipient.md)
 - [AdditionalRecipientReceivable](AdditionalRecipientReceivable.md)
 - [AdditionalRecipientReceivableRefund](AdditionalRecipientReceivableRefund.md)
 - [Address](Address.md)
 - [BatchChangeInventoryRequest](BatchChangeInventoryRequest.md)
 - [BatchChangeInventoryResponse](BatchChangeInventoryResponse.md)
 - [BatchDeleteCatalogObjectsRequest](BatchDeleteCatalogObjectsRequest.md)
 - [BatchDeleteCatalogObjectsResponse](BatchDeleteCatalogObjectsResponse.md)
 - [BatchRetrieveCatalogObjectsRequest](BatchRetrieveCatalogObjectsRequest.md)
 - [BatchRetrieveCatalogObjectsResponse](BatchRetrieveCatalogObjectsResponse.md)
 - [BatchRetrieveInventoryChangesRequest](BatchRetrieveInventoryChangesRequest.md)
 - [BatchRetrieveInventoryChangesResponse](BatchRetrieveInventoryChangesResponse.md)
 - [BatchRetrieveInventoryCountsRequest](BatchRetrieveInventoryCountsRequest.md)
 - [BatchRetrieveInventoryCountsResponse](BatchRetrieveInventoryCountsResponse.md)
 - [BatchRetrieveOrdersRequest](BatchRetrieveOrdersRequest.md)
 - [BatchRetrieveOrdersResponse](BatchRetrieveOrdersResponse.md)
 - [BatchUpsertCatalogObjectsRequest](BatchUpsertCatalogObjectsRequest.md)
 - [BatchUpsertCatalogObjectsResponse](BatchUpsertCatalogObjectsResponse.md)
 - [BreakType](BreakType.md)
 - [BusinessHours](BusinessHours.md)
 - [BusinessHoursPeriod](BusinessHoursPeriod.md)
 - [CaptureTransactionRequest](CaptureTransactionRequest.md)
 - [CaptureTransactionResponse](CaptureTransactionResponse.md)
 - [Card](Card.md)
 - [CatalogCategory](CatalogCategory.md)
 - [CatalogDiscount](CatalogDiscount.md)
 - [CatalogIdMapping](CatalogIdMapping.md)
 - [CatalogImage](CatalogImage.md)
 - [CatalogInfoRequest](CatalogInfoRequest.md)
 - [CatalogInfoResponse](CatalogInfoResponse.md)
 - [CatalogInfoResponseLimits](CatalogInfoResponseLimits.md)
 - [CatalogItem](CatalogItem.md)
 - [CatalogItemModifierListInfo](CatalogItemModifierListInfo.md)
 - [CatalogItemOption](CatalogItemOption.md)
 - [CatalogItemOptionForItem](CatalogItemOptionForItem.md)
 - [CatalogItemOptionValue](CatalogItemOptionValue.md)
 - [CatalogItemOptionValueForItemVariation](CatalogItemOptionValueForItemVariation.md)
 - [CatalogItemVariation](CatalogItemVariation.md)
 - [CatalogMeasurementUnit](CatalogMeasurementUnit.md)
 - [CatalogModifier](CatalogModifier.md)
 - [CatalogModifierList](CatalogModifierList.md)
 - [CatalogModifierOverride](CatalogModifierOverride.md)
 - [CatalogObject](CatalogObject.md)
 - [CatalogObjectBatch](CatalogObjectBatch.md)
 - [CatalogPricingRule](CatalogPricingRule.md)
 - [CatalogProductSet](CatalogProductSet.md)
 - [CatalogQuery](CatalogQuery.md)
 - [CatalogQueryExact](CatalogQueryExact.md)
 - [CatalogQueryItemVariationsForItemOptionValues](CatalogQueryItemVariationsForItemOptionValues.md)
 - [CatalogQueryItemsForItemOptions](CatalogQueryItemsForItemOptions.md)
 - [CatalogQueryItemsForModifierList](CatalogQueryItemsForModifierList.md)
 - [CatalogQueryItemsForTax](CatalogQueryItemsForTax.md)
 - [CatalogQueryPrefix](CatalogQueryPrefix.md)
 - [CatalogQueryRange](CatalogQueryRange.md)
 - [CatalogQuerySortedAttribute](CatalogQuerySortedAttribute.md)
 - [CatalogQueryText](CatalogQueryText.md)
 - [CatalogTax](CatalogTax.md)
 - [CatalogTimePeriod](CatalogTimePeriod.md)
 - [CatalogV1Id](CatalogV1Id.md)
 - [ChargeRequest](ChargeRequest.md)
 - [ChargeRequestAdditionalRecipient](ChargeRequestAdditionalRecipient.md)
 - [ChargeResponse](ChargeResponse.md)
 - [Checkout](Checkout.md)
 - [Coordinates](Coordinates.md)
 - [CreateBreakTypeRequest](CreateBreakTypeRequest.md)
 - [CreateBreakTypeResponse](CreateBreakTypeResponse.md)
 - [CreateCheckoutRequest](CreateCheckoutRequest.md)
 - [CreateCheckoutResponse](CreateCheckoutResponse.md)
 - [CreateCustomerCardRequest](CreateCustomerCardRequest.md)
 - [CreateCustomerCardResponse](CreateCustomerCardResponse.md)
 - [CreateCustomerRequest](CreateCustomerRequest.md)
 - [CreateCustomerResponse](CreateCustomerResponse.md)
 - [CreateMobileAuthorizationCodeRequest](CreateMobileAuthorizationCodeRequest.md)
 - [CreateMobileAuthorizationCodeResponse](CreateMobileAuthorizationCodeResponse.md)
 - [CreateOrderRequest](CreateOrderRequest.md)
 - [CreateOrderRequestDiscount](CreateOrderRequestDiscount.md)
 - [CreateOrderRequestLineItem](CreateOrderRequestLineItem.md)
 - [CreateOrderRequestModifier](CreateOrderRequestModifier.md)
 - [CreateOrderRequestTax](CreateOrderRequestTax.md)
 - [CreateOrderResponse](CreateOrderResponse.md)
 - [CreateRefundRequest](CreateRefundRequest.md)
 - [CreateRefundResponse](CreateRefundResponse.md)
 - [CreateShiftRequest](CreateShiftRequest.md)
 - [CreateShiftResponse](CreateShiftResponse.md)
 - [Customer](Customer.md)
 - [CustomerCreationSourceFilter](CustomerCreationSourceFilter.md)
 - [CustomerFilter](CustomerFilter.md)
 - [CustomerGroupInfo](CustomerGroupInfo.md)
 - [CustomerPreferences](CustomerPreferences.md)
 - [CustomerQuery](CustomerQuery.md)
 - [CustomerSort](CustomerSort.md)
 - [DateRange](DateRange.md)
 - [DeleteBreakTypeRequest](DeleteBreakTypeRequest.md)
 - [DeleteBreakTypeResponse](DeleteBreakTypeResponse.md)
 - [DeleteCatalogObjectRequest](DeleteCatalogObjectRequest.md)
 - [DeleteCatalogObjectResponse](DeleteCatalogObjectResponse.md)
 - [DeleteCustomerCardRequest](DeleteCustomerCardRequest.md)
 - [DeleteCustomerCardResponse](DeleteCustomerCardResponse.md)
 - [DeleteCustomerRequest](DeleteCustomerRequest.md)
 - [DeleteCustomerResponse](DeleteCustomerResponse.md)
 - [DeleteShiftRequest](DeleteShiftRequest.md)
 - [DeleteShiftResponse](DeleteShiftResponse.md)
 - [Device](Device.md)
 - [Employee](Employee.md)
 - [EmployeeWage](EmployeeWage.md)
 - [Error](Error.md)
 - [GetBreakTypeRequest](GetBreakTypeRequest.md)
 - [GetBreakTypeResponse](GetBreakTypeResponse.md)
 - [GetEmployeeWageRequest](GetEmployeeWageRequest.md)
 - [GetEmployeeWageResponse](GetEmployeeWageResponse.md)
 - [GetShiftRequest](GetShiftRequest.md)
 - [GetShiftResponse](GetShiftResponse.md)
 - [InventoryAdjustment](InventoryAdjustment.md)
 - [InventoryChange](InventoryChange.md)
 - [InventoryCount](InventoryCount.md)
 - [InventoryPhysicalCount](InventoryPhysicalCount.md)
 - [InventoryTransfer](InventoryTransfer.md)
 - [ItemVariationLocationOverrides](ItemVariationLocationOverrides.md)
 - [ListAdditionalRecipientReceivableRefundsRequest](ListAdditionalRecipientReceivableRefundsRequest.md)
 - [ListAdditionalRecipientReceivableRefundsResponse](ListAdditionalRecipientReceivableRefundsResponse.md)
 - [ListAdditionalRecipientReceivablesRequest](ListAdditionalRecipientReceivablesRequest.md)
 - [ListAdditionalRecipientReceivablesResponse](ListAdditionalRecipientReceivablesResponse.md)
 - [ListBreakTypesRequest](ListBreakTypesRequest.md)
 - [ListBreakTypesResponse](ListBreakTypesResponse.md)
 - [ListCatalogRequest](ListCatalogRequest.md)
 - [ListCatalogResponse](ListCatalogResponse.md)
 - [ListCustomersRequest](ListCustomersRequest.md)
 - [ListCustomersResponse](ListCustomersResponse.md)
 - [ListEmployeeWagesRequest](ListEmployeeWagesRequest.md)
 - [ListEmployeeWagesResponse](ListEmployeeWagesResponse.md)
 - [ListEmployeesRequest](ListEmployeesRequest.md)
 - [ListEmployeesResponse](ListEmployeesResponse.md)
 - [ListLocationsRequest](ListLocationsRequest.md)
 - [ListLocationsResponse](ListLocationsResponse.md)
 - [ListRefundsRequest](ListRefundsRequest.md)
 - [ListRefundsResponse](ListRefundsResponse.md)
 - [ListTransactionsRequest](ListTransactionsRequest.md)
 - [ListTransactionsResponse](ListTransactionsResponse.md)
 - [ListWorkweekConfigsRequest](ListWorkweekConfigsRequest.md)
 - [ListWorkweekConfigsResponse](ListWorkweekConfigsResponse.md)
 - [Location](Location.md)
 - [MeasurementUnit](MeasurementUnit.md)
 - [MeasurementUnitCustom](MeasurementUnitCustom.md)
 - [ModelBreak](ModelBreak.md)
 - [Money](Money.md)
 - [ObtainTokenRequest](ObtainTokenRequest.md)
 - [ObtainTokenResponse](ObtainTokenResponse.md)
 - [Order](Order.md)
 - [OrderEntry](OrderEntry.md)
 - [OrderFulfillment](OrderFulfillment.md)
 - [OrderFulfillmentPickupDetails](OrderFulfillmentPickupDetails.md)
 - [OrderFulfillmentRecipient](OrderFulfillmentRecipient.md)
 - [OrderLineItem](OrderLineItem.md)
 - [OrderLineItemDiscount](OrderLineItemDiscount.md)
 - [OrderLineItemModifier](OrderLineItemModifier.md)
 - [OrderLineItemTax](OrderLineItemTax.md)
 - [OrderMoneyAmounts](OrderMoneyAmounts.md)
 - [OrderQuantityUnit](OrderQuantityUnit.md)
 - [OrderReturn](OrderReturn.md)
 - [OrderReturnDiscount](OrderReturnDiscount.md)
 - [OrderReturnLineItem](OrderReturnLineItem.md)
 - [OrderReturnLineItemModifier](OrderReturnLineItemModifier.md)
 - [OrderReturnServiceCharge](OrderReturnServiceCharge.md)
 - [OrderReturnTax](OrderReturnTax.md)
 - [OrderRoundingAdjustment](OrderRoundingAdjustment.md)
 - [OrderServiceCharge](OrderServiceCharge.md)
 - [OrderSource](OrderSource.md)
 - [Refund](Refund.md)
 - [RegisterDomainRequest](RegisterDomainRequest.md)
 - [RegisterDomainResponse](RegisterDomainResponse.md)
 - [RenewTokenRequest](RenewTokenRequest.md)
 - [RenewTokenResponse](RenewTokenResponse.md)
 - [RetrieveCatalogObjectRequest](RetrieveCatalogObjectRequest.md)
 - [RetrieveCatalogObjectResponse](RetrieveCatalogObjectResponse.md)
 - [RetrieveCustomerRequest](RetrieveCustomerRequest.md)
 - [RetrieveCustomerResponse](RetrieveCustomerResponse.md)
 - [RetrieveEmployeeRequest](RetrieveEmployeeRequest.md)
 - [RetrieveEmployeeResponse](RetrieveEmployeeResponse.md)
 - [RetrieveInventoryAdjustmentRequest](RetrieveInventoryAdjustmentRequest.md)
 - [RetrieveInventoryAdjustmentResponse](RetrieveInventoryAdjustmentResponse.md)
 - [RetrieveInventoryChangesRequest](RetrieveInventoryChangesRequest.md)
 - [RetrieveInventoryChangesResponse](RetrieveInventoryChangesResponse.md)
 - [RetrieveInventoryCountRequest](RetrieveInventoryCountRequest.md)
 - [RetrieveInventoryCountResponse](RetrieveInventoryCountResponse.md)
 - [RetrieveInventoryPhysicalCountRequest](RetrieveInventoryPhysicalCountRequest.md)
 - [RetrieveInventoryPhysicalCountResponse](RetrieveInventoryPhysicalCountResponse.md)
 - [RetrieveTransactionRequest](RetrieveTransactionRequest.md)
 - [RetrieveTransactionResponse](RetrieveTransactionResponse.md)
 - [RevokeTokenRequest](RevokeTokenRequest.md)
 - [RevokeTokenResponse](RevokeTokenResponse.md)
 - [SearchCatalogObjectsRequest](SearchCatalogObjectsRequest.md)
 - [SearchCatalogObjectsResponse](SearchCatalogObjectsResponse.md)
 - [SearchCustomersRequest](SearchCustomersRequest.md)
 - [SearchCustomersResponse](SearchCustomersResponse.md)
 - [SearchOrdersCustomerFilter](SearchOrdersCustomerFilter.md)
 - [SearchOrdersDateTimeFilter](SearchOrdersDateTimeFilter.md)
 - [SearchOrdersFilter](SearchOrdersFilter.md)
 - [SearchOrdersFulfillmentFilter](SearchOrdersFulfillmentFilter.md)
 - [SearchOrdersQuery](SearchOrdersQuery.md)
 - [SearchOrdersRequest](SearchOrdersRequest.md)
 - [SearchOrdersResponse](SearchOrdersResponse.md)
 - [SearchOrdersSort](SearchOrdersSort.md)
 - [SearchOrdersSourceFilter](SearchOrdersSourceFilter.md)
 - [SearchOrdersStateFilter](SearchOrdersStateFilter.md)
 - [SearchShiftsRequest](SearchShiftsRequest.md)
 - [SearchShiftsResponse](SearchShiftsResponse.md)
 - [Shift](Shift.md)
 - [ShiftFilter](ShiftFilter.md)
 - [ShiftQuery](ShiftQuery.md)
 - [ShiftSort](ShiftSort.md)
 - [ShiftWage](ShiftWage.md)
 - [ShiftWorkday](ShiftWorkday.md)
 - [SourceApplication](SourceApplication.md)
 - [StandardUnitDescription](StandardUnitDescription.md)
 - [StandardUnitDescriptionGroup](StandardUnitDescriptionGroup.md)
 - [Tender](Tender.md)
 - [TenderCardDetails](TenderCardDetails.md)
 - [TenderCashDetails](TenderCashDetails.md)
 - [TimeRange](TimeRange.md)
 - [Transaction](Transaction.md)
 - [UpdateBreakTypeRequest](UpdateBreakTypeRequest.md)
 - [UpdateBreakTypeResponse](UpdateBreakTypeResponse.md)
 - [UpdateCustomerRequest](UpdateCustomerRequest.md)
 - [UpdateCustomerResponse](UpdateCustomerResponse.md)
 - [UpdateItemModifierListsRequest](UpdateItemModifierListsRequest.md)
 - [UpdateItemModifierListsResponse](UpdateItemModifierListsResponse.md)
 - [UpdateItemTaxesRequest](UpdateItemTaxesRequest.md)
 - [UpdateItemTaxesResponse](UpdateItemTaxesResponse.md)
 - [UpdateShiftRequest](UpdateShiftRequest.md)
 - [UpdateShiftResponse](UpdateShiftResponse.md)
 - [UpdateWorkweekConfigRequest](UpdateWorkweekConfigRequest.md)
 - [UpdateWorkweekConfigResponse](UpdateWorkweekConfigResponse.md)
 - [UpsertCatalogObjectRequest](UpsertCatalogObjectRequest.md)
 - [UpsertCatalogObjectResponse](UpsertCatalogObjectResponse.md)
 - [V1AdjustInventoryRequest](V1AdjustInventoryRequest.md)
 - [V1ApplyFeeRequest](V1ApplyFeeRequest.md)
 - [V1ApplyModifierListRequest](V1ApplyModifierListRequest.md)
 - [V1BankAccount](V1BankAccount.md)
 - [V1CashDrawerEvent](V1CashDrawerEvent.md)
 - [V1CashDrawerShift](V1CashDrawerShift.md)
 - [V1Category](V1Category.md)
 - [V1CreateCategoryRequest](V1CreateCategoryRequest.md)
 - [V1CreateDiscountRequest](V1CreateDiscountRequest.md)
 - [V1CreateEmployeeRoleRequest](V1CreateEmployeeRoleRequest.md)
 - [V1CreateFeeRequest](V1CreateFeeRequest.md)
 - [V1CreateItemRequest](V1CreateItemRequest.md)
 - [V1CreateModifierListRequest](V1CreateModifierListRequest.md)
 - [V1CreateModifierOptionRequest](V1CreateModifierOptionRequest.md)
 - [V1CreatePageRequest](V1CreatePageRequest.md)
 - [V1CreateRefundRequest](V1CreateRefundRequest.md)
 - [V1CreateVariationRequest](V1CreateVariationRequest.md)
 - [V1DeleteCategoryRequest](V1DeleteCategoryRequest.md)
 - [V1DeleteDiscountRequest](V1DeleteDiscountRequest.md)
 - [V1DeleteFeeRequest](V1DeleteFeeRequest.md)
 - [V1DeleteItemRequest](V1DeleteItemRequest.md)
 - [V1DeleteModifierListRequest](V1DeleteModifierListRequest.md)
 - [V1DeleteModifierOptionRequest](V1DeleteModifierOptionRequest.md)
 - [V1DeletePageCellRequest](V1DeletePageCellRequest.md)
 - [V1DeletePageRequest](V1DeletePageRequest.md)
 - [V1DeleteTimecardRequest](V1DeleteTimecardRequest.md)
 - [V1DeleteTimecardResponse](V1DeleteTimecardResponse.md)
 - [V1DeleteVariationRequest](V1DeleteVariationRequest.md)
 - [V1Discount](V1Discount.md)
 - [V1Employee](V1Employee.md)
 - [V1EmployeeRole](V1EmployeeRole.md)
 - [V1Fee](V1Fee.md)
 - [V1InventoryEntry](V1InventoryEntry.md)
 - [V1Item](V1Item.md)
 - [V1ItemImage](V1ItemImage.md)
 - [V1ListBankAccountsRequest](V1ListBankAccountsRequest.md)
 - [V1ListBankAccountsResponse](V1ListBankAccountsResponse.md)
 - [V1ListCashDrawerShiftsRequest](V1ListCashDrawerShiftsRequest.md)
 - [V1ListCashDrawerShiftsResponse](V1ListCashDrawerShiftsResponse.md)
 - [V1ListCategoriesRequest](V1ListCategoriesRequest.md)
 - [V1ListCategoriesResponse](V1ListCategoriesResponse.md)
 - [V1ListDiscountsRequest](V1ListDiscountsRequest.md)
 - [V1ListDiscountsResponse](V1ListDiscountsResponse.md)
 - [V1ListEmployeeRolesRequest](V1ListEmployeeRolesRequest.md)
 - [V1ListEmployeeRolesResponse](V1ListEmployeeRolesResponse.md)
 - [V1ListEmployeesRequest](V1ListEmployeesRequest.md)
 - [V1ListEmployeesResponse](V1ListEmployeesResponse.md)
 - [V1ListFeesRequest](V1ListFeesRequest.md)
 - [V1ListFeesResponse](V1ListFeesResponse.md)
 - [V1ListInventoryRequest](V1ListInventoryRequest.md)
 - [V1ListInventoryResponse](V1ListInventoryResponse.md)
 - [V1ListItemsRequest](V1ListItemsRequest.md)
 - [V1ListItemsResponse](V1ListItemsResponse.md)
 - [V1ListLocationsRequest](V1ListLocationsRequest.md)
 - [V1ListLocationsResponse](V1ListLocationsResponse.md)
 - [V1ListModifierListsRequest](V1ListModifierListsRequest.md)
 - [V1ListModifierListsResponse](V1ListModifierListsResponse.md)
 - [V1ListOrdersRequest](V1ListOrdersRequest.md)
 - [V1ListOrdersResponse](V1ListOrdersResponse.md)
 - [V1ListPagesRequest](V1ListPagesRequest.md)
 - [V1ListPagesResponse](V1ListPagesResponse.md)
 - [V1ListPaymentsRequest](V1ListPaymentsRequest.md)
 - [V1ListPaymentsResponse](V1ListPaymentsResponse.md)
 - [V1ListRefundsRequest](V1ListRefundsRequest.md)
 - [V1ListRefundsResponse](V1ListRefundsResponse.md)
 - [V1ListSettlementsRequest](V1ListSettlementsRequest.md)
 - [V1ListSettlementsResponse](V1ListSettlementsResponse.md)
 - [V1ListTimecardEventsRequest](V1ListTimecardEventsRequest.md)
 - [V1ListTimecardEventsResponse](V1ListTimecardEventsResponse.md)
 - [V1ListTimecardsRequest](V1ListTimecardsRequest.md)
 - [V1ListTimecardsResponse](V1ListTimecardsResponse.md)
 - [V1Merchant](V1Merchant.md)
 - [V1MerchantLocationDetails](V1MerchantLocationDetails.md)
 - [V1ModifierList](V1ModifierList.md)
 - [V1ModifierOption](V1ModifierOption.md)
 - [V1Money](V1Money.md)
 - [V1Order](V1Order.md)
 - [V1OrderHistoryEntry](V1OrderHistoryEntry.md)
 - [V1Page](V1Page.md)
 - [V1PageCell](V1PageCell.md)
 - [V1Payment](V1Payment.md)
 - [V1PaymentDiscount](V1PaymentDiscount.md)
 - [V1PaymentItemDetail](V1PaymentItemDetail.md)
 - [V1PaymentItemization](V1PaymentItemization.md)
 - [V1PaymentModifier](V1PaymentModifier.md)
 - [V1PaymentSurcharge](V1PaymentSurcharge.md)
 - [V1PaymentTax](V1PaymentTax.md)
 - [V1PhoneNumber](V1PhoneNumber.md)
 - [V1Refund](V1Refund.md)
 - [V1RemoveFeeRequest](V1RemoveFeeRequest.md)
 - [V1RemoveModifierListRequest](V1RemoveModifierListRequest.md)
 - [V1RetrieveBankAccountRequest](V1RetrieveBankAccountRequest.md)
 - [V1RetrieveBusinessRequest](V1RetrieveBusinessRequest.md)
 - [V1RetrieveCashDrawerShiftRequest](V1RetrieveCashDrawerShiftRequest.md)
 - [V1RetrieveEmployeeRequest](V1RetrieveEmployeeRequest.md)
 - [V1RetrieveEmployeeRoleRequest](V1RetrieveEmployeeRoleRequest.md)
 - [V1RetrieveItemRequest](V1RetrieveItemRequest.md)
 - [V1RetrieveModifierListRequest](V1RetrieveModifierListRequest.md)
 - [V1RetrieveOrderRequest](V1RetrieveOrderRequest.md)
 - [V1RetrievePaymentRequest](V1RetrievePaymentRequest.md)
 - [V1RetrieveSettlementRequest](V1RetrieveSettlementRequest.md)
 - [V1RetrieveTimecardRequest](V1RetrieveTimecardRequest.md)
 - [V1Settlement](V1Settlement.md)
 - [V1SettlementEntry](V1SettlementEntry.md)
 - [V1Tender](V1Tender.md)
 - [V1Timecard](V1Timecard.md)
 - [V1TimecardEvent](V1TimecardEvent.md)
 - [V1UpdateCategoryRequest](V1UpdateCategoryRequest.md)
 - [V1UpdateDiscountRequest](V1UpdateDiscountRequest.md)
 - [V1UpdateEmployeeRequest](V1UpdateEmployeeRequest.md)
 - [V1UpdateEmployeeRoleRequest](V1UpdateEmployeeRoleRequest.md)
 - [V1UpdateFeeRequest](V1UpdateFeeRequest.md)
 - [V1UpdateItemRequest](V1UpdateItemRequest.md)
 - [V1UpdateModifierListRequest](V1UpdateModifierListRequest.md)
 - [V1UpdateModifierOptionRequest](V1UpdateModifierOptionRequest.md)
 - [V1UpdateOrderRequest](V1UpdateOrderRequest.md)
 - [V1UpdatePageCellRequest](V1UpdatePageCellRequest.md)
 - [V1UpdatePageRequest](V1UpdatePageRequest.md)
 - [V1UpdateTimecardRequest](V1UpdateTimecardRequest.md)
 - [V1UpdateVariationRequest](V1UpdateVariationRequest.md)
 - [V1Variation](V1Variation.md)
 - [VoidTransactionRequest](VoidTransactionRequest.md)
 - [VoidTransactionResponse](VoidTransactionResponse.md)
 - [WorkweekConfig](WorkweekConfig.md)


## Documentation For Enums

 - [CardBrand](CardBrand.md)
 - [CatalogDiscountType](CatalogDiscountType.md)
 - [CatalogItemProductType](CatalogItemProductType.md)
 - [CatalogModifierListSelectionType](CatalogModifierListSelectionType.md)
 - [CatalogObjectType](CatalogObjectType.md)
 - [CatalogPricingType](CatalogPricingType.md)
 - [Country](Country.md)
 - [Currency](Currency.md)
 - [CustomerCreationSource](CustomerCreationSource.md)
 - [CustomerInclusionExclusion](CustomerInclusionExclusion.md)
 - [CustomerSortField](CustomerSortField.md)
 - [DayOfWeek](DayOfWeek.md)
 - [EmployeeStatus](EmployeeStatus.md)
 - [ErrorCategory](ErrorCategory.md)
 - [ErrorCode](ErrorCode.md)
 - [InventoryAlertType](InventoryAlertType.md)
 - [InventoryChangeType](InventoryChangeType.md)
 - [InventoryState](InventoryState.md)
 - [LocationCapability](LocationCapability.md)
 - [LocationStatus](LocationStatus.md)
 - [LocationType](LocationType.md)
 - [MeasurementUnitArea](MeasurementUnitArea.md)
 - [MeasurementUnitGeneric](MeasurementUnitGeneric.md)
 - [MeasurementUnitLength](MeasurementUnitLength.md)
 - [MeasurementUnitVolume](MeasurementUnitVolume.md)
 - [MeasurementUnitWeight](MeasurementUnitWeight.md)
 - [OrderFulfillmentPickupDetailsScheduleType](OrderFulfillmentPickupDetailsScheduleType.md)
 - [OrderFulfillmentState](OrderFulfillmentState.md)
 - [OrderFulfillmentType](OrderFulfillmentType.md)
 - [OrderLineItemDiscountScope](OrderLineItemDiscountScope.md)
 - [OrderLineItemDiscountType](OrderLineItemDiscountType.md)
 - [OrderLineItemTaxScope](OrderLineItemTaxScope.md)
 - [OrderLineItemTaxType](OrderLineItemTaxType.md)
 - [OrderServiceChargeCalculationPhase](OrderServiceChargeCalculationPhase.md)
 - [OrderState](OrderState.md)
 - [Product](Product.md)
 - [RefundStatus](RefundStatus.md)
 - [RegisterDomainResponseStatus](RegisterDomainResponseStatus.md)
 - [SearchOrdersSortField](SearchOrdersSortField.md)
 - [ShiftFilterStatus](ShiftFilterStatus.md)
 - [ShiftSortField](ShiftSortField.md)
 - [ShiftStatus](ShiftStatus.md)
 - [ShiftWorkdayMatcher](ShiftWorkdayMatcher.md)
 - [SortOrder](SortOrder.md)
 - [TaxCalculationPhase](TaxCalculationPhase.md)
 - [TaxInclusionType](TaxInclusionType.md)
 - [TenderCardDetailsEntryMethod](TenderCardDetailsEntryMethod.md)
 - [TenderCardDetailsStatus](TenderCardDetailsStatus.md)
 - [TenderType](TenderType.md)
 - [TransactionProduct](TransactionProduct.md)
 - [V1AdjustInventoryRequestAdjustmentType](V1AdjustInventoryRequestAdjustmentType.md)
 - [V1BankAccountType](V1BankAccountType.md)
 - [V1CashDrawerEventEventType](V1CashDrawerEventEventType.md)
 - [V1CashDrawerShiftEventType](V1CashDrawerShiftEventType.md)
 - [V1CreateRefundRequestType](V1CreateRefundRequestType.md)
 - [V1DiscountColor](V1DiscountColor.md)
 - [V1DiscountDiscountType](V1DiscountDiscountType.md)
 - [V1EmployeeRolePermissions](V1EmployeeRolePermissions.md)
 - [V1EmployeeStatus](V1EmployeeStatus.md)
 - [V1FeeAdjustmentType](V1FeeAdjustmentType.md)
 - [V1FeeCalculationPhase](V1FeeCalculationPhase.md)
 - [V1FeeInclusionType](V1FeeInclusionType.md)
 - [V1FeeType](V1FeeType.md)
 - [V1ItemColor](V1ItemColor.md)
 - [V1ItemType](V1ItemType.md)
 - [V1ItemVisibility](V1ItemVisibility.md)
 - [V1ListEmployeesRequestStatus](V1ListEmployeesRequestStatus.md)
 - [V1ListSettlementsRequestStatus](V1ListSettlementsRequestStatus.md)
 - [V1MerchantAccountType](V1MerchantAccountType.md)
 - [V1MerchantBusinessType](V1MerchantBusinessType.md)
 - [V1ModifierListSelectionType](V1ModifierListSelectionType.md)
 - [V1OrderHistoryEntryAction](V1OrderHistoryEntryAction.md)
 - [V1OrderState](V1OrderState.md)
 - [V1PageCellObjectType](V1PageCellObjectType.md)
 - [V1PageCellPlaceholderType](V1PageCellPlaceholderType.md)
 - [V1PaymentItemizationItemizationType](V1PaymentItemizationItemizationType.md)
 - [V1PaymentSurchargeType](V1PaymentSurchargeType.md)
 - [V1PaymentTaxInclusionType](V1PaymentTaxInclusionType.md)
 - [V1RefundType](V1RefundType.md)
 - [V1SettlementEntryType](V1SettlementEntryType.md)
 - [V1SettlementStatus](V1SettlementStatus.md)
 - [V1TenderCardBrand](V1TenderCardBrand.md)
 - [V1TenderEntryMethod](V1TenderEntryMethod.md)
 - [V1TenderType](V1TenderType.md)
 - [V1TimecardEventEventType](V1TimecardEventEventType.md)
 - [V1UpdateModifierListRequestSelectionType](V1UpdateModifierListRequestSelectionType.md)
 - [V1UpdateOrderRequestAction](V1UpdateOrderRequestAction.md)
 - [V1VariationInventoryAlertType](V1VariationInventoryAlertType.md)
 - [V1VariationPricingType](V1VariationPricingType.md)
 - [WebhookEvents](WebhookEvents.md)
 - [Weekday](Weekday.md)


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
 - **ITEMS_READ**: __HTTP Method__: `GET`  Grants read access to product catalog information. For example, to get an  item or a list of items.
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
```
