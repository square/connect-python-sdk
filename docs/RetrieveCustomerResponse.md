# RetrieveCustomerResponse
> squareconnect.models.retrieve_customer_response

### Description

Defines the fields that are included in the response body of a request to the [RetrieveCustomer](#endpoint-retrievecustomer) endpoint.  One of `errors` or `customer` is present in a given response (never both).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 
**customer** | [**Customer**](Customer.md) | The requested customer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


