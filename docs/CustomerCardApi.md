# CustomerCardApi
> squareconnect.apis.customer_card_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**create_customer_card**](CustomerCardApi.md#create_customer_card) | **POST** /v2/customers/{customer_id}/cards
[**delete_customer_card**](CustomerCardApi.md#delete_customer_card) | **DELETE** /v2/customers/{customer_id}/cards/{card_id}


# **create_customer_card**
> CreateCustomerCardResponse create_customer_card(authorization, customer_id, body)

### Description

Adds a card on file to an existing customer.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **customer_id** | **str**| 
 **body** | [**CreateCustomerCardRequest**](CreateCustomerCardRequest.md)| 

### Return type

[**CreateCustomerCardResponse**](CreateCustomerCardResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_card**
> DeleteCustomerCardResponse delete_customer_card(authorization, customer_id, card_id)

### Description

Removes a card on file from a customer.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **customer_id** | **str**| 
 **card_id** | **str**| 

### Return type

[**DeleteCustomerCardResponse**](DeleteCustomerCardResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

