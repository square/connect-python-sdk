# LocationApi
> squareconnect.apis.location_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**list_locations**](LocationApi.md#list_locations) | **GET** /v2/locations


# **list_locations**
> ListLocationsResponse list_locations(authorization)

### Description

Provides the details for all of a business's locations.  Most other Connect API endpoints have a required `location_id` path parameter. The `id` field of the [`Location`](#type-location) objects returned by this endpoint correspond to that `location_id` parameter.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 

### Return type

[**ListLocationsResponse**](ListLocationsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

