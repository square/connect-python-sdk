# V1CashDrawerEvent
> squareconnect.models.v1_cash_drawer_event

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The event&#39;s unique ID. | [optional] 
**employee_id** | **str** | The ID of the employee that created the event. | [optional] 
**event_type** | **str** | The type of event that occurred. | [optional] 
**event_money** | [**V1Money**](V1Money.md) | The amount of money that was added to or removed from the cash drawer because of the event. This value can be positive (for added money) or negative (for removed money). | [optional] 
**created_at** | **str** | The time when the event occurred, in ISO 8601 format. | [optional] 
**description** | **str** | An optional description of the event, entered by the employee that created it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


