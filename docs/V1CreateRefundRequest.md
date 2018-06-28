# V1CreateRefundRequest
> squareconnect.models.v1_create_refund_request

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The ID of the payment to refund. If you&#39;re creating a PARTIAL refund for a split tender payment, instead provide the id of the particular tender you want to refund. See Split Tender Payments for details. | 
**type** | **str** | TThe type of refund (FULL or PARTIAL). | 
**reason** | **str** | The reason for the refund. | 
**refunded_money** | [**V1Money**](V1Money.md) | The amount of money to refund. Required only for PARTIAL refunds. | [optional] 
**request_idempotence_key** | **str** | An optional key to ensure idempotence if you issue the same PARTIAL refund request more than once. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


