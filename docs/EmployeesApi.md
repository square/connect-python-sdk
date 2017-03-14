# EmployeesApi
> squareconnect.apis.employees_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**v1_create_employee**](EmployeesApi.md#v1_create_employee) | **POST** /v1/me/employees
[**v1_create_employee_role**](EmployeesApi.md#v1_create_employee_role) | **POST** /v1/me/roles
[**v1_create_timecard**](EmployeesApi.md#v1_create_timecard) | **POST** /v1/me/timecards
[**v1_delete_timecard**](EmployeesApi.md#v1_delete_timecard) | **DELETE** /v1/me/timecards/{timecard_id}
[**v1_list_cash_drawer_shifts**](EmployeesApi.md#v1_list_cash_drawer_shifts) | **GET** /v1/{location_id}/cash-drawer-shifts
[**v1_list_employee_roles**](EmployeesApi.md#v1_list_employee_roles) | **GET** /v1/me/roles
[**v1_list_employees**](EmployeesApi.md#v1_list_employees) | **GET** /v1/me/employees
[**v1_list_timecard_events**](EmployeesApi.md#v1_list_timecard_events) | **GET** /v1/me/timecards/{timecard_id}/events
[**v1_list_timecards**](EmployeesApi.md#v1_list_timecards) | **GET** /v1/me/timecards
[**v1_retrieve_cash_drawer_shift**](EmployeesApi.md#v1_retrieve_cash_drawer_shift) | **GET** /v1/{location_id}/cash-drawer-shifts/{shift_id}
[**v1_retrieve_employee**](EmployeesApi.md#v1_retrieve_employee) | **GET** /v1/me/employees/{employee_id}
[**v1_retrieve_employee_role**](EmployeesApi.md#v1_retrieve_employee_role) | **GET** /v1/me/roles/{role_id}
[**v1_retrieve_timecard**](EmployeesApi.md#v1_retrieve_timecard) | **GET** /v1/me/timecards/{timecard_id}
[**v1_update_employee**](EmployeesApi.md#v1_update_employee) | **PUT** /v1/me/employees/{employee_id}
[**v1_update_employee_role**](EmployeesApi.md#v1_update_employee_role) | **PUT** /v1/me/roles/{role_id}
[**v1_update_timecard**](EmployeesApi.md#v1_update_timecard) | **PUT** /v1/me/timecards/{timecard_id}


# **v1_create_employee**
> V1Employee v1_create_employee(body)

### Description

Creates an employee for a business.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Employee**](V1Employee.md)| 

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_employee_role**
> V1EmployeeRole v1_create_employee_role(employee_role)

### Description

Creates an employee role you can then assign to employees.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **employee_role** | [**V1EmployeeRole**](V1EmployeeRole.md)| 

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_timecard**
> V1Timecard v1_create_timecard(body)

### Description

Creates a timecard for an employee. Each timecard corresponds to a single shift.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Timecard**](V1Timecard.md)| 

### Return type

[**V1Timecard**](V1Timecard.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_timecard**
> object v1_delete_timecard(timecard_id)

### Description

Deletes a timecard. Deleted timecards are still accessible from Connect API endpoints, but the value of their deleted field is set to true. See Handling deleted timecards for more information.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **timecard_id** | **str**| 

### Return type

**object**

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_cash_drawer_shifts**
> list[V1CashDrawerShift] v1_list_cash_drawer_shifts(location_id, order=order, begin_time=begin_time, end_time=end_time)

### Description

Provides the details for all of a location's cash drawer shifts during a date range. The date range you specify cannot exceed 90 days.

### Parameters

Name | Type | Notes
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

# **v1_list_employee_roles**
> list[V1EmployeeRole] v1_list_employee_roles(order=order, limit=limit, cursor=cursor)

### Description

Provides summary information for all of a business's employee roles.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| [optional] 
 **limit** | **int**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**list[V1EmployeeRole]**](V1EmployeeRole.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_employees**
> list[V1Employee] v1_list_employees(order=order, begin_updated_at=begin_updated_at, end_updated_at=end_updated_at, begin_created_at=begin_created_at, end_created_at=end_created_at, status=status, external_id=external_id, limit=limit)

### Description

Provides summary information for all of a business's employees.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| [optional] 
 **begin_updated_at** | **str**| [optional] 
 **end_updated_at** | **str**| [optional] 
 **begin_created_at** | **str**| [optional] 
 **end_created_at** | **str**| [optional] 
 **status** | **str**| [optional] 
 **external_id** | **str**| [optional] 
 **limit** | **int**| [optional] 

### Return type

[**list[V1Employee]**](V1Employee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_timecard_events**
> list[V1TimecardEvent] v1_list_timecard_events(timecard_id)

### Description

Provides summary information for all events associated with a particular timecard.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **timecard_id** | **str**| 

### Return type

[**list[V1TimecardEvent]**](V1TimecardEvent.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_timecards**
> list[V1Timecard] v1_list_timecards(order=order, employee_id=employee_id, begin_clockin_time=begin_clockin_time, end_clockin_time=end_clockin_time, begin_clockout_time=begin_clockout_time, end_clockout_time=end_clockout_time, begin_updated_at=begin_updated_at, end_updated_at=end_updated_at, deleted=deleted, limit=limit, cursor=cursor)

### Description

Provides summary information for all of a business's employee timecards.

### Parameters

Name | Type | Notes
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

# **v1_retrieve_cash_drawer_shift**
> V1CashDrawerShift v1_retrieve_cash_drawer_shift(location_id, shift_id)

### Description

Provides the details for a single cash drawer shift, including all events that occurred during the shift.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **shift_id** | **str**| 

### Return type

[**V1CashDrawerShift**](V1CashDrawerShift.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_retrieve_employee**
> V1Employee v1_retrieve_employee(employee_id)

### Description

Provides the details for a single employee.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| 

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_retrieve_employee_role**
> V1EmployeeRole v1_retrieve_employee_role(role_id)

### Description

Provides the details for a single employee role.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| 

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_retrieve_timecard**
> V1Timecard v1_retrieve_timecard(timecard_id)

### Description

Provides the details for a single timecard.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **timecard_id** | **str**| 

### Return type

[**V1Timecard**](V1Timecard.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_employee**
> V1Employee v1_update_employee(employee_id, body)

### Description

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| 
 **body** | [**V1Employee**](V1Employee.md)| 

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_employee_role**
> V1EmployeeRole v1_update_employee_role(role_id, body)

### Description

Modifies the details of an employee role.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| 
 **body** | [**V1EmployeeRole**](V1EmployeeRole.md)| 

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_timecard**
> V1Timecard v1_update_timecard(timecard_id, body)

### Description

Modifies a timecard's details. This creates an API_EDIT event for the timecard. You can view a timecard's event history with the List Timecard Events endpoint.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **timecard_id** | **str**| 
 **body** | [**V1Timecard**](V1Timecard.md)| 

### Return type

[**V1Timecard**](V1Timecard.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

