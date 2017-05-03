# CustomersApi
> squareconnect.apis.customers_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**create_customer**](CustomersApi.md#create_customer) | **POST** /v2/customers
[**create_customer_card**](CustomersApi.md#create_customer_card) | **POST** /v2/customers/{customer_id}/cards
[**delete_customer**](CustomersApi.md#delete_customer) | **DELETE** /v2/customers/{customer_id}
[**delete_customer_card**](CustomersApi.md#delete_customer_card) | **DELETE** /v2/customers/{customer_id}/cards/{card_id}
[**list_customers**](CustomersApi.md#list_customers) | **GET** /v2/customers
[**retrieve_customer**](CustomersApi.md#retrieve_customer) | **GET** /v2/customers/{customer_id}
[**update_customer**](CustomersApi.md#update_customer) | **PUT** /v2/customers/{customer_id}


# **create_customer**
> CreateCustomerResponse create_customer(authorization, body)

### Description

Creates a new customer for a business, which can have associated cards on file.  You must provide __at least one__ of the following values in your request to this endpoint:  - `given_name` - `family_name` - `company_name` - `email_address` - `phone_number`  This endpoint does not accept an idempotency key. If you accidentally create a duplicate customer, you can delete it with the [DeleteCustomer](#endpoint-deletecustomer) endpoint.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **body** | [**CreateCustomerRequest**](CreateCustomerRequest.md)| 

### Return type

[**CreateCustomerResponse**](CreateCustomerResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_card**
> CreateCustomerCardResponse create_customer_card(authorization, customer_id, body)

### Description

Adds a card on file to an existing customer.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **customer_id** | **str**| 
 **body** | [**CreateCustomerCardRequest**](CreateCustomerCardRequest.md)| 

### Return type

[**CreateCustomerCardResponse**](CreateCustomerCardResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer**
> DeleteCustomerResponse delete_customer(authorization, customer_id)

### Description

Deletes a customer from a business, along with any linked cards on file.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **customer_id** | **str**| 

### Return type

[**DeleteCustomerResponse**](DeleteCustomerResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_card**
> DeleteCustomerCardResponse delete_customer_card(authorization, customer_id, card_id)

### Description

Removes a card on file from a customer.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **customer_id** | **str**| 
 **card_id** | **str**| 

### Return type

[**DeleteCustomerCardResponse**](DeleteCustomerCardResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> ListCustomersResponse list_customers(authorization, cursor=cursor)

### Description

Lists a business's customers.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **cursor** | **str**| [optional] 

### Return type

[**ListCustomersResponse**](ListCustomersResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_customer**
> RetrieveCustomerResponse retrieve_customer(authorization, customer_id)

### Description

Returns details for a single customer.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **customer_id** | **str**| 

### Return type

[**RetrieveCustomerResponse**](RetrieveCustomerResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> UpdateCustomerResponse update_customer(authorization, customer_id, body)

### Description

Updates the details of an existing customer.  You cannot edit a customer's cards on file with this endpoint. To make changes to a card on file, you must delete the existing card on file with the [DeleteCustomerCard](#endpoint-deletecustomercard) endpoint, then create a new one with the [CreateCustomerCard](#endpoint-createcustomercard) endpoint.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **customer_id** | **str**| 
 **body** | [**UpdateCustomerRequest**](UpdateCustomerRequest.md)| 

### Return type

[**UpdateCustomerResponse**](UpdateCustomerResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

