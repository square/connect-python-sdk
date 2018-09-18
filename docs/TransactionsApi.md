# TransactionsApi
> squareconnect.apis.transactions_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**capture_transaction**](TransactionsApi.md#capture_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/capture
[**charge**](TransactionsApi.md#charge) | **POST** /v2/locations/{location_id}/transactions
[**create_refund**](TransactionsApi.md#create_refund) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/refund
[**list_refunds**](TransactionsApi.md#list_refunds) | **GET** /v2/locations/{location_id}/refunds
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /v2/locations/{location_id}/transactions
[**retrieve_transaction**](TransactionsApi.md#retrieve_transaction) | **GET** /v2/locations/{location_id}/transactions/{transaction_id}
[**void_transaction**](TransactionsApi.md#void_transaction) | **POST** /v2/locations/{location_id}/transactions/{transaction_id}/void


# **capture_transaction**
> CaptureTransactionResponse capture_transaction(location_id, transaction_id)

### Description

Captures a transaction that was created with the [Charge](#endpoint-charge) endpoint with a `delay_capture` value of `true`.  See [Delayed capture transactions](/payments/transactions/overview#delayed-capture) for more information.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **transaction_id** | **str**| 

### Return type

[**CaptureTransactionResponse**](CaptureTransactionResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge**
> ChargeResponse charge(location_id, body)

### Description

Charges a card represented by a card nonce or a customer's card on file.  Your request to this endpoint must include _either_:  - A value for the `card_nonce` parameter (to charge a card nonce generated with the `SqPaymentForm`) - Values for the `customer_card_id` and `customer_id` parameters (to charge a customer's card on file)  In order for an eCommerce payment to potentially qualify for [Square chargeback protection](https://squareup.com/help/article/5394), you _must_ provide values for the following parameters in your request:  - `buyer_email_address` - At least one of `billing_address` or `shipping_address`  When this response is returned, the amount of Square's processing fee might not yet be calculated. To obtain the processing fee, wait about ten seconds and call [RetrieveTransaction](#endpoint-retrievetransaction). See the `processing_fee_money` field of each [Tender included](#type-tender) in the transaction.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**ChargeRequest**](ChargeRequest.md)| 

### Return type

[**ChargeResponse**](ChargeResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_refund**
> CreateRefundResponse create_refund(location_id, transaction_id, body)

### Description

Initiates a refund for a previously charged tender.  You must issue a refund within 120 days of the associated payment. See [this article](https://squareup.com/help/us/en/article/5060) for more information on refund behavior.  NOTE: Card-present transactions with Interac credit cards **cannot be refunded using the Connect API**. Interac transactions must refunded in-person (e.g., dipping the card using POS app).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **transaction_id** | **str**| 
 **body** | [**CreateRefundRequest**](CreateRefundRequest.md)| 

### Return type

[**CreateRefundResponse**](CreateRefundResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_refunds**
> ListRefundsResponse list_refunds(location_id, begin_time=begin_time, end_time=end_time, sort_order=sort_order, cursor=cursor)

### Description

Lists refunds for one of a business's locations.  In addition to full or partial tender refunds processed through Square APIs, refunds may result from itemized returns or exchanges through Square's Point of Sale applications.  Refunds with a `status` of `PENDING` are not currently included in this endpoint's response.  Max results per [page](#paginatingresults): 50

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
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

# **list_transactions**
> ListTransactionsResponse list_transactions(location_id, begin_time=begin_time, end_time=end_time, sort_order=sort_order, cursor=cursor)

### Description

Lists transactions for a particular location.  Transactions include payment information from sales and exchanges and refund information from returns and exchanges.  Max results per [page](#paginatingresults): 50

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
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
> RetrieveTransactionResponse retrieve_transaction(location_id, transaction_id)

### Description

Retrieves details for a single transaction.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **transaction_id** | **str**| 

### Return type

[**RetrieveTransactionResponse**](RetrieveTransactionResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_transaction**
> VoidTransactionResponse void_transaction(location_id, transaction_id)

### Description

Cancels a transaction that was created with the [Charge](#endpoint-charge) endpoint with a `delay_capture` value of `true`.  See [Delayed capture transactions](/payments/transactions/overview#delayed-capture) for more information.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **transaction_id** | **str**| 

### Return type

[**VoidTransactionResponse**](VoidTransactionResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

