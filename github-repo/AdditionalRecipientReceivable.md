# AdditionalRecipientReceivable
> squareconnect.models.additional_recipient_receivable

### Description

Represents a monetary distribution of part of a [Transaction](#type-transaction)'s amount for Transactions which included additional recipients. The location of this receivable is that same as the one specified in the [AdditionalRecipient](#type-additionalrecipient).

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | 
**transaction_id** | **str** | 
**transaction_location_id** | **str** | 
**amount_money** | [**Money**](Money.md) | 
**created_at** | **str** | [optional] 
**refunds** | [**list[AdditionalRecipientReceivableRefund]**](AdditionalRecipientReceivableRefund.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


