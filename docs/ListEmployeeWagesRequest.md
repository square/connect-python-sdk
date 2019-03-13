# ListEmployeeWagesRequest
> squareconnect.models.list_employee_wages_request

### Description

A request for a set of `EmployeeWage` objects

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Filter wages returned to only those that are associated with the specified employee. | [optional] 
**limit** | **int** | Maximum number of Employee Wages to return per page. Can range between 1 and 200. The default is the maximum at 200. | [optional] 
**cursor** | **str** | Pointer to the next page of Employee Wage results to fetch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


