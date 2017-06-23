# V1ItemsApi
> squareconnect.apis.v1_items_api

All endpoints are relative to [Square Connect V2 Documentation](https://docs.connect.squareup.com/api/connect/v2/#navsection-endpoints)


Method | HTTP request 
------------- | -------------
[**adjust_inventory**](V1ItemsApi.md#adjust_inventory) | **POST** /v1/{location_id}/inventory/{variation_id}
[**apply_fee**](V1ItemsApi.md#apply_fee) | **PUT** /v1/{location_id}/items/{item_id}/fees/{fee_id}
[**apply_modifier_list**](V1ItemsApi.md#apply_modifier_list) | **PUT** /v1/{location_id}/items/{item_id}/modifier-lists/{modifier_list_id}
[**create_category**](V1ItemsApi.md#create_category) | **POST** /v1/{location_id}/categories
[**create_discount**](V1ItemsApi.md#create_discount) | **POST** /v1/{location_id}/discounts
[**create_fee**](V1ItemsApi.md#create_fee) | **POST** /v1/{location_id}/fees
[**create_item**](V1ItemsApi.md#create_item) | **POST** /v1/{location_id}/items
[**create_modifier_list**](V1ItemsApi.md#create_modifier_list) | **POST** /v1/{location_id}/modifier-lists
[**create_modifier_option**](V1ItemsApi.md#create_modifier_option) | **POST** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options
[**create_page**](V1ItemsApi.md#create_page) | **POST** /v1/{location_id}/pages
[**create_variation**](V1ItemsApi.md#create_variation) | **POST** /v1/{location_id}/items/{item_id}/variations
[**delete_category**](V1ItemsApi.md#delete_category) | **DELETE** /v1/{location_id}/categories/{category_id}
[**delete_discount**](V1ItemsApi.md#delete_discount) | **DELETE** /v1/{location_id}/discounts/{discount_id}
[**delete_fee**](V1ItemsApi.md#delete_fee) | **DELETE** /v1/{location_id}/fees/{fee_id}
[**delete_item**](V1ItemsApi.md#delete_item) | **DELETE** /v1/{location_id}/items/{item_id}
[**delete_modifier_list**](V1ItemsApi.md#delete_modifier_list) | **DELETE** /v1/{location_id}/modifier-lists/{modifier_list_id}
[**delete_modifier_option**](V1ItemsApi.md#delete_modifier_option) | **DELETE** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options/{modifier_option_id}
[**delete_page**](V1ItemsApi.md#delete_page) | **DELETE** /v1/{location_id}/pages/{page_id}
[**delete_page_cell**](V1ItemsApi.md#delete_page_cell) | **DELETE** /v1/{location_id}/pages/{page_id}/cells
[**delete_variation**](V1ItemsApi.md#delete_variation) | **DELETE** /v1/{location_id}/items/{item_id}/variations/{variation_id}
[**list_categories**](V1ItemsApi.md#list_categories) | **GET** /v1/{location_id}/categories
[**list_discounts**](V1ItemsApi.md#list_discounts) | **GET** /v1/{location_id}/discounts
[**list_fees**](V1ItemsApi.md#list_fees) | **GET** /v1/{location_id}/fees
[**list_inventory**](V1ItemsApi.md#list_inventory) | **GET** /v1/{location_id}/inventory
[**list_items**](V1ItemsApi.md#list_items) | **GET** /v1/{location_id}/items
[**list_modifier_lists**](V1ItemsApi.md#list_modifier_lists) | **GET** /v1/{location_id}/modifier-lists
[**list_pages**](V1ItemsApi.md#list_pages) | **GET** /v1/{location_id}/pages
[**remove_fee**](V1ItemsApi.md#remove_fee) | **DELETE** /v1/{location_id}/items/{item_id}/fees/{fee_id}
[**remove_modifier_list**](V1ItemsApi.md#remove_modifier_list) | **DELETE** /v1/{location_id}/items/{item_id}/modifier-lists/{modifier_list_id}
[**retrieve_item**](V1ItemsApi.md#retrieve_item) | **GET** /v1/{location_id}/items/{item_id}
[**retrieve_modifier_list**](V1ItemsApi.md#retrieve_modifier_list) | **GET** /v1/{location_id}/modifier-lists/{modifier_list_id}
[**update_category**](V1ItemsApi.md#update_category) | **PUT** /v1/{location_id}/categories/{category_id}
[**update_discount**](V1ItemsApi.md#update_discount) | **PUT** /v1/{location_id}/discounts/{discount_id}
[**update_fee**](V1ItemsApi.md#update_fee) | **PUT** /v1/{location_id}/fees/{fee_id}
[**update_item**](V1ItemsApi.md#update_item) | **PUT** /v1/{location_id}/items/{item_id}
[**update_modifier_list**](V1ItemsApi.md#update_modifier_list) | **PUT** /v1/{location_id}/modifier-lists/{modifier_list_id}
[**update_modifier_option**](V1ItemsApi.md#update_modifier_option) | **PUT** /v1/{location_id}/modifier-lists/{modifier_list_id}/modifier-options/{modifier_option_id}
[**update_page**](V1ItemsApi.md#update_page) | **PUT** /v1/{location_id}/pages/{page_id}
[**update_page_cell**](V1ItemsApi.md#update_page_cell) | **PUT** /v1/{location_id}/pages/{page_id}/cells
[**update_variation**](V1ItemsApi.md#update_variation) | **PUT** /v1/{location_id}/items/{item_id}/variations/{variation_id}


# **adjust_inventory**
> V1InventoryEntry adjust_inventory(location_id, variation_id, body)

### Description

Adjusts an item variation's current available inventory.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **variation_id** | **str**| 
 **body** | [**V1AdjustInventoryRequest**](V1AdjustInventoryRequest.md)| 

### Return type

[**V1InventoryEntry**](V1InventoryEntry.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_fee**
> V1Item apply_fee(location_id, item_id, fee_id)

### Description

Associates a fee with an item, meaning the fee is automatically applied to the item in Square Register.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **item_id** | **str**| 
 **fee_id** | **str**| 

### Return type

[**V1Item**](V1Item.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_modifier_list**
> V1Item apply_modifier_list(location_id, modifier_list_id, item_id)

### Description

Associates a modifier list with an item, meaning modifier options from the list can be applied to the item.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **modifier_list_id** | **str**| 
 **item_id** | **str**| 

### Return type

[**V1Item**](V1Item.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_category**
> V1Category create_category(location_id, body)

### Description

Creates an item category.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**V1Category**](V1Category.md)| 

### Return type

[**V1Category**](V1Category.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_discount**
> V1Discount create_discount(location_id, body)

### Description

Creates a discount.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**V1Discount**](V1Discount.md)| 

### Return type

[**V1Discount**](V1Discount.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fee**
> V1Fee create_fee(location_id, body)

### Description

Creates a fee (tax).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**V1Fee**](V1Fee.md)| 

### Return type

[**V1Fee**](V1Fee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item**
> V1Item create_item(location_id, body, batch_token=batch_token)

### Description

Creates an item and at least one variation for it.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**V1Item**](V1Item.md)| 
 **batch_token** | **str**| [optional] 

### Return type

[**V1Item**](V1Item.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_modifier_list**
> V1ModifierList create_modifier_list(location_id, body)

### Description

Creates an item modifier list and at least one modifier option for it.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**V1ModifierList**](V1ModifierList.md)| 

### Return type

[**V1ModifierList**](V1ModifierList.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_modifier_option**
> V1ModifierOption create_modifier_option(location_id, modifier_list_id, body)

### Description

Creates an item modifier option and adds it to a modifier list.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **modifier_list_id** | **str**| 
 **body** | [**V1ModifierOption**](V1ModifierOption.md)| 

### Return type

[**V1ModifierOption**](V1ModifierOption.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_page**
> V1Page create_page(location_id, body)

### Description

Creates a Favorites page in Square Register.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **body** | [**V1Page**](V1Page.md)| 

### Return type

[**V1Page**](V1Page.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_variation**
> V1Variation create_variation(location_id, item_id, body)

### Description

Creates an item variation for an existing item.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **item_id** | **str**| 
 **body** | [**V1Variation**](V1Variation.md)| 

### Return type

[**V1Variation**](V1Variation.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> V1Category delete_category(location_id, category_id)

### Description

Deletes an existing item category.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **category_id** | **str**| 

### Return type

[**V1Category**](V1Category.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_discount**
> V1Discount delete_discount(location_id, discount_id)

### Description

Deletes an existing discount.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **discount_id** | **str**| 

### Return type

[**V1Discount**](V1Discount.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fee**
> V1Fee delete_fee(location_id, fee_id)

### Description

Deletes an existing fee (tax).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **fee_id** | **str**| 

### Return type

[**V1Fee**](V1Fee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> V1Item delete_item(location_id, item_id)

### Description

Deletes an existing item and all item variations associated with it.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **item_id** | **str**| 

### Return type

[**V1Item**](V1Item.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_modifier_list**
> V1ModifierList delete_modifier_list(location_id, modifier_list_id)

### Description

Deletes an existing item modifier list and all modifier options associated with it.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **modifier_list_id** | **str**| 

### Return type

[**V1ModifierList**](V1ModifierList.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_modifier_option**
> V1ModifierOption delete_modifier_option(location_id, modifier_list_id, modifier_option_id)

### Description

Deletes an existing item modifier option from a modifier list.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **modifier_list_id** | **str**| 
 **modifier_option_id** | **str**| 

### Return type

[**V1ModifierOption**](V1ModifierOption.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page**
> V1Page delete_page(location_id, page_id)

### Description

Deletes an existing Favorites page and all of its cells.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **page_id** | **str**| 

### Return type

[**V1Page**](V1Page.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_page_cell**
> V1Page delete_page_cell(location_id, page_id, row=row, column=column)

### Description

Deletes a cell from a Favorites page in Square Register.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **page_id** | **str**| 
 **row** | **str**| [optional] 
 **column** | **str**| [optional] 

### Return type

[**V1Page**](V1Page.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variation**
> V1Variation delete_variation(location_id, item_id, variation_id)

### Description

Deletes an existing item variation from an item.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **item_id** | **str**| 
 **variation_id** | **str**| 

### Return type

[**V1Variation**](V1Variation.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_categories**
> list[V1Category] list_categories(location_id)

### Description

Lists all of a location's item categories.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 

### Return type

[**list[V1Category]**](V1Category.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_discounts**
> list[V1Discount] list_discounts(location_id)

### Description

Lists all of a location's discounts.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 

### Return type

[**list[V1Discount]**](V1Discount.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fees**
> list[V1Fee] list_fees(location_id)

### Description

Lists all of a location's fees (taxes).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 

### Return type

[**list[V1Fee]**](V1Fee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory**
> list[V1InventoryEntry] list_inventory(location_id, limit=limit, batch_token=batch_token)

### Description

Provides inventory information for all of a merchant's inventory-enabled item variations.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **limit** | **int**| [optional] 
 **batch_token** | **str**| [optional] 

### Return type

[**list[V1InventoryEntry]**](V1InventoryEntry.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items**
> list[V1Item] list_items(location_id)

### Description

Provides summary information for all of a location's items.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 

### Return type

[**list[V1Item]**](V1Item.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_modifier_lists**
> list[V1ModifierList] list_modifier_lists(location_id)

### Description

Lists all of a location's modifier lists.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 

### Return type

[**list[V1ModifierList]**](V1ModifierList.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pages**
> list[V1Page] list_pages(location_id)

### Description

Lists all of a location's Favorites pages in Square Register.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 

### Return type

[**list[V1Page]**](V1Page.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_fee**
> V1Item remove_fee(location_id, item_id, fee_id)

### Description

Removes a fee assocation from an item, meaning the fee is no longer automatically applied to the item in Square Register.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **item_id** | **str**| 
 **fee_id** | **str**| 

### Return type

[**V1Item**](V1Item.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_modifier_list**
> V1Item remove_modifier_list(location_id, modifier_list_id, item_id)

### Description

Removes a modifier list association from an item, meaning modifier options from the list can no longer be applied to the item.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **modifier_list_id** | **str**| 
 **item_id** | **str**| 

### Return type

[**V1Item**](V1Item.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_item**
> V1Item retrieve_item(location_id, item_id)

### Description

Provides the details for a single item, including associated modifier lists and fees.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **item_id** | **str**| 

### Return type

[**V1Item**](V1Item.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_modifier_list**
> V1ModifierList retrieve_modifier_list(location_id, modifier_list_id)

### Description

Provides the details for a single modifier list.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **modifier_list_id** | **str**| 

### Return type

[**V1ModifierList**](V1ModifierList.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> V1Category update_category(location_id, category_id, body)

### Description

Modifies the details of an existing item category.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **category_id** | **str**| 
 **body** | [**V1Category**](V1Category.md)| 

### Return type

[**V1Category**](V1Category.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_discount**
> V1Discount update_discount(location_id, discount_id, body)

### Description

Modifies the details of an existing discount.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **discount_id** | **str**| 
 **body** | [**V1Discount**](V1Discount.md)| 

### Return type

[**V1Discount**](V1Discount.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fee**
> V1Fee update_fee(location_id, fee_id, body)

### Description

Modifies the details of an existing fee (tax).

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **fee_id** | **str**| 
 **body** | [**V1Fee**](V1Fee.md)| 

### Return type

[**V1Fee**](V1Fee.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item**
> V1Item update_item(location_id, item_id, body)

### Description

Modifies the core details of an existing item.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **item_id** | **str**| 
 **body** | [**V1Item**](V1Item.md)| 

### Return type

[**V1Item**](V1Item.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_modifier_list**
> V1ModifierList update_modifier_list(location_id, modifier_list_id, body)

### Description

Modifies the details of an existing item modifier list.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **modifier_list_id** | **str**| 
 **body** | [**V1UpdateModifierListRequest**](V1UpdateModifierListRequest.md)| 

### Return type

[**V1ModifierList**](V1ModifierList.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_modifier_option**
> V1ModifierOption update_modifier_option(location_id, modifier_list_id, modifier_option_id, body)

### Description

Modifies the details of an existing item modifier option.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **modifier_list_id** | **str**| 
 **modifier_option_id** | **str**| 
 **body** | [**V1ModifierOption**](V1ModifierOption.md)| 

### Return type

[**V1ModifierOption**](V1ModifierOption.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_page**
> V1Page update_page(location_id, page_id, body)

### Description

Modifies the details of a Favorites page in Square Register.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **page_id** | **str**| 
 **body** | [**V1Page**](V1Page.md)| 

### Return type

[**V1Page**](V1Page.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_page_cell**
> V1Page update_page_cell(location_id, page_id, body)

### Description

Modifies a cell of a Favorites page in Square Register.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **page_id** | **str**| 
 **body** | [**V1PageCell**](V1PageCell.md)| 

### Return type

[**V1Page**](V1Page.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_variation**
> V1Variation update_variation(location_id, item_id, variation_id, body)

### Description

Modifies the details of an existing item variation.

### Parameters

Name | Type | Notes | Default Value
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| 
 **item_id** | **str**| 
 **variation_id** | **str**| 
 **body** | [**V1Variation**](V1Variation.md)| 

### Return type

[**V1Variation**](V1Variation.md)

### Authorization

Assign your **Access Token** from developer portal to the authorization parameter.

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

