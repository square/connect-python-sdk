# ListCustomersResponse
> squareconnect.models.list_customers_response

### Description

Defines the fields that are included in the response body of a request to the [ListCustomers](#endpoint-listcustomers) endpoint.  One of `errors` or `customers` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**customers** | [**list[Customer]**](Customer.md) | [optional] 
**cursor** | **str** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


