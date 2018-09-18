# V1Timecard
> squareconnect.models.v1_timecard

### Description

Represents a timecard for an employee.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The timecard&#39;s unique ID. | [optional] 
**employee_id** | **str** | The ID of the employee the timecard is associated with. | 
**deleted** | **bool** | If true, the timecard was deleted by the merchant, and it is no longer valid. | [optional] 
**clockin_time** | **str** | The clock-in time for the timecard, in ISO 8601 format. | [optional] 
**clockout_time** | **str** | The clock-out time for the timecard, in ISO 8601 format. Provide this value only if importing timecard information from another system. | [optional] 
**clockin_location_id** | **str** | The ID of the location the employee clocked in from. We strongly reccomend providing a clockin_location_id. Square uses the clockin_location_id to determine a timecard’s timezone and overtime rules. | [optional] 
**clockout_location_id** | **str** | The ID of the location the employee clocked out from. Provide this value only if importing timecard information from another system. | [optional] 
**created_at** | **str** | The time when the timecard was created, in ISO 8601 format. | [optional] 
**updated_at** | **str** | The time when the timecard was most recently updated, in ISO 8601 format. | [optional] 
**regular_seconds_worked** | **float** | The total number of regular (non-overtime) seconds worked in the timecard. | [optional] 
**overtime_seconds_worked** | **float** | The total number of overtime seconds worked in the timecard. | [optional] 
**doubletime_seconds_worked** | **float** | The total number of doubletime seconds worked in the timecard. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


