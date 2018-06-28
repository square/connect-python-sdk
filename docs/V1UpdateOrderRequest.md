# V1UpdateOrderRequest
> squareconnect.models.v1_update_order_request

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to perform on the order (COMPLETE, CANCEL, or REFUND). | 
**shipped_tracking_number** | **str** | The tracking number of the shipment associated with the order. Only valid if action is COMPLETE. | [optional] 
**completed_note** | **str** | A merchant-specified note about the completion of the order. Only valid if action is COMPLETE. | [optional] 
**refunded_note** | **str** | A merchant-specified note about the refunding of the order. Only valid if action is REFUND. | [optional] 
**canceled_note** | **str** | A merchant-specified note about the canceling of the order. Only valid if action is CANCEL. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


