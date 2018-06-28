# CustomerFilter
> squareconnect.models.customer_filter

### Description

Represents a set of [`CustomerQuery`](#type-customerquery) filters used to limit the set of Customers returned by [`SearchCustomers`](#endpoint-seachcustomers).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_source** | [**CustomerCreationSourceFilter**](CustomerCreationSourceFilter.md) | A filter to select customers based on their creation source. | [optional] 
**created_at** | [**TimeRange**](TimeRange.md) | A filter to select customers based on when they were created. | [optional] 
**updated_at** | [**TimeRange**](TimeRange.md) | A filter to select customers based on when they were updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


