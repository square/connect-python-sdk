# ListBreakTypesResponse
> squareconnect.models.list_break_types_response

### Description

The response to a request for a set of `BreakTypes`. Contains the requested `BreakType` objects. May contain a set of `Error` objects if the request resulted in errors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_types** | [**list[BreakType]**](BreakType.md) |  A page of &#x60;BreakType&#x60; results. | [optional] 
**cursor** | **str** | Value supplied in the subsequent request to fetch the next next page of Break Type results. | [optional] 
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


