# ListEmployeeWagesResponse
> squareconnect.models.list_employee_wages_response

### Description

The response to a request for a set of `EmployeeWage` objects. Contains  a set of `EmployeeWage`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_wages** | [**list[EmployeeWage]**](EmployeeWage.md) | A page of Employee Wage results. | [optional] 
**cursor** | **str** | Value supplied in the subsequent request to fetch the next next page of Employee Wage results. | [optional] 
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


