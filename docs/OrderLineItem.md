# OrderLineItem
> squareconnect.models.order_line_item

### Description

Represents a line item in an order. Each line item describes a different product to purchase, with its own quantity and price details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the line item. | [optional] 
**quantity** | **str** | The quantity purchased, as a string representation of a number.  This string must have a positive integer value. | 
**note** | **str** | The note of the line item. | [optional] 
**catalog_object_id** | **str** | The [CatalogItemVariation](#type-catalogitemvariation) id applied to this line item. | [optional] 
**variation_name** | **str** | The name of the variation applied to this line item. | [optional] 
**modifiers** | [**list[OrderLineItemModifier]**](OrderLineItemModifier.md) | The [CatalogModifier](#type-catalogmodifier)s applied to this line item. | [optional] 
**taxes** | [**list[OrderLineItemTax]**](OrderLineItemTax.md) | The taxes applied to this line item. | [optional] 
**discounts** | [**list[OrderLineItemDiscount]**](OrderLineItemDiscount.md) | The discounts applied to this line item. | [optional] 
**base_price_money** | [**Money**](Money.md) | The base price for a single unit of the line item. | [optional] 
**gross_sales_money** | [**Money**](Money.md) | The gross sales amount of money calculated as (item base price + modifiers price) * quantity. | [optional] 
**total_tax_money** | [**Money**](Money.md) | The total tax amount of money to collect for the line item. | [optional] 
**total_discount_money** | [**Money**](Money.md) | The total discount amount of money to collect for the line item. | [optional] 
**total_money** | [**Money**](Money.md) | The total amount of money to collect for this line item. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


