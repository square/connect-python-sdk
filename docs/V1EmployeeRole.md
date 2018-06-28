# V1EmployeeRole
> squareconnect.models.v1_employee_role

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The role&#39;s unique ID, Can only be set by Square. | [optional] 
**name** | **str** | The role&#39;s merchant-defined name. | 
**permissions** | **list[str]** | The role&#39;s permissions. | 
**is_owner** | **bool** | If true, employees with this role have all permissions, regardless of the values indicated in permissions. | [optional] 
**created_at** | **str** | The time when the employee entity was created, in ISO 8601 format. Is set by Square when the Role is created. | [optional] 
**updated_at** | **str** | The time when the employee entity was most recently updated, in ISO 8601 format. Is set by Square when the Role updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


