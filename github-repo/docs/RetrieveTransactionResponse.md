# RetrieveTransactionResponse
> squareconnect.models.retrieve_transaction_response

### Description

Defines the fields that are included in the response body of a request to the [RetrieveTransaction](#endpont-retrievetransaction) endpoint.  One of `errors` or `transaction` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**transaction** | [**Transaction**](Transaction.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


