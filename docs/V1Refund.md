# V1Refund
> squareconnect.models.v1_refund

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of refund  | [optional] 
**reason** | **str** | The merchant-specified reason for the refund. | [optional] 
**refunded_money** | [**V1Money**](V1Money.md) | The amount of money refunded. This amount is always negative. | [optional] 
**created_at** | **str** | The time when the merchant initiated the refund for Square to process, in ISO 8601 format. | [optional] 
**processed_at** | **str** | The time when Square processed the refund on behalf of the merchant, in ISO 8601 format. | [optional] 
**payment_id** | **str** | A Square-issued ID associated with the refund. For single-tender refunds, payment_id is the ID of the original payment ID. For split-tender refunds, payment_id is the ID of the original tender. For exchange-based refunds (is_exchange &#x3D;&#x3D; true), payment_id is the ID of the original payment ID even if the payment includes other tenders. | [optional] 
**merchant_id** | **str** |  | [optional] 
**is_exchange** | **bool** | Indicates whether or not the refund is associated with an exchange. If is_exchange is true, the refund reflects the value of goods returned in the exchange not the total money refunded. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


