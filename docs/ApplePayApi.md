# ApplePayApi
> squareconnect.apis.apple_pay_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**register_domain**](ApplePayApi.md#register_domain) | **POST** /v2/apple-pay/domains


# **register_domain**
> RegisterDomainResponse register_domain(body)

### Description

Activates a domain for use with Web Apple Pay and Square. A validation will be performed on this domain by Apple to ensure is it properly set up as an Apple Pay enabled domain.  This endpoint provides an easy way for platform developers to bulk activate Web Apple Pay with Square for merchants using their platform.  To learn more about Apple Pay on Web see the Apple Pay section in the [Embedding the Square Payment Form](/payments/sqpaymentform/overview) guide.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterDomainRequest**](RegisterDomainRequest.md)| 

### Return type

[**RegisterDomainResponse**](RegisterDomainResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

