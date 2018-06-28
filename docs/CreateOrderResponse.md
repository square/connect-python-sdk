# CreateOrderResponse
> squareconnect.models.create_order_response

### Description

Defines the fields that are included in the response body of a request to the [CreateOrder](#endpoint-createorder) endpoint.  One of `errors` or `order` is present in a given response (never both).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**Order**](Order.md) | The newly created order. | [optional] 
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


