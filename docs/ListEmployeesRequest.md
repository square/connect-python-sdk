# ListEmployeesRequest
> squareconnect.models.list_employees_request

### Description

Retrieve a paged-list of employees for a Square account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** | Filter employees returned to only those that are associated with the specified location. | [optional] 
**status** | **str** | Specifies the EmployeeStatus to filter the employee by. See [EmployeeStatus](#type-employeestatus) for possible values | [optional] 
**limit** | **int** | The number of employees to be returned on each page. | [optional] 
**cursor** | **str** | The token required to retrieve the specified page of results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


