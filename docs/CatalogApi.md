# CatalogApi
> squareconnect.apis.catalog_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**batch_delete_catalog_objects**](CatalogApi.md#batch_delete_catalog_objects) | **POST** /v2/catalog/batch-delete
[**batch_retrieve_catalog_objects**](CatalogApi.md#batch_retrieve_catalog_objects) | **POST** /v2/catalog/batch-retrieve
[**batch_upsert_catalog_objects**](CatalogApi.md#batch_upsert_catalog_objects) | **POST** /v2/catalog/batch-upsert
[**catalog_info**](CatalogApi.md#catalog_info) | **GET** /v2/catalog/info
[**delete_catalog_object**](CatalogApi.md#delete_catalog_object) | **DELETE** /v2/catalog/object/{object_id}
[**list_catalog**](CatalogApi.md#list_catalog) | **GET** /v2/catalog/list
[**retrieve_catalog_object**](CatalogApi.md#retrieve_catalog_object) | **GET** /v2/catalog/object/{object_id}
[**search_catalog_objects**](CatalogApi.md#search_catalog_objects) | **POST** /v2/catalog/search
[**update_item_modifier_lists**](CatalogApi.md#update_item_modifier_lists) | **POST** /v2/catalog/update-item-modifier-lists
[**update_item_taxes**](CatalogApi.md#update_item_taxes) | **POST** /v2/catalog/update-item-taxes
[**upsert_catalog_object**](CatalogApi.md#upsert_catalog_object) | **POST** /v2/catalog/object


# **batch_delete_catalog_objects**
> BatchDeleteCatalogObjectsResponse batch_delete_catalog_objects(body)

### Description

Deletes a set of [CatalogItem](#type-catalogitem)s based on the provided list of target IDs and returns a set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted object are also deleted. For example, deleting a CatalogItem will also delete all of its [CatalogItemVariation](#type-catalogitemvariation) children.  `BatchDeleteCatalogObjects` succeeds even if only a portion of the targeted IDs can be deleted. The response will only include IDs that were actually deleted.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchDeleteCatalogObjectsRequest**](BatchDeleteCatalogObjectsRequest.md)| 

### Return type

[**BatchDeleteCatalogObjectsResponse**](BatchDeleteCatalogObjectsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_retrieve_catalog_objects**
> BatchRetrieveCatalogObjectsResponse batch_retrieve_catalog_objects(body)

### Description

Returns a set of objects based on the provided ID. [CatalogItem](#type-catalogitem)s returned in the set include all of the child information including: all [CatalogItemVariation](#type-catalogitemvariation) objects, references to its [CatalogModifierList](#type-catalogmodifierlist) objects, and the ids of any [CatalogTax](#type-catalogtax) objects that apply to it.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchRetrieveCatalogObjectsRequest**](BatchRetrieveCatalogObjectsRequest.md)| 

### Return type

[**BatchRetrieveCatalogObjectsResponse**](BatchRetrieveCatalogObjectsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_upsert_catalog_objects**
> BatchUpsertCatalogObjectsResponse batch_upsert_catalog_objects(body)

### Description

Creates or updates up to 10,000 target objects based on the provided list of objects. The target objects are grouped into batches and each batch is inserted/updated in an all-or-nothing manner. If an object within a batch is malformed in some way, or violates a database constraint, the entire batch containing that item will be disregarded. However, other batches in the same request may still succeed. Each batch may contain up to 1,000 objects, and batches will be processed in order as long as the total object count for the request (items, variations, modifier lists, discounts, and taxes) is no more than 10,000.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchUpsertCatalogObjectsRequest**](BatchUpsertCatalogObjectsRequest.md)| 

### Return type

[**BatchUpsertCatalogObjectsResponse**](BatchUpsertCatalogObjectsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_info**
> CatalogInfoResponse catalog_info()

### Description

Returns information about the Square Catalog API, such as batch size limits for `BatchUpsertCatalogObjects`.

### Parameters
This endpoint does not need any parameter.

### Return type

[**CatalogInfoResponse**](CatalogInfoResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_catalog_object**
> DeleteCatalogObjectResponse delete_catalog_object(object_id)

### Description

Deletes a single [CatalogObject](#type-catalogobject) based on the provided ID and returns the set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted object are also deleted. For example, deleting a [CatalogItem](#type-catalogitem) will also delete all of its [CatalogItemVariation](#type-catalogitemvariation) children.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| 

### Return type

[**DeleteCatalogObjectResponse**](DeleteCatalogObjectResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_catalog**
> ListCatalogResponse list_catalog(cursor=cursor, types=types)

### Description

Returns a list of [CatalogObject](#type-catalogobject)s that includes all objects of a set of desired types (for example, all [CatalogItem](#type-catalogitem) and [CatalogTax](#type-catalogtax) objects) in the catalog. The types parameter is specified as a comma-separated list of valid [CatalogObject](#type-catalogobject) types: `ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| [optional] 
 **types** | **str**| [optional] 

### Return type

[**ListCatalogResponse**](ListCatalogResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_catalog_object**
> RetrieveCatalogObjectResponse retrieve_catalog_object(object_id, include_related_objects=include_related_objects)

### Description

Returns a single [CatalogItem](#type-catalogitem) as a [CatalogObject](#type-catalogobject) based on the provided ID. The returned object includes all of the relevant [CatalogItem](#type-catalogitem) information including: [CatalogItemVariation](#type-catalogitemvariation) children, references to its [CatalogModifierList](#type-catalogmodifierlist) objects, and the ids of any [CatalogTax](#type-catalogtax) objects that apply to it.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| 
 **include_related_objects** | **bool**| [optional] 

### Return type

[**RetrieveCatalogObjectResponse**](RetrieveCatalogObjectResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_catalog_objects**
> SearchCatalogObjectsResponse search_catalog_objects(body)

### Description

Queries the targeted catalog using a variety of query types ([CatalogQuerySortedAttribute](#type-catalogquerysortedattribute), ([CatalogQueryExact](#type-catalogqueryexact, ([CatalogQueryRange](#type-catalogqueryrange), ([CatalogQueryText](#type-catalogquerytext), ([CatalogQueryItemsForTax](#type-catalogqueryitemsfortax), ([CatalogQueryItemsForModifierList](#type-catalogqueryitemsformodifierlist)).

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchCatalogObjectsRequest**](SearchCatalogObjectsRequest.md)| 

### Return type

[**SearchCatalogObjectsResponse**](SearchCatalogObjectsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_modifier_lists**
> UpdateItemModifierListsResponse update_item_modifier_lists(body)

### Description

Updates the [CatalogModifierList](#type-catalogmodifierlist) objects that apply to the targeted [CatalogItem](#type-catalogitem) without having to perform an upsert on the entire item.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateItemModifierListsRequest**](UpdateItemModifierListsRequest.md)| 

### Return type

[**UpdateItemModifierListsResponse**](UpdateItemModifierListsResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_taxes**
> UpdateItemTaxesResponse update_item_taxes(body)

### Description

Updates the [CatalogTax](#type-catalogtax) objects that apply to the targeted [CatalogItem](#type-catalogitem) without having to perform an upsert on the entire item.

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateItemTaxesRequest**](UpdateItemTaxesRequest.md)| 

### Return type

[**UpdateItemTaxesResponse**](UpdateItemTaxesResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_catalog_object**
> UpsertCatalogObjectResponse upsert_catalog_object(body)

### Description

Creates or updates the target [CatalogObject](#type-catalogobject).

### Parameters

Name | Type | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpsertCatalogObjectRequest**](UpsertCatalogObjectRequest.md)| 

### Return type

[**UpsertCatalogObjectResponse**](UpsertCatalogObjectResponse.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

