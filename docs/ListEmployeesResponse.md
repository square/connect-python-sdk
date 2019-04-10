# ListEmployeesResponse
> squareconnect.models.list_employees_response

### Description

Defines the fields that are included in the response body of a request to the ListEmployees endpoint.  One of `errors` or `employees` is present in a given response (never both).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employees** | [**list[Employee]**](Employee.md) | List of employees returned from the request. | [optional] 
**cursor** | **str** | The token to be used to retrieve the next page of results. | [optional] 
**errors** | [**list[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


