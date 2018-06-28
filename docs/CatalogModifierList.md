# CatalogModifierList
> squareconnect.models.catalog_modifier_list

### Description

A modifier list in the Catalog object model. A [CatalogModifierList](#type-catalogmodifierlist) contains [Modifier](#type-catalogmodifier)s that can be applied to a [CatalogItem](#type-catalogitem) at the time of sale.  For example, a modifier list \"Condiments\" that would apply to a \"Hot Dog\" [CatalogItem](#type-catalogitem) might contain [CatalogModifier](#type-catalogmodifier)s \"Ketchup\", \"Mustard\", and \"Relish\". The `selection_type` field specifies whether or not multiple selections from the modifier list are allowed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The [CatalogModifierList](#type-catalogmodifierlist)&#39;s name. Searchable. | [optional] 
**selection_type** | **str** | Indicates whether multiple options from the [CatalogModifierList](#type-catalogmodifierlist) can be applied to a single [CatalogItem](#type-catalogitem). See [CatalogModifierListSelectionType](#type-catalogmodifierlistselectiontype) for all possible values. | [optional] 
**modifiers** | [**list[CatalogObject]**](CatalogObject.md) | The options included in the [CatalogModifierList](#type-catalogmodifierlist). You must include at least one [CatalogModifier](#type-catalogmodifier). Each [CatalogObject](#type-catalogobject) must have type &#x60;MODIFIER&#x60; and contain [CatalogModifier](#type-catalogmodifier) data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


