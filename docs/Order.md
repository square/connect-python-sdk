# Order
> squareconnect.models.order

### Description

Contains all information related to a single order to process with Square, including line items that specify the products to purchase

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | [optional] 
**location_id** | **str** | [optional] 
**reference_id** | **str** | [optional] 
**line_items** | [**list[OrderLineItem]**](OrderLineItem.md) | [optional] 
**total_money** | [**Money**](Money.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


