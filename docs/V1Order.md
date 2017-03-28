# V1Order
> squareconnect.models.v1_order

### Description

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | [optional] 
**id** | **str** | [optional] 
**buyer_email** | **str** | [optional] 
**recipient_name** | **str** | [optional] 
**recipient_phone_number** | **str** | [optional] 
**state** | **str** | [optional] 
**shipping_address** | [**Address**](Address.md) | [optional] 
**subtotal_money** | [**V1Money**](V1Money.md) | [optional] 
**total_shipping_money** | [**V1Money**](V1Money.md) | [optional] 
**total_tax_money** | [**V1Money**](V1Money.md) | [optional] 
**total_price_money** | [**V1Money**](V1Money.md) | [optional] 
**total_discount_money** | [**V1Money**](V1Money.md) | [optional] 
**created_at** | **str** | [optional] 
**updated_at** | **str** | [optional] 
**expires_at** | **str** | [optional] 
**payment_id** | **str** | [optional] 
**buyer_note** | **str** | [optional] 
**completed_note** | **str** | [optional] 
**refunded_note** | **str** | [optional] 
**canceled_note** | **str** | [optional] 
**tender** | [**V1Tender**](V1Tender.md) | [optional] 
**order_history** | [**list[V1OrderHistoryEntry]**](V1OrderHistoryEntry.md) | [optional] 
**promo_code** | **str** | [optional] 
**btc_receive_address** | **str** | [optional] 
**btc_price_satoshi** | **float** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


