# OrdersApi
> squareconnect.apis.orders_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**batch_retrieve_orders**](OrdersApi.md#batch_retrieve_orders) | **POST** /v2/locations/{location_id}/orders/batch-retrieve
[**create_order**](OrdersApi.md#create_order) | **POST** /v2/locations/{location_id}/orders


# **batch_retrieve_orders**
> BatchRetrieveOrdersResponse batch_retrieve_orders(location_id, body)

### Description

Retrieves a set of [Order](#type-order)s by their IDs.  If a given Order ID does not exist, the ID is ignored instead of generating an error.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**BatchRetrieveOrdersRequest**](BatchRetrieveOrdersRequest.md)| 

### Return type

[**BatchRetrieveOrdersResponse**](BatchRetrieveOrdersResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> CreateOrderResponse create_order(location_id, body)

### Description

Creates an [Order](#type-order) that can then be referenced as `order_id` in a request to the [Charge](#endpoint-charge) endpoint. Orders specify products for purchase, along with discounts, taxes, and other settings to apply to the purchase.  To associate a created order with a request to the Charge endpoint, provide the order's `id` in the `order_id` field of your request.  You cannot modify an order after you create it. If you need to modify an order, instead create a new order with modified details.  To learn more about the Orders API, see the [Orders API Overview](/products/orders/overview).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**CreateOrderRequest**](CreateOrderRequest.md)| 

### Return type

[**CreateOrderResponse**](CreateOrderResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

