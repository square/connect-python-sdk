# ListAdditionalRecipientReceivablesResponse
> squareconnect.models.list_additional_recipient_receivables_response

### Description

Defines the fields that are included in the response body of a request to the [ListAdditionalRecipientReceivables](#endpoint-listadditionalrecipientreceivables) endpoint.  One of `errors` or `additional_recipient_receivables` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**receivables** | [**list[AdditionalRecipientReceivable]**](AdditionalRecipientReceivable.md) | [optional] 
**cursor** | **str** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


