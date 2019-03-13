# ShiftFilter
> squareconnect.models.shift_filter

### Description

Defines a filter used in a search for `Shift` records. `AND` logic is used by Square's servers to apply each filter property specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **list[str]** | Fetch shifts for the specified location. | [optional] 
**employee_id** | **list[str]** | Fetch shifts for the specified employee. | [optional] 
**status** | **str** | Fetch a &#x60;Shift&#x60; instance by &#x60;Shift.status&#x60;. | [optional] 
**start** | [**TimeRange**](TimeRange.md) | Fetch &#x60;Shift&#x60;s that start in the time range - Inclusive. | [optional] 
**end** | [**TimeRange**](TimeRange.md) | Fetch the &#x60;Shift&#x60;s that end in the time range - Inclusive. | [optional] 
**workday** | [**ShiftWorkday**](ShiftWorkday.md) | Fetch the &#x60;Shift&#x60;s based on workday date range. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


