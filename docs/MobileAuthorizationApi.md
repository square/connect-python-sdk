# MobileAuthorizationApi
> squareconnect.apis.mobile_authorization_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**create_mobile_authorization_code**](MobileAuthorizationApi.md#create_mobile_authorization_code) | **POST** /mobile/authorization-code


# **create_mobile_authorization_code**
> CreateMobileAuthorizationCodeResponse create_mobile_authorization_code(body)

### Description

Generates code to authorize a mobile application to connect to a Square card reader  Authorization codes are one-time-use and expire __60 minutes__ after being issued.  __Important:__ The `Authorization` header you provide to this endpoint must have the following format:  ``` Authorization: Bearer ACCESS_TOKEN ```  Replace `ACCESS_TOKEN` with a [valid production authorization credential](https://docs.connect.squareup.com/get-started#step-4-understand-the-different-application-credentials).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMobileAuthorizationCodeRequest**](CreateMobileAuthorizationCodeRequest.md)| 

### Return type

[**CreateMobileAuthorizationCodeResponse**](CreateMobileAuthorizationCodeResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

