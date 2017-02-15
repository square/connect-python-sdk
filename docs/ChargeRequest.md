# ChargeRequest
> squareconnect.models.charge_request

### Description

Defines the parameters that can be included in the body of a request to the [Charge](#endpoint-charge) endpoint.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**idempotency_key** | **str** | 
**amount_money** | [**Money**](Money.md) | 
**card_nonce** | **str** | [optional] 
**customer_card_id** | **str** | [optional] 
**delay_capture** | **bool** | [optional] 
**reference_id** | **str** | [optional] 
**note** | **str** | [optional] 
**customer_id** | **str** | [optional] 
**billing_address** | [**Address**](Address.md) | [optional] 
**shipping_address** | [**Address**](Address.md) | [optional] 
**buyer_email_address** | **str** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


