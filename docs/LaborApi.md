# LaborApi
> squareconnect.apis.labor_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**create_break_type**](LaborApi.md#create_break_type) | **POST** /v2/labor/break-types
[**create_shift**](LaborApi.md#create_shift) | **POST** /v2/labor/shifts
[**delete_break_type**](LaborApi.md#delete_break_type) | **DELETE** /v2/labor/break-types/{id}
[**delete_shift**](LaborApi.md#delete_shift) | **DELETE** /v2/labor/shifts/{id}
[**get_break_type**](LaborApi.md#get_break_type) | **GET** /v2/labor/break-types/{id}
[**get_employee_wage**](LaborApi.md#get_employee_wage) | **GET** /v2/labor/employee-wages/{id}
[**get_shift**](LaborApi.md#get_shift) | **GET** /v2/labor/shifts/{id}
[**list_break_types**](LaborApi.md#list_break_types) | **GET** /v2/labor/break-types
[**list_employee_wages**](LaborApi.md#list_employee_wages) | **GET** /v2/labor/employee-wages
[**list_workweek_configs**](LaborApi.md#list_workweek_configs) | **GET** /v2/labor/workweek-configs
[**search_shifts**](LaborApi.md#search_shifts) | **POST** /v2/labor/shifts/search
[**update_break_type**](LaborApi.md#update_break_type) | **PUT** /v2/labor/break-types/{id}
[**update_shift**](LaborApi.md#update_shift) | **PUT** /v2/labor/shifts/{id}
[**update_workweek_config**](LaborApi.md#update_workweek_config) | **PUT** /v2/labor/workweek-configs/{id}


# **create_break_type**
> CreateBreakTypeResponse create_break_type(body)

### Description

Creates a new `BreakType`.   A `BreakType` is a template for creating `Break` objects.  You must provide the following values in your request to this endpoint:  - `location_id` - `break_name` - `expected_duration` - `is_paid`  You can only have 3 `BreakType` instances per location. If you attempt to add a 4th `BreakType` for a location, an `INVALID_REQUEST_ERROR` \"Exceeded limit of 3 breaks per location.\" is returned.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBreakTypeRequest**](CreateBreakTypeRequest.md)| 

### Return type

[**CreateBreakTypeResponse**](CreateBreakTypeResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shift**
> CreateShiftResponse create_shift(body)

### Description

Creates a new `Shift`.   A `Shift` represents a complete work day for a single employee.  You must provide the following values in your request to this endpoint:  - `location_id` - `employee_id` - `start_at`  An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when: - The `status` of the new `Shift` is `OPEN` and the employee has another  shift with an `OPEN` status.  - The `start_at` date is in the future - the `start_at` or `end_at` overlaps another shift for the same employee - If `Break`s are set in the request, a break `start_at` must not be before the `Shift.start_at`. A break `end_at` must not be after the `Shift.end_at`

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**CreateShiftRequest**](CreateShiftRequest.md)| 

### Return type

[**CreateShiftResponse**](CreateShiftResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_break_type**
> DeleteBreakTypeResponse delete_break_type(id)

### Description

Deletes an existing `BreakType`.   A `BreakType` can be deleted even if it is referenced from a `Shift`.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **id** | **str**| 

### Return type

[**DeleteBreakTypeResponse**](DeleteBreakTypeResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shift**
> DeleteShiftResponse delete_shift(id)

### Description

Deletes a `Shift`.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **id** | **str**| 

### Return type

[**DeleteShiftResponse**](DeleteShiftResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_break_type**
> GetBreakTypeResponse get_break_type(id)

### Description

Returns a single `BreakType` specified by id.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **id** | **str**| 

### Return type

[**GetBreakTypeResponse**](GetBreakTypeResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_wage**
> GetEmployeeWageResponse get_employee_wage(id)

### Description

Returns a single `EmployeeWage` specified by id.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **id** | **str**| 

### Return type

[**GetEmployeeWageResponse**](GetEmployeeWageResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shift**
> GetShiftResponse get_shift(id)

### Description

Returns a single `Shift` specified by id.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **id** | **str**| 

### Return type

[**GetShiftResponse**](GetShiftResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_break_types**
> ListBreakTypesResponse list_break_types(location_id=location_id, limit=limit, cursor=cursor)

### Description

Returns a paginated list of `BreakType` instances for a business.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**ListBreakTypesResponse**](ListBreakTypesResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_wages**
> ListEmployeeWagesResponse list_employee_wages(employee_id=employee_id, limit=limit, cursor=cursor)

### Description

Returns a paginated list of `EmployeeWage` instances for a business.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**ListEmployeeWagesResponse**](ListEmployeeWagesResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workweek_configs**
> ListWorkweekConfigsResponse list_workweek_configs(limit=limit, cursor=cursor)

### Description

Returns a list of `WorkweekConfig` instances for a business.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **limit** | **int**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**ListWorkweekConfigsResponse**](ListWorkweekConfigsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_shifts**
> SearchShiftsResponse search_shifts(body)

### Description

Returns a paginated list of `Shift` records for a business.  The list to be returned can be filtered by: - Location IDs **and** - employee IDs **and** - shift status (`OPEN`, `CLOSED`) **and** - shift start **and** - shift end **and** - work day details  The list can be sorted by: - `start_at` - `end_at` - `created_at` - `updated_at`

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**SearchShiftsRequest**](SearchShiftsRequest.md)| 

### Return type

[**SearchShiftsResponse**](SearchShiftsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_break_type**
> UpdateBreakTypeResponse update_break_type(id, body)

### Description

Updates an existing `BreakType`.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **id** | **str**| 
 **body** | [**UpdateBreakTypeRequest**](UpdateBreakTypeRequest.md)| 

### Return type

[**UpdateBreakTypeResponse**](UpdateBreakTypeResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shift**
> UpdateShiftResponse update_shift(id, body)

### Description

Updates an existing `Shift`.   When adding a `Break` to a `Shift`, any earlier `Breaks` in the `Shift` have  the `end_at` property set to a valid RFC-3339 datetime string.   When closing a `Shift`, all `Break` instances in the shift must be complete with `end_at` set on each `Break`.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **id** | **str**| 
 **body** | [**UpdateShiftRequest**](UpdateShiftRequest.md)| 

### Return type

[**UpdateShiftResponse**](UpdateShiftResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workweek_config**
> UpdateWorkweekConfigResponse update_workweek_config(id, body)

### Description

Updates a `WorkweekConfig`.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **id** | **str**| 
 **body** | [**UpdateWorkweekConfigRequest**](UpdateWorkweekConfigRequest.md)| 

### Return type

[**UpdateWorkweekConfigResponse**](UpdateWorkweekConfigResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

