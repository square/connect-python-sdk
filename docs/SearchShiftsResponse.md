# SearchShiftsResponse
> squareconnect.models.search_shifts_response

### Description

The response to a request for `Shift` objects. Contains the requested `Shift` objects. May contain a set of `Error` objects if the request resulted in errors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shifts** | [**list[Shift]**](Shift.md) | Shifts | [optional] 
**cursor** | **str** | Opaque cursor for fetching the next page. | [optional] 
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


