# Refund
> squareconnect.models.refund

### Description

Represents a refund processed for a Square transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The refund&#39;s unique ID. | 
**location_id** | **str** | The ID of the refund&#39;s associated location. | 
**transaction_id** | **str** | The ID of the transaction that the refunded tender is part of. | 
**tender_id** | **str** | The ID of the refunded tender. | 
**created_at** | **str** | The time when the refund was created, in RFC 3339 format. | [optional] 
**reason** | **str** | The reason for the refund being issued. | 
**amount_money** | [**Money**](Money.md) | The amount of money refunded to the buyer. | 
**status** | **str** | The current status of the refund (&#x60;PENDING&#x60;, &#x60;APPROVED&#x60;, &#x60;REJECTED&#x60;, or &#x60;FAILED&#x60;). | 
**processing_fee_money** | [**Money**](Money.md) | The amount of Square processing fee money refunded to the *merchant*. | [optional] 
**additional_recipients** | [**list[AdditionalRecipient]**](AdditionalRecipient.md) | Additional recipients (other than the merchant) receiving a portion of this refund. For example, fees assessed on a refund of a purchase by a third party integration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


