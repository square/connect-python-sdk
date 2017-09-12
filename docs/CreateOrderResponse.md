# CreateOrderResponse
> squareconnect.models.create_order_response

### Description

Defines the fields that are included in the response body of a request to the [CreateOrder](#endpoint-createorder) endpoint.  One of `errors` or `order` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**order** | [**Order**](Order.md) | [optional] 
**errors** | [**list[Error]**](Error.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


