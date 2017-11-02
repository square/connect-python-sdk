# V1Payment
> squareconnect.models.v1_payment

### Description

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | [optional] 
**merchant_id** | **str** | [optional] 
**created_at** | **str** | [optional] 
**creator_id** | **str** | [optional] 
**device** | [**Device**](Device.md) | [optional] 
**payment_url** | **str** | [optional] 
**receipt_url** | **str** | [optional] 
**inclusive_tax_money** | [**V1Money**](V1Money.md) | [optional] 
**additive_tax_money** | [**V1Money**](V1Money.md) | [optional] 
**tax_money** | [**V1Money**](V1Money.md) | [optional] 
**tip_money** | [**V1Money**](V1Money.md) | [optional] 
**discount_money** | [**V1Money**](V1Money.md) | [optional] 
**total_collected_money** | [**V1Money**](V1Money.md) | [optional] 
**processing_fee_money** | [**V1Money**](V1Money.md) | [optional] 
**net_total_money** | [**V1Money**](V1Money.md) | [optional] 
**refunded_money** | [**V1Money**](V1Money.md) | [optional] 
**swedish_rounding_money** | [**V1Money**](V1Money.md) | [optional] 
**gross_sales_money** | [**V1Money**](V1Money.md) | [optional] 
**net_sales_money** | [**V1Money**](V1Money.md) | [optional] 
**inclusive_tax** | [**list[V1PaymentTax]**](V1PaymentTax.md) | [optional] 
**additive_tax** | [**list[V1PaymentTax]**](V1PaymentTax.md) | [optional] 
**tender** | [**list[V1Tender]**](V1Tender.md) | [optional] 
**refunds** | [**list[V1Refund]**](V1Refund.md) | [optional] 
**itemizations** | [**list[V1PaymentItemization]**](V1PaymentItemization.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


