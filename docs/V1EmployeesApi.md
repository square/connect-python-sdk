# V1EmployeesApi
> squareconnect.apis.v1_employees_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**create_employee**](V1EmployeesApi.md#create_employee) | **POST** /v1/me/employees
[**create_employee_role**](V1EmployeesApi.md#create_employee_role) | **POST** /v1/me/roles
[**create_timecard**](V1EmployeesApi.md#create_timecard) | **POST** /v1/me/timecards
[**delete_timecard**](V1EmployeesApi.md#delete_timecard) | **DELETE** /v1/me/timecards/{timecard_id}
[**list_cash_drawer_shifts**](V1EmployeesApi.md#list_cash_drawer_shifts) | **GET** /v1/{location_id}/cash-drawer-shifts
[**list_employee_roles**](V1EmployeesApi.md#list_employee_roles) | **GET** /v1/me/roles
[**list_employees**](V1EmployeesApi.md#list_employees) | **GET** /v1/me/employees
[**list_timecard_events**](V1EmployeesApi.md#list_timecard_events) | **GET** /v1/me/timecards/{timecard_id}/events
[**list_timecards**](V1EmployeesApi.md#list_timecards) | **GET** /v1/me/timecards
[**retrieve_cash_drawer_shift**](V1EmployeesApi.md#retrieve_cash_drawer_shift) | **GET** /v1/{location_id}/cash-drawer-shifts/{shift_id}
[**retrieve_employee**](V1EmployeesApi.md#retrieve_employee) | **GET** /v1/me/employees/{employee_id}
[**retrieve_employee_role**](V1EmployeesApi.md#retrieve_employee_role) | **GET** /v1/me/roles/{role_id}
[**retrieve_timecard**](V1EmployeesApi.md#retrieve_timecard) | **GET** /v1/me/timecards/{timecard_id}
[**update_employee**](V1EmployeesApi.md#update_employee) | **PUT** /v1/me/employees/{employee_id}
[**update_employee_role**](V1EmployeesApi.md#update_employee_role) | **PUT** /v1/me/roles/{role_id}
[**update_timecard**](V1EmployeesApi.md#update_timecard) | **PUT** /v1/me/timecards/{timecard_id}


# **create_employee**
> V1Employee create_employee(body)

### Description

Creates an employee for a business.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**V1Employee**](V1Employee.md)| 

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_role**
> V1EmployeeRole create_employee_role(employee_role)

### Description

Creates an employee role you can then assign to employees.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **employee_role** | [**V1EmployeeRole**](V1EmployeeRole.md)| 

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timecard**
> V1Timecard create_timecard(body, batch_token=batch_token)

### Description

Creates a timecard for an employee. Each timecard corresponds to a single shift.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**V1Timecard**](V1Timecard.md)| 
 **batch_token** | **str**| [optional] 

### Return type

[**V1Timecard**](V1Timecard.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timecard**
> object delete_timecard(timecard_id)

### Description

Deletes a timecard. Deleted timecards are still accessible from Connect API endpoints, but the value of their deleted field is set to true. See Handling deleted timecards for more information.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **timecard_id** | **str**| 

### Return type

**object**

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cash_drawer_shifts**
> list[V1CashDrawerShift] list_cash_drawer_shifts(location_id, order=order, begin_time=begin_time, end_time=end_time)

### Description

Provides the details for all of a location's cash drawer shifts during a date range. The date range you specify cannot exceed 90 days.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **order** | **str**| [optional] 
 **begin_time** | **str**| [optional] 
 **end_time** | **str**| [optional] 

### Return type

[**list[V1CashDrawerShift]**](V1CashDrawerShift.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_roles**
> list[V1EmployeeRole] list_employee_roles(order=order, limit=limit, batch_token=batch_token)

### Description

Provides summary information for all of a business's employee roles.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **order** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **batch_token** | **str**| [optional] 

### Return type

[**list[V1EmployeeRole]**](V1EmployeeRole.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employees**
> list[V1Employee] list_employees(order=order, begin_updated_at=begin_updated_at, end_updated_at=end_updated_at, begin_created_at=begin_created_at, end_created_at=end_created_at, status=status, external_id=external_id, limit=limit, batch_token=batch_token)

### Description

Provides summary information for all of a business's employees.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **order** | **str**| [optional] 
 **begin_updated_at** | **str**| [optional] 
 **end_updated_at** | **str**| [optional] 
 **begin_created_at** | **str**| [optional] 
 **end_created_at** | **str**| [optional] 
 **status** | **str**| [optional] 
 **external_id** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **batch_token** | **str**| [optional] 

### Return type

[**list[V1Employee]**](V1Employee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_timecard_events**
> list[V1TimecardEvent] list_timecard_events(timecard_id)

### Description

Provides summary information for all events associated with a particular timecard.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **timecard_id** | **str**| 

### Return type

[**list[V1TimecardEvent]**](V1TimecardEvent.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_timecards**
> list[V1Timecard] list_timecards(order=order, employee_id=employee_id, begin_clockin_time=begin_clockin_time, end_clockin_time=end_clockin_time, begin_clockout_time=begin_clockout_time, end_clockout_time=end_clockout_time, begin_updated_at=begin_updated_at, end_updated_at=end_updated_at, deleted=deleted, limit=limit, cursor=cursor)

### Description

Provides summary information for all of a business's employee timecards.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **order** | **str**| [optional] 
 **employee_id** | **str**| [optional] 
 **begin_clockin_time** | **str**| [optional] 
 **end_clockin_time** | **str**| [optional] 
 **begin_clockout_time** | **str**| [optional] 
 **end_clockout_time** | **str**| [optional] 
 **begin_updated_at** | **str**| [optional] 
 **end_updated_at** | **str**| [optional] 
 **deleted** | **bool**| [optional] 
 **limit** | **int**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**list[V1Timecard]**](V1Timecard.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_cash_drawer_shift**
> V1CashDrawerShift retrieve_cash_drawer_shift(location_id, shift_id)

### Description

Provides the details for a single cash drawer shift, including all events that occurred during the shift.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **shift_id** | **str**| 

### Return type

[**V1CashDrawerShift**](V1CashDrawerShift.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_employee**
> V1Employee retrieve_employee(employee_id)

### Description

Provides the details for a single employee.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| 

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_employee_role**
> V1EmployeeRole retrieve_employee_role(role_id)

### Description

Provides the details for a single employee role.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| 

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_timecard**
> V1Timecard retrieve_timecard(timecard_id)

### Description

Provides the details for a single timecard.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **timecard_id** | **str**| 

### Return type

[**V1Timecard**](V1Timecard.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee**
> V1Employee update_employee(employee_id, body)

### Description

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| 
 **body** | [**V1Employee**](V1Employee.md)| 

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_role**
> V1EmployeeRole update_employee_role(role_id, body)

### Description

Modifies the details of an employee role.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| 
 **body** | [**V1EmployeeRole**](V1EmployeeRole.md)| 

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_timecard**
> V1Timecard update_timecard(timecard_id, body)

### Description

Modifies a timecard's details. This creates an API_EDIT event for the timecard. You can view a timecard's event history with the List Timecard Events endpoint.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **timecard_id** | **str**| 
 **body** | [**V1Timecard**](V1Timecard.md)| 

### Return type

[**V1Timecard**](V1Timecard.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

