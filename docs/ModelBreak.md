# ModelBreak
> squareconnect.models.model_break

### Description

A record of an employee's break during a shift.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID for this object | [optional] 
**start_at** | **str** | RFC 3339; follows same timezone info as &#x60;Shift&#x60;. Precision up to the minute is respected; seconds are truncated. | 
**end_at** | **str** | RFC 3339; follows same timezone info as &#x60;Shift&#x60;. Precision up to the minute is respected; seconds are truncated. The &#x60;end_at&#x60; minute is not counted when the break length is calculated. For example, a break from &#x60;00:00&#x60; to &#x60;00:11&#x60;  is considered a 10 minute break (midnight to 10 minutes after midnight). | [optional] 
**break_type_id** | **str** | The &#x60;BreakType&#x60; this &#x60;Break&#x60; was templated on. | 
**name** | **str** | A human-readable name. | 
**expected_duration** | **str** | Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of the break. | 
**is_paid** | **bool** | Whether this break counts towards time worked for compensation purposes. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


