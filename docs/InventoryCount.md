# InventoryCount
> squareconnect.models.inventory_count

### Description

Represents the estimated quantity of items in a particular state at a particular location based on the known history of physical counts and inventory adjustments.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_object_id** | **str** | The Square generated ID of the [CatalogObject](#type-catalogobject) being tracked. | [optional] 
**catalog_object_type** | **str** | The [CatalogObjectType](#type-catalogobjecttype) of the [CatalogObject](#type-catalogobject) being tracked. Tracking is only supported for the &#x60;ITEM_VARIATION&#x60; type. | [optional] 
**state** | **str** | The current [InventoryState](#type-inventorystate) for the related quantity of items. | [optional] 
**location_id** | **str** | The Square ID of the [Location](#type-location) where the related quantity of items are being tracked. | [optional] 
**quantity** | **str** | The number of items in the count as a decimal string. Fractional quantities are not supported. | [optional] 
**calculated_at** | **str** | A read-only timestamp in RFC 3339 format that indicates when Square received the most recent physical count or adjustment that had an affect on the estimated count. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


