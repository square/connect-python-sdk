# RefundApi
> squareconnect.apis.refund_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**create_refund**](RefundApi.md#create_refund) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/refund
[**list_refunds**](RefundApi.md#list_refunds) | **GET** /v2/locations/{location_id}/refunds


# **create_refund**
> CreateRefundResponse create_refund(authorization, location_id, transaction_id, body)

### Description

Initiates a refund for a previously charged tender.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **location_id** | **str**| 
 **transaction_id** | **str**| 
 **body** | [**CreateRefundRequest**](CreateRefundRequest.md)| 

### Return type

[**CreateRefundResponse**](CreateRefundResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_refunds**
> ListRefundsResponse list_refunds(authorization, location_id, begin_time=begin_time, end_time=end_time, sort_order=sort_order, cursor=cursor)

### Description

Lists refunds for one of a business's locations.  Refunds with a `status` of `PENDING` are not currently included in this endpoint's response.  Max results per [page](#paginatingresults): 50

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **location_id** | **str**| 
 **begin_time** | **str**| [optional] 
 **end_time** | **str**| [optional] 
 **sort_order** | **str**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**ListRefundsResponse**](ListRefundsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

