# AdditionalRecipientReceivableRefund
> squareconnect.models.additional_recipient_receivable_refund

### Description

A refund of an [AdditionalRecipientReceivable](#type-additionalrecipientreceivable). This includes the ID of the additional recipient receivable associated to this object, as well as a reference to the [Refund](#type-refund) that created this receivable refund.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The receivable refund&#39;s unique ID, issued by Square payments servers. | 
**receivable_id** | **str** | The ID of the receivable that the refund was applied to. | 
**refund_id** | **str** | The ID of the refund that is associated to this receivable refund. | 
**transaction_location_id** | **str** | The ID of the location that created the receivable. This is the location ID on the associated transaction. | 
**amount_money** | [**Money**](Money.md) | The amount of the refund. This will always be non-negative. | 
**created_at** | **str** | The time when the refund was created, in RFC 3339 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


