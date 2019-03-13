# V1ListEmployeeRolesRequest
> squareconnect.models.v1_list_employee_roles_request

### Description



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** | The order in which employees are listed in the response, based on their created_at field.Default value: ASC See [SortOrder](#type-sortorder) for possible values | [optional] 
**limit** | **int** | The maximum integer number of employee entities to return in a single response. Default 100, maximum 200. | [optional] 
**batch_token** | **str** | A pagination cursor to retrieve the next set of results for your original query to the endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


