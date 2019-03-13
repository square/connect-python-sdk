# EmployeesApi
> squareconnect.apis.employees_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**list_employees**](EmployeesApi.md#list_employees) | **GET** /v2/employees
[**retrieve_employee**](EmployeesApi.md#retrieve_employee) | **GET** /v2/employees/{id}


# **list_employees**
> ListEmployeesResponse list_employees(location_id=location_id, status=status, limit=limit, cursor=cursor)

### Description

Gets a list of `Employee` objects for a business.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| [optional] 
 **status** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**ListEmployeesResponse**](ListEmployeesResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_employee**
> RetrieveEmployeeResponse retrieve_employee(id)

### Description

Gets an `Employee` by Square-assigned employee `ID` (UUID)

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **id** | **str**| 

### Return type

[**RetrieveEmployeeResponse**](RetrieveEmployeeResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

