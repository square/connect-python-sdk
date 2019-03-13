# V1ListEmployeesRequest
> squareconnect.models.v1_list_employees_request

### Description



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** | The order in which employees are listed in the response, based on their created_at field.      Default value: ASC See [SortOrder](#type-sortorder) for possible values | [optional] 
**begin_updated_at** | **str** | If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format | [optional] 
**end_updated_at** | **str** | If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format. | [optional] 
**begin_created_at** | **str** | If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format. | [optional] 
**end_created_at** | **str** | If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format. | [optional] 
**status** | **str** | If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE). See [V1ListEmployeesRequestStatus](#type-v1listemployeesrequeststatus) for possible values | [optional] 
**external_id** | **str** | If provided, the endpoint returns only employee entities with the specified external_id. | [optional] 
**limit** | **int** | The maximum integer number of employee entities to return in a single response. Default 100, maximum 200. | [optional] 
**batch_token** | **str** | A pagination cursor to retrieve the next set of results for your original query to the endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


