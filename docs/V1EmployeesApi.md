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

 Use the CreateEmployee endpoint to add an employee to a Square account. Employees created with the Connect API have an initial status of `INACTIVE`. Inactive employees cannot sign in to Square Point of Sale until they are activated from the Square Dashboard. Employee status cannot be changed with the Connect API.  <aside class=\"important\"> Employee entities cannot be deleted. To disable employee profiles, set the employee's status to <code>INACTIVE</code> </aside>

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

Creates an employee role you can then assign to employees.  Square accounts can include any number of roles that can be assigned to employees. These roles define the actions and permissions granted to an employee with that role. For example, an employee with a \"Shift Manager\" role might be able to issue refunds in Square Point of Sale, whereas an employee with a \"Clerk\" role might not.  Roles are assigned with the [V1UpdateEmployee](#endpoint-v1updateemployee) endpoint. An employee can have only one role at a time.  If an employee has no role, they have none of the permissions associated with roles. All employees can accept payments with Square Point of Sale.

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
> V1Timecard create_timecard(body)

### Description

Creates a timecard for an employee and clocks them in with an `API_CREATE` event and a `clockin_time` set to the current time unless the request provides a different value. To import timecards from another system (rather than clocking someone in). Specify the `clockin_time` and* `clockout_time` in the request.  Timecards correspond to exactly one shift for a given employee, bounded by the `clockin_time` and `clockout_time` fields. An employee is considered clocked in if they have a timecard that doesn't have a `clockout_time` set. An employee that is currently clocked in cannot be clocked in a second time.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**V1Timecard**](V1Timecard.md)| 

### Return type

[**V1Timecard**](V1Timecard.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timecard**
> object delete_timecard(timecard_id)

### Description

Deletes a timecard. Timecards can also be deleted through the Square Dashboard. Deleted timecards are still accessible through Connect API endpoints, but cannot be modified. The `deleted` field of the `Timecard` object indicates whether the timecard has been deleted.  *Note**: By default, deleted timecards appear alongside valid timecards in results returned by the [ListTimecards](#endpoint-v1employees-listtimecards) endpoint. To filter deleted timecards, include the `deleted` query parameter in the list request.  <aside> Only approved accounts can manage their employees with Square. Unapproved accounts cannot use employee management features with the API. </aside>

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

Provides summary information for all events associated with a particular timecard.  <aside> Only approved accounts can manage their employees with Square. Unapproved accounts cannot use employee management features with the API. </aside>

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
> list[V1Timecard] list_timecards(order=order, employee_id=employee_id, begin_clockin_time=begin_clockin_time, end_clockin_time=end_clockin_time, begin_clockout_time=begin_clockout_time, end_clockout_time=end_clockout_time, begin_updated_at=begin_updated_at, end_updated_at=end_updated_at, deleted=deleted, limit=limit, batch_token=batch_token)

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
 **batch_token** | **str**| [optional] 

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

Provides the details for a single timecard. <aside> Only approved accounts can manage their employees with Square. Unapproved accounts cannot use employee management features with the API. </aside>

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

Modifies the details of a timecard with an `API_EDIT` event for the timecard. Updating an active timecard with a `clockout_time` clocks the employee out.

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

