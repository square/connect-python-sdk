# OrderFulfillment
> squareconnect.models.order_fulfillment

### Description

Contains details on how to fulfill this order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the fulfillment. See [OrderFulfillmentType](#type-orderfulfillmenttype) for possible values | [optional] 
**state** | **str** | The state of the fulfillment. See [OrderFulfillmentState](#type-orderfulfillmentstate) for possible values | [optional] 
**pickup_details** | [**OrderFulfillmentPickupDetails**](OrderFulfillmentPickupDetails.md) | Contains pickup-specific details. Required when fulfillment type is &#x60;PICKUP&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


