# CreateRefundResponse
> squareconnect.models.create_refund_response

### Description

Defines the fields that are included in the response body of a request to the [CreateRefund](#endpoint-createrefund) endpoint.  One of `errors` or `refund` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**refund** | [**Refund**](Refund.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


