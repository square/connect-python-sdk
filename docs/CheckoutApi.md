# CheckoutApi
> squareconnect.apis.checkout_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**create_checkout**](CheckoutApi.md#create_checkout) | **POST** /v2/locations/{location_id}/checkouts


# **create_checkout**
> CreateCheckoutResponse create_checkout(authorization, location_id, body)

### Description

Creates a [Checkout](#type-checkout) response that links a `checkoutId` and `checkout_page_url` that customers can be directed to in order to provide their payment information using a payment processing workflow hosted on connect.squareup.com.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **location_id** | **str**| 
 **body** | [**CreateCheckoutRequest**](CreateCheckoutRequest.md)| 

### Return type

[**CreateCheckoutResponse**](CreateCheckoutResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

