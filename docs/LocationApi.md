# LocationApi
> squareconnect.apis.location_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**list_locations**](LocationApi.md#list_locations) | **GET** /v2/locations
[**v1_list_locations**](LocationApi.md#v1_list_locations) | **GET** /v1/me/locations
[**v1_retrieve_business**](LocationApi.md#v1_retrieve_business) | **GET** /v1/me


# **list_locations**
> ListLocationsResponse list_locations()

### Description

Provides the details for all of a business's locations.  Most other Connect API endpoints have a required `location_id` path parameter. The `id` field of the [`Location`](#type-location) objects returned by this endpoint correspond to that `location_id` parameter.

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListLocationsResponse**](ListLocationsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_locations**
> list[V1Merchant] v1_list_locations()

### Description

Provides details for a business's locations, including their IDs.

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V1Merchant]**](V1Merchant.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_retrieve_business**
> V1Merchant v1_retrieve_business()

### Description

Get a business's information.

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1Merchant**](V1Merchant.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

