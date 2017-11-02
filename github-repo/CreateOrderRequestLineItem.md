# CreateOrderRequestLineItem
> squareconnect.models.create_order_request_line_item

### Description

Represents a line item to include in an order. Each line item describes a different product to purchase, with its own quantity and price details.  Line items can either reference objects from the merchant's catalog, or can alternatively specify a name and price instead.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**name** | **str** | [optional] 
**quantity** | **str** | 
**base_price_money** | [**Money**](Money.md) | [optional] 
**variation_name** | **str** | [optional] 
**note** | **str** | [optional] 
**catalog_object_id** | **str** | [optional] 
**modifiers** | [**list[CreateOrderRequestModifier]**](CreateOrderRequestModifier.md) | [optional] 
**taxes** | [**list[CreateOrderRequestTax]**](CreateOrderRequestTax.md) | [optional] 
**discounts** | [**list[CreateOrderRequestDiscount]**](CreateOrderRequestDiscount.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


