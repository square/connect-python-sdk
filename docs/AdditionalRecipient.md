# AdditionalRecipient
> squareconnect.models.additional_recipient

### Description

Represents an additional recipient (other than the merchant) receiving a portion of this tender.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | The location ID for a recipient (other than the merchant) receiving a portion of this tender. | 
**description** | **str** | The description of the additional recipient. | 
**amount_money** | [**Money**](Money.md) | The amount of money distributed to the recipient. | 
**receivable_id** | **str** | The unique ID for this [AdditionalRecipientReceivable](#type-additionalrecipientreceivable), assigned by the server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


