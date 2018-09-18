# InventoryApi
> squareconnect.apis.inventory_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**batch_change_inventory**](InventoryApi.md#batch_change_inventory) | **POST** /v2/inventory/batch-change
[**batch_retrieve_inventory_changes**](InventoryApi.md#batch_retrieve_inventory_changes) | **POST** /v2/inventory/batch-retrieve-changes
[**batch_retrieve_inventory_counts**](InventoryApi.md#batch_retrieve_inventory_counts) | **POST** /v2/inventory/batch-retrieve-counts
[**retrieve_inventory_adjustment**](InventoryApi.md#retrieve_inventory_adjustment) | **GET** /v2/inventory/adjustment/{adjustment_id}
[**retrieve_inventory_changes**](InventoryApi.md#retrieve_inventory_changes) | **GET** /v2/inventory/{catalog_object_id}/changes
[**retrieve_inventory_count**](InventoryApi.md#retrieve_inventory_count) | **GET** /v2/inventory/{catalog_object_id}
[**retrieve_inventory_physical_count**](InventoryApi.md#retrieve_inventory_physical_count) | **GET** /v2/inventory/physical-count/{physical_count_id}


# **batch_change_inventory**
> BatchChangeInventoryResponse batch_change_inventory(body)

### Description

Applies adjustments and counts to the provided item quantities.  On success: returns the current calculated counts for all objects referenced in the request. On failure: returns a list of related errors.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**BatchChangeInventoryRequest**](BatchChangeInventoryRequest.md)| 

### Return type

[**BatchChangeInventoryResponse**](BatchChangeInventoryResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_retrieve_inventory_changes**
> BatchRetrieveInventoryChangesResponse batch_retrieve_inventory_changes(body)

### Description

Returns historical physical counts and adjustments based on the provided filter criteria.  Results are paginated and sorted in ascending order according their `occurred_at` timestamp (oldest first).  BatchRetrieveInventoryChanges is a catch-all query endpoint for queries that cannot be handled by other, simpler endpoints.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**BatchRetrieveInventoryChangesRequest**](BatchRetrieveInventoryChangesRequest.md)| 

### Return type

[**BatchRetrieveInventoryChangesResponse**](BatchRetrieveInventoryChangesResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_retrieve_inventory_counts**
> BatchRetrieveInventoryCountsResponse batch_retrieve_inventory_counts(body)

### Description

Returns current counts for the provided [CatalogObject](#type-catalogobject)s at the requested [Location](#type-location)s.  Results are paginated and sorted in descending order according to their `calculated_at` timestamp (newest first).  When `updated_at` is specified, only counts that have changed since that time (based on the server timestamp for the most recent change) are returned. This allows clients to perform a \"sync\" operation, for example in response to receiving a Webhook notification.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **body** | [**BatchRetrieveInventoryCountsRequest**](BatchRetrieveInventoryCountsRequest.md)| 

### Return type

[**BatchRetrieveInventoryCountsResponse**](BatchRetrieveInventoryCountsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_inventory_adjustment**
> RetrieveInventoryAdjustmentResponse retrieve_inventory_adjustment(adjustment_id)

### Description

Returns the [InventoryAdjustment](#type-inventoryadjustment) object with the provided `adjustment_id`.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **adjustment_id** | **str**| 

### Return type

[**RetrieveInventoryAdjustmentResponse**](RetrieveInventoryAdjustmentResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_inventory_changes**
> RetrieveInventoryChangesResponse retrieve_inventory_changes(catalog_object_id, location_ids=location_ids, cursor=cursor)

### Description

Returns a set of physical counts and inventory adjustments for the provided [CatalogObject](#type-catalogobject) at the requested [Location](#type-location)s.  Results are paginated and sorted in descending order according to their `occurred_at` timestamp (newest first).  There are no limits on how far back the caller can page. This endpoint is useful when displaying recent changes for a specific item. For more sophisticated queries, use a batch endpoint.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **catalog_object_id** | **str**| 
 **location_ids** | **str**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**RetrieveInventoryChangesResponse**](RetrieveInventoryChangesResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_inventory_count**
> RetrieveInventoryCountResponse retrieve_inventory_count(catalog_object_id, location_ids=location_ids, cursor=cursor)

### Description

Retrieves the current calculated stock count for a given [CatalogObject](#type-catalogobject) at a given set of [Location](#type-location)s. Responses are paginated and unsorted. For more sophisticated queries, use a batch endpoint.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **catalog_object_id** | **str**| 
 **location_ids** | **str**| [optional] 
 **cursor** | **str**| [optional] 

### Return type

[**RetrieveInventoryCountResponse**](RetrieveInventoryCountResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_inventory_physical_count**
> RetrieveInventoryPhysicalCountResponse retrieve_inventory_physical_count(physical_count_id)

### Description

Returns the [InventoryPhysicalCount](#type-inventoryphysicalcount) object with the provided `physical_count_id`.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **physical_count_id** | **str**| 

### Return type

[**RetrieveInventoryPhysicalCountResponse**](RetrieveInventoryPhysicalCountResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

