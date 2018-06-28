# ListCustomersResponse
> squareconnect.models.list_customers_response

### Description

Defines the fields that are included in the response body of a request to the [ListCustomers](#endpoint-listcustomers) endpoint.  One of `errors` or `customers` is present in a given response (never both).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 
**customers** | [**list[Customer]**](Customer.md) | An array of &#x60;Customer&#x60; objects that match your query. | [optional] 
**cursor** | **str** | A pagination cursor to retrieve the next set of results for your original query to the endpoint. This value is present only if the request succeeded and additional results are available.  See [Paginating results](#paginatingresults) for more information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


