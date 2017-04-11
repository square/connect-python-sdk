# TransactionApi
> squareconnect.apis.transaction_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**capture_transaction**](TransactionApi.md#capture_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/capture
[**charge**](TransactionApi.md#charge) | **POST** /v2/locations/{location_id}/transactions
[**list_transactions**](TransactionApi.md#list_transactions) | **GET** /v2/locations/{location_id}/transactions
[**retrieve_transaction**](TransactionApi.md#retrieve_transaction) | **GET** /v2/locations/{location_id}/transactions/{transaction_id}
[**void_transaction**](TransactionApi.md#void_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/void


# **capture_transaction**
> CaptureTransactionResponse capture_transaction(authorization, location_id, transaction_id)

### Description

Captures a transaction that was created with the [Charge](#endpoint-charge) endpoint with a `delay_capture` value of `true`.  See [Delayed capture transactions](/articles/delayed-capture-transactions/) for more information.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **location_id** | **str**| 
 **transaction_id** | **str**| 

### Return type

[**CaptureTransactionResponse**](CaptureTransactionResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge**
> ChargeResponse charge(authorization, location_id, body)

### Description

Charges a card represented by a card nonce or a customer's card on file.  Your request to this endpoint must include _either_:  - A value for the `card_nonce` parameter (to charge a card nonce generated with the `SqPaymentForm`) - Values for the `customer_card_id` and `customer_id` parameters (to charge a customer's card on file)  In order for an e-commerce payment to potentially qualify for [Square chargeback protection](https://squareup.com/help/article/5394), you _must_ provide values for the following parameters in your request:  - `buyer_email_address` - At least one of `billing_address` or `shipping_address`  When this response is returned, the amount of Square's processing fee might not yet be calculated. To obtain the processing fee, wait about ten seconds and call [RetrieveTransaction](#endpoint-retrievetransaction). See the `processing_fee_money` field of each [Tender included](#type-tender) in the transaction.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **location_id** | **str**| 
 **body** | [**ChargeRequest**](ChargeRequest.md)| 

### Return type

[**ChargeResponse**](ChargeResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> ListTransactionsResponse list_transactions(authorization, location_id, begin_time=begin_time, end_time=end_time, sort_order=sort_order, cursor=cursor)

### Description

Lists transactions for a particular location.  Max results per [page](#paginatingresults): 50

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

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction**
> RetrieveTransactionResponse retrieve_transaction(authorization, location_id, transaction_id)

### Description

Retrieves details for a single transaction.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **location_id** | **str**| 
 **transaction_id** | **str**| 

### Return type

[**RetrieveTransactionResponse**](RetrieveTransactionResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_transaction**
> VoidTransactionResponse void_transaction(authorization, location_id, transaction_id)

### Description

Cancels a transaction that was created with the [Charge](#endpoint-charge) endpoint with a `delay_capture` value of `true`.  See [Delayed capture transactions](/articles/delayed-capture-transactions/) for more information.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| 
 **location_id** | **str**| 
 **transaction_id** | **str**| 

### Return type

[**VoidTransactionResponse**](VoidTransactionResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

