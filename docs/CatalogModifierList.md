# CatalogModifierList
> squareconnect.models.catalog_modifier_list

### Description

A modifier list in the Catalog object model. A [CatalogModifierList](#type-catalogmodifierlist) contains [Modifier](#type-catalogmodifier)s that can be applied to a [CatalogItem](#type-catalogitem) at the time of sale.  For example, a modifier list \"Condiments\" that would apply to a \"Hot Dog\" [CatalogItem](#type-catalogitem) might contain [CatalogModifier](#type-catalogmodifier)s \"Ketchup\", \"Mustard\", and \"Relish\". The `selection_type` field specifies whether or not multiple selections from the modifier list are allowed.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**name** | **str** | 
**selection_type** | **str** | [optional] 
**modifiers** | [**list[CatalogObject]**](CatalogObject.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


