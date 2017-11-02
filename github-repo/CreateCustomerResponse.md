# CreateCustomerResponse
> squareconnect.models.create_customer_response

### Description

Defines the fields that are included in the response body of a request to the [CreateCustomer](#endpoint-createcustomer) endpoint.  One of `errors` or `customer` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**customer** | [**Customer**](Customer.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


