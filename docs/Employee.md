# Employee
> squareconnect.models.employee

### Description

An employee created in the **Square Dashboard** account of a business.  Used by the Labor API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID for this &#x60;Employee&#x60;. | [optional] 
**first_name** | **str** | Given (first) name of the employee. | [optional] 
**last_name** | **str** | Family (last) name of the employee | [optional] 
**location_ids** | **list[str]** | A list of location IDs where this employee has access. | [optional] 
**status** | **str** | Specifies the status of the employee being fetched. | [optional] 
**created_at** | **str** | A read-only timestamp in RFC 3339 format. | [optional] 
**updated_at** | **str** | A read-only timestamp in RFC 3339 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


