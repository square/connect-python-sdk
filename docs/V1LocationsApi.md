# V1LocationsApi
> squareconnect.apis.v1_locations_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**list_locations**](V1LocationsApi.md#list_locations) | **GET** /v1/me/locations
[**retrieve_business**](V1LocationsApi.md#retrieve_business) | **GET** /v1/me


# **list_locations**
> list[V1Merchant] list_locations()

### Description

Provides details for a business's locations, including their IDs.

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1Merchant]**](V1Merchant.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_business**
> V1Merchant retrieve_business()

### Description

Get a business's information.

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1Merchant**](V1Merchant.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

