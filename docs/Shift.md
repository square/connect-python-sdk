# Shift
> squareconnect.models.shift

### Description

A record of the hourly rate, start, and end times for a single work shift  for an employee. May include a record of the start and end times for breaks  taken during the shift.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID for this object | [optional] 
**employee_id** | **str** | The ID of the employee this shift belongs to. | 
**location_id** | **str** | The ID of the location this shift occurred at. Should be based on where the employee clocked in. | [optional] 
**timezone** | **str** | Read-only convenience value that is calculated from the location based on &#x60;location_id&#x60;. Format: the IANA Timezone Database identifier for the location timezone. | [optional] 
**start_at** | **str** | RFC 3339; shifted to location timezone + offset. Precision up to the minute is respected; seconds are truncated. | 
**end_at** | **str** | RFC 3339; shifted to timezone + offset. Precision up to the minute is respected; seconds are truncated. The &#x60;end_at&#x60; minute is not counted when the shift length is calculated. For example, a shift from &#x60;00:00&#x60; to &#x60;08:01&#x60; is considered an 8 hour shift (midnight to 8am). | [optional] 
**wage** | [**ShiftWage**](ShiftWage.md) | Job and pay related information. | [optional] 
**breaks** | [**list[ModelBreak]**](ModelBreak.md) | A list of any paid or unpaid breaks that were taken during this shift. | [optional] 
**status** | **str** | Describes working state of the current &#x60;Shift&#x60;. See [ShiftStatus](#type-shiftstatus) for possible values | [optional] 
**version** | **int** | Used for resolving concurrency issues; request will fail if version provided does not match server version at time of request. If not provided, Square executes a blind write; potentially overwriting data from another write. | [optional] 
**created_at** | **str** | A read-only timestamp in RFC 3339 format; presented in UTC. | [optional] 
**updated_at** | **str** | A read-only timestamp in RFC 3339 format; presented in UTC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


