# ListAdditionalRecipientReceivableRefundsResponse
> squareconnect.models.list_additional_recipient_receivable_refunds_response

### Description

Defines the fields that are included in the response body of a request to the [ListAdditionalRecipientReceivableRefunds](#endpoint-listadditionalrecipientreceivablerefunds) endpoint.  One of `errors` or `additional_recipient_receivable_refunds` is present in a given response (never both).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**receivable_refunds** | [**list[AdditionalRecipientReceivableRefund]**](AdditionalRecipientReceivableRefund.md) | [optional] 
**cursor** | **str** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


