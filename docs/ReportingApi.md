# ReportingApi
> squareconnect.apis.reporting_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**list_additional_recipient_receivable_refunds**](ReportingApi.md#list_additional_recipient_receivable_refunds) | **GET** /v2/locations/{location_id}/additional-recipient-receivable-refunds
[**list_additional_recipient_receivables**](ReportingApi.md#list_additional_recipient_receivables) | **GET** /v2/locations/{location_id}/additional-recipient-receivables


# **list_additional_recipient_receivable_refunds**
> ListAdditionalRecipientReceivableRefundsResponse list_additional_recipient_receivable_refunds(location_id, begin_time=begin_time, end_time=end_time, sort_order=sort_order, cursor=cursor)

### Description

Returns a list of refunded transactions (across all possible originating locations) relating to monies credited to the provided location ID by another Square account using the `additional_recipients` field in a transaction.  Max results per [page](#paginatingresults): 50

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **begin_time** | **str**| [optional] 
 **end_time** | **str**| [optional] 
 **sort_order** | **str**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**ListAdditionalRecipientReceivableRefundsResponse**](ListAdditionalRecipientReceivableRefundsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_additional_recipient_receivables**
> ListAdditionalRecipientReceivablesResponse list_additional_recipient_receivables(location_id, begin_time=begin_time, end_time=end_time, sort_order=sort_order, cursor=cursor)

### Description

Returns a list of receivables (across all possible sending locations) representing monies credited to the provided location ID by another Square account using the `additional_recipients` field in a transaction.  Max results per [page](#paginatingresults): 50

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **begin_time** | **str**| [optional] 
 **end_time** | **str**| [optional] 
 **sort_order** | **str**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**ListAdditionalRecipientReceivablesResponse**](ListAdditionalRecipientReceivablesResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

