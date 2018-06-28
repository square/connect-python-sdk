# SearchCustomersResponse
> squareconnect.models.search_customers_response

### Description

Defines the fields that are included in the response body of a request to the [SearchCustomers](#endpoint-searchcustomers) endpoint.  One of `errors` or `customers` is present in a given response (never both).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 
**customers** | [**list[Customer]**](Customer.md) | An array of &#x60;Customer&#x60; objects that match a query. | [optional] 
**cursor** | **str** | A pagination cursor that can be used during subsequent calls to SearchCustomers to retrieve the next set of results associated with the original query. Pagination cursors are only present when a request succeeds and additional results are available.  See [Paginating results](#paginatingresults) for more information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


