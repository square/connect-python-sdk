# V1Employee
> squareconnect.models.v1_employee

### Description

Represents one of a business's employees.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The employee&#39;s unique ID. | [optional] 
**first_name** | **str** | The employee&#39;s first name. | 
**last_name** | **str** | The employee&#39;s last name. | 
**role_ids** | **list[str]** | The ids of the employee&#39;s associated roles. Currently, you can specify only one or zero roles per employee. | [optional] 
**authorized_location_ids** | **list[str]** | The IDs of the locations the employee is allowed to clock in at. | [optional] 
**email** | **str** | The employee&#39;s email address. | [optional] 
**status** | **str** | CWhether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard.  | [optional] 
**external_id** | **str** | An ID the merchant can set to associate the employee with an entity in another system. | [optional] 
**created_at** | **str** | The time when the employee entity was created, in ISO 8601 format. | [optional] 
**updated_at** | **str** | The time when the employee entity was most recently updated, in ISO 8601 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


