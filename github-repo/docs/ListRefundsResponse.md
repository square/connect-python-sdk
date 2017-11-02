# ListRefundsResponse
> squareconnect.models.list_refunds_response

### Description

Defines the fields that are included in the response body of a request to the [ListRefunds](#endpoint-listrefunds) endpoint.  One of `errors` or `refunds` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**refunds** | [**list[Refund]**](Refund.md) | [optional] 
**cursor** | **str** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


