# Order
> squareconnect.models.order

### Description

Contains all information related to a single order to process with Square, including line items that specify the products to purchase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The order&#39;s unique ID.  This value is only present for Order objects created by the Orders API through the [CreateOrder](#endpoint-createorder) endpoint. | [optional] 
**location_id** | **str** | The ID of the merchant location this order is associated with. | 
**reference_id** | **str** | A client specified identifier to associate an entity in another system with this order. | [optional] 
**line_items** | [**list[OrderLineItem]**](OrderLineItem.md) | The line items included in the order. Every order has at least one line item. | 
**total_money** | [**Money**](Money.md) | The total amount of money to collect for the order. | [optional] 
**total_tax_money** | [**Money**](Money.md) | The total tax amount of money to collect for the order. | [optional] 
**total_discount_money** | [**Money**](Money.md) | The total discount amount of money to collect for the order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


