# OrderLineItem
> squareconnect.models.order_line_item

### Description

Represents a line item in an order. Each line item describes a different product to purchase, with its own quantity and price details.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**name** | **str** | [optional] 
**quantity** | **str** | [optional] 
**taxes** | [**list[OrderLineItemTax]**](OrderLineItemTax.md) | [optional] 
**discounts** | [**list[OrderLineItemDiscount]**](OrderLineItemDiscount.md) | [optional] 
**base_price_money** | [**Money**](Money.md) | [optional] 
**total_tax_money** | [**Money**](Money.md) | [optional] 
**total_discount_money** | [**Money**](Money.md) | [optional] 
**total_money** | [**Money**](Money.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


