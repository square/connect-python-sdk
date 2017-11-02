# ListTransactionsResponse
> squareconnect.models.list_transactions_response

### Description

Defines the fields that are included in the response body of a request to the [ListTransactions](#endpoint-listtransactions) endpoint.  One of `errors` or `transactions` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**transactions** | [**list[Transaction]**](Transaction.md) | [optional] 
**cursor** | **str** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


