# OrderLineItemDiscount
> squareconnect.models.order_line_item_discount

### Description

Represents a discount that applies to one or more line items in an order.  Fixed-amount, order-level discounts are distributed across all non-zero line item totals. The amount distributed to each line item is relative to that item’s contribution to the order subtotal.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**name** | **str** | [optional] 
**type** | **str** | [optional] 
**percentage** | **str** | [optional] 
**amount_money** | [**Money**](Money.md) | [optional] 
**applied_money** | [**Money**](Money.md) | [optional] 
**scope** | **str** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


